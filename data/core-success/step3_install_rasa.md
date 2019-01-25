## Get started from website (including privacy clause etc)
* get_started_step3
    - greet_success: action_greet_user

## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - getstarted_3: utter_ask_python_installed

## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda

## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda

## Install Rasa: Happy Path
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4

## Install Rasa: Happy Path
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4

## Install Rasa: Happy Path with already provided package_manager
* install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4

## Install Rasa: No Python installed
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build

## Install Rasa: Ask Python installed -> Which version
* install_rasa
    - getstarted_3: utter_ask_python_installed
* ask_faq_python_version
    - faq: action_faqs
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build

## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - getstarted_3: action_store_problem_description
    - getstarted_3: utter_direct_to_forum_for_help
    - getstarted_3_success: utter_direct_to_step4

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - getstarted_3: action_store_problem_description
    - getstarted_3: utter_direct_to_forum_for_help
    - getstarted_3_success: utter_direct_to_step4

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else

## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* technical_question OR enter_data OR out_of_scope
    - getstarted_3: action_store_problem_description
    - getstarted_3: utter_direct_to_forum_for_help
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum
    - getstarted_3: action_store_problem_description
    - faq: action_faqs

## Install Rasa: Ask ready to build -> No -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum
    - getstarted_3: action_store_problem_description
    - faq: action_faqs


## Install Rasa: Ask ready to build -> No  -> Problem -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum
    - getstarted_3: action_store_problem_description
    - faq: action_faqs
