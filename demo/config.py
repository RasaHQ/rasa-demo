from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os

policy_model_dir = os.environ.get("POLICY_MODEL_DIR", "models/dialogue/")

rasa_nlu_config = os.environ.get("RASA_NLU_CONFIG", "nlu_config.yml")

account_sid = os.environ.get("ACCOUNT_SID", "")

auth_token = os.environ.get("AUTH_TOKEN", "")

twilio_number = os.environ.get("TWILIO_NUMBER", "")

platform_api = os.environ.get("PLATFORM_API", "")

self_port = int(os.environ.get("SELF_PORT", "5001"))

core_model_dir = os.environ.get("CORE_MODEL_DIR", "models/dialogue/")

remote_core_endpoint = os.environ.get("RASA_REMOTE_CORE_ENDPOINT_URL", "")

rasa_core_token = os.environ.get("RASA_CORE_TOKEN", "")
