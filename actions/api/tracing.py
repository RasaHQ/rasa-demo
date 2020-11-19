import logging

from opentelemetry import baggage, trace
from opentelemetry.propagators import extract, inject
from opentelemetry.trace import get_current_span, set_span_in_context
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.trace.propagation.textmap import DictGetter
from opentelemetry.sdk.resources import Resource

# core exporters
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
    BatchExportSpanProcessor,
)
from opentelemetry.exporter.otlp.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter import jaeger

import contextlib
tracer = None
current_span = None

logger = logging.getLogger(__name__)
logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

tracer = None
current_span = None

def init_tracer(service_name):
    service_name = "rasa"

    resource = Resource(attributes={"service.name": service_name})
    trace.set_tracer_provider(TracerProvider(resource=resource))

    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(ConsoleSpanExporter())
    )

    otlp_exporter = OTLPSpanExporter(endpoint="localhost:55680", insecure="True")
    trace.get_tracer_provider().add_span_processor(
        BatchExportSpanProcessor(otlp_exporter)
    )

    jaeger_exporter = jaeger.JaegerSpanExporter(
        service_name=service_name,
        agent_host_name="localhost",
        agent_port=6831,
    )
    trace.get_tracer_provider().add_span_processor(
        BatchExportSpanProcessor(jaeger_exporter)
    )

    # this call also sets opentracing.tracer
    global tracer
    tracer = trace.get_tracer(__name__)  # returns opentelemetry.sdk.trace.Tracer object
    return tracer

def start_span(tracer, name, attributes=None):
    span = tracer.start_active_span(name)
    if attributes:
        for k, v in attributes.items():
            span.span.set_tag(k, v)
    return span

def extract_start_span(tracer, domain, name, attributes=None):
    if (domain and "headers" in domain):
        headers = domain["headers"]
        carrier_getter = DictGetter()

        ctx = extract(carrier_getter, headers)
        baggage_entries = baggage.get_all(context=ctx)
        logger.debug(f"extract_start_span, headers: {headers}, baggage_entries: {baggage_entries}")
        span_context = get_current_span(context=ctx).get_span_context()
        logger.debug(f"extract_start_span, span_context: {span_context}")

        span = trace.DefaultSpan(span_context)
        ctx = set_span_in_context(span, context=ctx)

        #span_ctx = tracer.extract(Format.HTTP_HEADERS, headers)
        #span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
        #logger.debug(f"extract_start_span, headers: {headers}, span_tags: {span_tags}")
        #span = tracer.start_active_span(name, child_of=span_ctx, tags=span_tags)
        return span
    else:
        logger.debug(f"extract_start_span, no header, domain: {domain}")
        return contextlib.nullcontext()

def inject(tracer, url):
    headers = {}
    span = tracer.active_span
    span.set_tag(tags.HTTP_METHOD, 'POST')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    tracer.inject(span, Format.HTTP_HEADERS, headers)
    #span_header = self.tracer.inject(span, Format.HTTP_HEADERS, headers)
    # tracer.inject(child_span.context, 'zipkin-span-format', text_carrier)
    return headers

#def extract(tracer, headers):
