FROM rasa/rasa-sdk:1.7.0

WORKDIR /app

COPY actions/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./actions /app/actions
COPY setup.py /app

RUN  pip install -e . --no-cache-dir

CMD ["start", "--actions", "actions.actions"]
