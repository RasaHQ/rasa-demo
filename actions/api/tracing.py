import logging
from jaeger_client import Config
from opentracing.ext import tags
from opentracing import Format, UnsupportedFormatException
import contextlib

logger = logging.getLogger(__name__)
logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

def init_tracer(service):
    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'reporter_batch_size': 1,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

def start_span(tracer, name, attributes=None):
    span = tracer.start_active_span(name)
    if attributes:
        for k, v in attributes.items():
            span.span.set_tag(k, v)
    return span

def extract_start_span(tracer, domain, name, attributes=None):
    if (domain and "headers" in domain):
        headers = domain["headers"]
        span_ctx = tracer.extract(Format.HTTP_HEADERS, headers)
        span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
        #span = tracer.start_active_span(name)
        logger.debug(f"extract_start_span, headers: {headers}, span_tags: {span_tags}")
        span = tracer.start_active_span(name, child_of=span_ctx, tags=span_tags)
        #if attributes:
        #    for k, v in attributes.items():
        #        span.span.set_tag(k, v)
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
