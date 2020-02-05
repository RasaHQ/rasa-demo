FROM rasa/rasa-sdk:1.7.0

WORKDIR /app

COPY demo/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./demo /app/demo
COPY setup.py /app

RUN  pip install -e . --no-cache-dir

CMD ["start", "--actions", "demo.actions"]
