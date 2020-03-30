FROM rasa/rasa-sdk:1.9.0

WORKDIR /app

COPY demo/requirements.txt ./

USER root

RUN pip install -r requirements.txt

COPY ./demo /app/demo
COPY setup.py /app

RUN  pip install -e . --no-cache-dir

USER 1001

CMD ["start", "--actions", "demo.actions"]
