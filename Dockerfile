# NB! when updating make sure the version is in sync with:
# * rasa version in requirements.txt
# * RASA_VERSION and RASA_X_VERSION  in .github/workflows/continuous-deployment.yml
# Pull SDK image as base image
FROM rasa/rasa-sdk:2.8.3

# Use subdirectory as working directory
WORKDIR /app

# Copy actions requirements
COPY actions/requirements-actions.txt ./

# Change to root user to install dependencies
USER root

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  python3 \
  python3-venv \
  python3-pip \
  python3-dev \
  # required by psycopg2 at build and runtime
  libpq-dev \
  # required for health check
  curl \
  && apt-get autoremove -y

# Make sure that all security updates are installed
RUN apt-get update && apt-get dist-upgrade -y --no-install-recommends

# Install extra requirements for actions code
RUN pip install -r requirements-actions.txt

# Copy actions code to working directory
COPY ./actions /app/actions

# Install modules from setup.py
COPY setup.py /app
COPY README.md /app
RUN pip install . --no-cache-dir

# Download spacy language data
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en

# Don't use root user to run code
USER 1001

# Start the action server
CMD ["start", "--actions", "actions.actions"]
