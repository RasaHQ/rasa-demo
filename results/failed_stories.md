## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_whatisrasa
    - fallback: action_default_ask_affirmation
* deny
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "what is your address?"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - None: action_restart   <!-- predicted: subscribe -->


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - chitchat: action_default_ask_affirmation
* ask_wherefrom
    - fallback: action_revert_fallback_events


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - chitchat: action_chitchat   <!-- predicted: fallback -->
* handleinsult
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - chitchat: action_chitchat   <!-- predicted: fallback -->
* handleinsult
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - chitchat: action_chitchat   <!-- predicted: fallback -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: action_default_ask_affirmation
* bye
    - fallback: action_revert_fallback_events


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - chitchat: action_chitchat   <!-- predicted: fallback -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - chitchat: action_chitchat   <!-- predicted: fallback -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_time
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* ask_why_contribute
    - getstarted_4_success: utter_reasons_to_contribute   <!-- predicted: getstarted_1 -->
* handleinsult
    - chitchat: action_default_ask_affirmation
* handleinsult
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - None: action_restart   <!-- predicted: subscribe -->


## Generated Story goal:1 step, id:ad02fffc3bd841788f5b10e283fe2ab8, 12/17/18 7345417199532554495
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_faqs
    - getstarted_1_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* affirm
    - rasa_help: utter_ask_migration
* deny
    - rasa_help: utter_explain_stack
    - rasa_help: utter_stack_details
    - rasa_help: utter_explain_nlucore
* affirm
    - rasa_help: utter_explain_nlu
    - rasa_help: utter_also_explain_core   <!-- predicted: getstarted_1 -->
* affirm
    - rasa_help: utter_tryout
* enter_data
    - chitchat: action_store_email


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* enter_data
    - chitchat: action_default_ask_affirmation
* greet
    - fallback: action_revert_fallback_events


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* enter_data
    - chitchat: action_default_ask_affirmation


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* greet
    - greet_success: action_default_fallback


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* affirm
    - chitchat: action_store_problem_description
    - slot{"problem_description": "yes"}
    - chitchat_fail: action_faqs
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* affirm
    - chitchat: action_default_ask_affirmation
* telljoke
    - fallback: action_revert_fallback_events


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* affirm
    - chitchat: action_store_problem_description
    - slot{"problem_description": "yes"}
    - chitchat_fail: action_faqs
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* affirm
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* ask_isbot
    - chitchat: action_default_fallback


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* deny
    - fallback: action_revert_fallback_events


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* deny
    - chitchat: utter_nohelp
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* enter_data
    - chitchat: utter_quickstart_nlu_only
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_ask_affirmation
* out_of_scope
    - fallback: action_default_ask_rephrase
* deny
    - fallback: action_revert_fallback_events


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* deny
    - chitchat: utter_nohelp
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* enter_data
    - chitchat: utter_quickstart_nlu_only
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_ask_affirmation
* out_of_scope
    - fallback: action_default_ask_rephrase


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* deny
    - chitchat: utter_nohelp
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* enter_data
    - chitchat: utter_quickstart_nlu_only
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_ask_affirmation


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* technical_question
    - faq: action_default_fallback


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_howdoing
    - chitchat: action_default_fallback


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: action_default_fallback


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_default_fallback


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* bye
    - chitchat: utter_bye
* nlu_info
    - rasa_help: action_default_fallback


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* bye
    - chitchat: utter_bye
* deny
    - chitchat: action_default_fallback


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_whatspossible
    - fallback: action_revert_fallback_events


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_default_ask_affirmation


## Generated Story goal:oos , id:5a1c8e47b3ba4dc38b2a3de3ffedee30, 12/17/18 4221492392327213787
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_whoisit
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - rasa_help_fail: utter_thumbsup   <!-- predicted: rasa_help -->
* ask_whatspossible
    - chitchat: action_chitchat


## Generated Story goal:subscribe, id:ee59175ac0a64f468b1b4559296f359a, 12/17/18 7101882852510041551
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "blah"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "chat "}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": 1}
    - sales: action_store_budget
    - slot{"budget": 1}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "bi"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name": "q"}
    - sales: utter_ask_businessmail
* bye
    - sales_fail: utter_bye   <!-- predicted: sales -->


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:1bc7a86220da42588b30b2a5566b00dc, 12/17/18 940448344067621014
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - getstarted_1: utter_great   <!-- predicted: chitchat -->
    - getstarted_1_fail: utter_ask_email
* enter_data{"email": "f.madureira@gmail.com"}
    - slot{"email": "f.madureira@gmail.com"}
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_store_email
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else


## Generated Story goal:1 step, id:269eec083b394990820028bb4ef61d01, 12/17/18 -7615535506954100338
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239


## Generated Story goal:1 step, id:4f647cb2427c495dbff5cf6fa1d7feb9, 12/15/18 -1171376024735749581
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_quickstart
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:ad02fffc3bd841788f5b10e283fe2ab8, 12/17/18 7345417199532554495
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_faqs
    - getstarted_1_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* affirm
    - rasa_help: utter_ask_migration
* deny
    - rasa_help: utter_explain_stack
    - rasa_help: utter_stack_details
    - rasa_help: utter_explain_nlucore
* affirm
    - rasa_help: utter_explain_nlu
    - rasa_help: utter_also_explain_core   <!-- predicted: getstarted_1 -->
* affirm
    - rasa_help: utter_tryout
* affirm
    - rasa_help: action_faqs
    - rasa_help_fail: utter_tryout   <!-- predicted: rasa_help -->
* enter_data{"email": "urandombg@abv.bg"}
    - slot{"email": "urandombg@abv.bg"}
    - slot{"email": "urandombg@abv.bg"}
    - subscribe: action_store_email
    - slot{"email": "urandombg@abv.bg"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - chitchat: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat_fail: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat_fail: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat_fail: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build   <!-- predicted: getstarted_3 -->
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* affirm
    - chitchat: action_store_problem_description
    - slot{"problem_description": "yes"}
    - chitchat_fail: action_faqs
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user


## Generated Story goal:1 step, id:db1d15d9e40047ebb3e8c13bbd0810b3, 12/15/18 2742610268326907746
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* deny
    - chitchat: utter_nohelp
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* enter_data
    - chitchat: utter_quickstart_nlu_only
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* deny
    - chitchat: utter_nohelp


## Generated Story goal:1 step, id:9978f875abec4c3c9955ec3d5dae51b1, 12/15/18 1526679696595893973
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details   <!-- predicted: getstarted_1_fail -->
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu   <!-- predicted: getstarted_1_success -->
    - getstarted_1: utter_also_explain_core
* enter_data{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - chitchat: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart
    - getstarted_1_fail: utter_anything_else


## Generated Story goal:1 step, id:16439d767388463d93e9c827767bca96, 05/01/19 -5426994757726665781
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* greet
    - greet_success: action_greet_user


## Generated Story goal:1 step, id:0da3c44e9839403eafaa89050e2b8d3e, 12/15/18 726412975159353253
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details   <!-- predicted: getstarted_1_fail -->
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_select_installation_command
    - getstarted_1_fail: utter_ask_ready_to_build
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - None: action_listen   <!-- predicted: chitchat_fail -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - getstarted_1: action_greet_user
    - getstarted_1_fail: utter_stack_details
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* bye
    - chitchat: utter_bye


## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916, 12/15/18 -5644677460292251299
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:2d42a9856ff545b5a1705e76aa2024ce, 12/17/18 -3109717157276131254
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:7c9b8897dcbe4b46af67aa5b2290dc4f, 12/17/18 -1844283597923529811
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: action_store_unknown_product
    - slot{"unknown_product": "hubot"}
    - getstarted_1_success: utter_no_guide_for_switch
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_time
    - chitchat: action_chitchat
* telljoke{"user_type": "new"}
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities


## Generated Story goal:1 step, id:8f756ee8a18e4f658946110f224aeb78, 05/01/19 -2911689985886478407
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - getstarted_3: action_faqs
    - getstarted_3_fail: utter_explain_nlucore
* greet
    - greet_success: action_greet_user
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* technical_question
    - faq: action_greet_user
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* enter_data
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* technical_question
    - faq: action_store_problem_description
    - slot{"problem_description": "error syntax"}
    - faq_success: utter_direct_to_forum_for_help
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - getstarted_3_fail: utter_duckling
    - getstarted_3_fail: utter_anything_else
* install_rasa
    - getstarted_3: action_store_budget
    - slot{"budget": "i need to install in my computer"}
    - getstarted_3_fail: utter_sales_contact
* install_rasa
    - getstarted_3: action_faqs
* greet
    - greet_success: action_store_budget
    - slot{"budget": "hello"}
    - greet_fail: utter_quickstart_nlu_only
    - greet_fail: utter_quickstart
    - greet_fail: utter_direct_install
    - greet_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_quickstart_nlu_only
    - getstarted_3_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding_fail: utter_thumbsup   <!-- predicted: onboarding -->
* ask_howdoing
    - chitchat: action_chitchat
* ask_how_contribute
    - getstarted_4: utter_not_sure
    - getstarted_4_fail: utter_possibilities   <!-- predicted: getstarted_4 -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else
* ask_whatisrasa
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:120a458cbe094db9b49c0d2a9adca7ca, 12/15/18 -7037911620927207371
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted   <!-- predicted: chitchat -->
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else


