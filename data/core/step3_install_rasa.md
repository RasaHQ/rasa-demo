## Get started from website (including privacy clause etc)
* get_started_step3
    - action_greet_user

## Install Rasa Happy Path
* install_rasa
  - utter_ask_python_installed
* mood_confirm
  - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
  - action_select_installation_command
  - utter_ask_ready_to_build
* mood_confirm
  - utter_get_starter_pack
  - utter_direct_to_step4
  - utter_anything_else

## Install Rasa: No Python installed
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build

## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* mood_confirm
    - utter_ask_describe_problem
* technical_question or enter_data or out_of_scope
    - action_store_problem_description
    - utter_direct_to_forum_for_help

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question or enter_data or out_of_scope
    - action_store_problem_description
    - utter_direct_to_forum_for_help

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else

## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"}
  - action_select_installation_command
  - utter_ask_ready_to_build
* technical_question or enter_data or out_of_scope
  - action_store_problem_description
  - utter_direct_to_forum_for_help
* mood_confirm OR thank
    - utter_anything_else
