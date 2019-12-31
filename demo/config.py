import os

policy_model_dir = os.environ.get("POLICY_MODEL_DIR", "models/dialogue/")

rasa_nlu_config = os.environ.get("RASA_NLU_CONFIG", "nlu_config.yml")

account_sid = os.environ.get("ACCOUNT_SID", "")

auth_token = os.environ.get("AUTH_TOKEN", "")

twilio_number = os.environ.get("TWILIO_NUMBER", "")

platform_api = os.environ.get("RASA_API_ENDPOINT_URL", "")

self_port = int(os.environ.get("SELF_PORT", "5001"))

core_model_dir = os.environ.get("CORE_MODEL_DIR", "models/dialogue/")

remote_core_endpoint = os.environ.get("RASA_REMOTE_CORE_ENDPOINT_URL", "")

rasa_core_token = os.environ.get("RASA_CORE_TOKEN", "")

mailchimp_api_key = os.environ.get("MAILCHIMP_API_KEY", "")

mailchimp_list = os.environ.get("MAILCHIMP_LIST", "")

gdrive_credentials = os.environ.get("GDRIVE_CREDENTIALS", "")

access_token = os.environ.get("TELEGRAM_TOKEN", "")

verify = os.environ.get("TELEGRAM_VERIFY", "rasas_bot")

webhook_url = os.environ.get("WEBHOOK_URL", "https://website-demo.rasa.com/webhook")

rasa_platform_token = os.environ.get("RASA_PLATFORM_TOKEN", "")

rasa_nlg_endpoint = os.environ.get("RASA_NLG_ENDPOINT_URL", "")

algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")

algolia_search_key = os.environ.get("ALGOLIA_SEARCH_KEY", "")

algolia_docs_index = os.environ.get("ALGOLIA_DOCS_INDEX", "")
