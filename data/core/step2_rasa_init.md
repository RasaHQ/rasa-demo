## Get started from website
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build

## Get started from website + not interested in step 2
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* deny
    - utter_anything_else

## Direct "install Rasa"
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build

## Installation went well
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* affirm
    - utter_run_rasa_init
    - utter_direct_to_step3

## Installation went well
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* affirm
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - slot{"problem_description": "I don't know how to customize the pipeline"}
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - slot{"problem_description": "I don't know how to customize the pipeline"}
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (cut to the chase)
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (cut to the chase)
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (but FAQ)
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* ask_faq_ee OR ask_faq_human_languages_rasa OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (but FAQ)
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* ask_faq_ee OR ask_faq_human_languages_rasa OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (but FAQ + cut to the chase)
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* ask_faq_ee OR ask_faq_human_languages_rasa OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Problems installing (but FAQ + cut to the chase)
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* ask_faq_ee OR ask_faq_human_languages_rasa OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## Just don't want to continue
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else

## Just don't want to continue
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else
