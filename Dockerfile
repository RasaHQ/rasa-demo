# Pull SDK image as base image
FROM rasa/rasa-sdk:1.7.0

# Use subdirectory as working directory
WORKDIR /app

# Copy actions requirements
COPY actions/requirements-actions.txt ./

# Install extra requirements for actions code
RUN pip install -r requirements-actions.txt

# Copy actions code to working directory
COPY ./actions /app/actions
COPY setup.py /app

# Install modules from setup.py
RUN  pip install -e . --no-cache-dir

# Start the action server
CMD ["start", "--actions", "actions.actions"]
