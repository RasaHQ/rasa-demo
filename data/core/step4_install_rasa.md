## Get started from website (including privacy clause etc)
* get_started_step4
    - action_greet_user
    - slot{"step": "4"}

## Install Rasa: Happy Path
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step5

## Install Rasa: Happy Path
* get_started_step4
    - action_greet_user
    - slot{"step":"4"}
* install_rasa OR affirm
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step5

## Install Rasa: No Python installed
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_installation_command
    - utter_ask_ready_to_build

## Install Rasa: Ask Python installed -> Which version
* install_rasa
    - utter_ask_python_installed
* ask_faq_python_version
    - action_faqs
    - utter_get_python
    - utter_installation_command
    - utter_ask_ready_to_build



