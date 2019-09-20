## Get started from website
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_run_rasa_init
    - utter_direct_to_step3

## Get starter from website + deny
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* deny
    - utter_anything_else


<!-- Checkpoints -->
## Get started from website
* get_started_step4
    - action_greet_user
    - slot{"step": "4"}
* affirm OR install_rasa
> get_started_with_installation

## Get started directly
* install_rasa
> get_started_with_installation


<!-- Stories -->
## Python installed
> get_started_with_installation
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_direct_to_step5

## Python installed + problems
> get_started_with_installation
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_direct_to_step5

## Python installed + FAQ on which version
> get_started_with_installation
    - utter_ask_python_installed
* ask_faq_python_version
    - action_faqs
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build

## Python installed + problems (cut to the chase)
> get_started_with_installation
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_direct_to_step5

## Python not installed
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* affirm
    - utter_direct_to_step5

## Python not installed + problems
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_direct_to_step5

## Python not installed + problems (cut to the chase)
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_direct_to_step5

## Python not installed + FAQ
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_store_problem_description
    - action_faqs
    - utter_direct_to_step5

## Python not installed + FAQ (cut to the chase)
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_store_problem_description
    - action_faqs
    - utter_direct_to_step5

## Python installed + simply not ready to build
> get_started_with_installation
    - utter_ask_python_installed
* affirm
    - utter_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else

## Python not installed + simply not ready to build
> get_started_with_installation
    - utter_ask_python_installed
* deny
    - slot{"new_to_python": true}
    - utter_get_python
    - utter_installation_command_followup
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else


