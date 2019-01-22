## Generated Story goal:1 step, id:fbe7e1ee43b1405eb6577cdb883558d8, 15/01/19 4629665864994283838
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* enter_data{"number": 9}
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* affirm
    - utter_quickstart
    - utter_anything_else
* affirm
    - utter_what_help
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* affirm
    - utter_thumbsup
* deny
    - utter_nohelp
* affirm
    - utter_what_help
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:1bfcb89ff64341f8a856fec65e1aeca2, 07/01/19 8923318737579790833
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_time
    - action_chitchat
* ask_time
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* enter_data{"company": "Microsoft"}
    - action_store_unknown_product
    - slot{"unknown_product": "Microsoft"}
    - utter_no_guide_for_switch
    - utter_anything_else
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - action_default_ask_affirmation

## Generated Story goal:1 step, id:70921bd927364afd92913042c87f3289, 07/01/19 100382275354927073
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - action_greet_user

## Generated Story goal:chitchat, id:8307cdc26aed49d5a4a98f7714277d46, 07/01/19 1914445861236382035
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* bye
    - utter_bye

## Generated Story goal:sales, id:7df6d7f505074a53a9e90ee20f7e3869, 15/01/19 6475110632872315884
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* affirm
    - utter_thumbsup
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "accountant"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "for internal employees"}
    - utter_thank_usecase
    - utter_ask_budget
* bye
    - utter_bye
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:1 step, id:a251a6b415e244168043f96e0d4aded9, 07/01/19 593641502568558950
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
    - utter_also_explain_core

## Generated Story goal:sales, id:4bc8fef875534047b388ba6a14e11687, 15/01/19 3427957246853936316
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "I am plumber"}
    - utter_ask_usecase
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope{"number": 1}
    - action_default_ask_rephrase
* out_of_scope{"number": 1}
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* out_of_scope{"number": 1}
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_usecase

## Generated Story goal:1 step, id:a46ce83cbaa64a6085ce2262cfbc9764, 15/01/19 -3201029944716160294
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "watson"}
    - utter_no_guide_for_switch
    - utter_anything_else

## Generated Story goal:1 step, id:8b2984085e6445d08ea86c4905af1ab4, 15/01/19 7165157089960791365
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* bye
    - utter_bye
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout

## Generated Story goal:1 step, id:ad342ea0cbe44414acd1afda61705137, 15/01/19 4973900345118329436
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data
    - action_chitchat
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else
* enter_data
    - utter_not_sure
    - utter_possibilities
* deny
    - utter_nohelp
* enter_data
    - utter_not_sure
    - utter_possibilities
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup
* deny
    - utter_thumbsup
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* affirm
    - utter_what_help
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* bye
    - utter_bye

## Generated Story goal:1 step, id:db62e52efe3c4f84b437deac80137d02, 15/01/19 3838895679153575229
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - action_chitchat
    - utter_explain_nlucore
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* react_positive
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* react_positive
    - utter_ask_pip_or_conda

## Generated Story goal:chitchat, id:f4c3c53b13ac43378325e1c56b5f484e, 07/01/19 5332122666946064871
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_default_ask_affirmation
* ask_whatspossible
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: enter_data
    - form: feedback_form
    - slot{"feedback_message": "HJola"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* greet
    - action_default_ask_affirmation
* greet
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user

## Generated Story goal:1 step, id:012f30d6a8154fbab32dffd41c584ef7, 15/01/19 -6662803536974591812
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* affirm
    - utter_what_help
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - utter_getstarted_new
    - utter_built_bot_before
* how_to_get_started
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* ask_wherefrom
    - action_default_ask_affirmation
* ask_wherefrom
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* ask_wherefrom
    - action_chitchat

## Generated Story goal:1 step, id:78e3cf5772174fbf9db0b3ebf16c0a89, 07/01/19 -8745616666398737387
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - action_chitchat
* technical_question
    - utter_not_sure
    - utter_possibilities
* bye
    - utter_bye
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:a67bff8ff589455a89519aaada17e952, 15/01/19 2304876415402087605
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* greet
    - action_greet_user
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_fallback
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:rasa_help, id:1ea8190f19c841c6ab7dc7c4544a41b1, 15/01/19 -4042678351450787643
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* canthelp
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* how_to_get_started{"product": "core"}
    - utter_ask_for_nlu_specifics
* ask_whatisrasa
    - action_chitchat
    - utter_ask_for_nlu_specifics

## Generated Story goal:1 step, id:f58967374e05402e8e2baa7a96bce56b, 15/01/19 -6126456534379029119
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_tryout
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:8d68ea22666845a29ac5f1bed03464f2, 15/01/19 7141169605040788581
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* enter_data
    - action_faqs
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* ask_whatspossible
    - action_chitchat

## Generated Story goal:oos, id:1377af6a3e98484695e9e1bb5d2a7c05, 15/01/19 -1165950991246183909
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - action_default_ask_affirmation
* ask_whatisrasa
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - action_chitchat
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else

## Generated Story goal:1 step, id:77dd2e06abb64b0789a0fda2845db7b4, 15/01/19 -5131068832767696714
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:153cf37f7e5f4c5aa3ce2fe66e1b3324, 15/01/19 -622266475627768804
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howold
    - action_chitchat
* react_positive
    - utter_react_positive
* ask_weather
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data
    - utter_not_sure
    - utter_possibilities
* canthelp
    - action_default_ask_affirmation
* ask_faq_platform
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_platform
    - action_faqs
* out_of_scope
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:1 step, id:f0e34ace757848bd86d9b9548e1e311b, 15/01/19 -561252308693303088
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_ask_migration
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "noooooooooooooooooooooooooooooooooooooooo"}
    - utter_no_guide_for_switch
    - utter_anything_else
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else

## Generated Story goal:1 step, id:fb75f75f6fe34f6b92c771f93315188e, 15/01/19 -4792259829584148949
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - utter_getstarted_new
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:1 step, id:90fe793b62464e48a764df952cc2b22d, 15/01/19 2712483524640120030
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_ask_affirmation
* install_rasa
    - action_revert_fallback_events
    - rewind
    - rewind
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4
    - utter_anything_else

## Generated Story goal:1 step, id:e977c395a2404bef8ba7f0c3b7e65970, 07/01/19 -4133629017110263203
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:6b52adb1fd2744159997728397c9dd16, 15/01/19 2425289827982194203
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatismyname
    - action_chitchat
* ask_howdoing
    - action_default_ask_affirmation
* ask_whatspossible
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:c0e23ddef4af464faf60b1ab6f858bfd, 15/01/19 5696486632048569640
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* thank
    - utter_noworries
    - utter_anything_else

## Generated Story goal:1 step, id:da5443027739425eafa0772168f90317, 07/01/19 740792119035148927
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - action_chitchat
* how_to_get_started
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data{"number": 1}
    - utter_not_sure
    - utter_possibilities
* ask_how_contribute
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* technical_question
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* technical_question
    - utter_not_sure
    - utter_possibilities
* nlu_info
    - utter_moreinformation
    - utter_ask_jobfunction
* bye
    - utter_bye

## Generated Story goal:1 step, id:030829eb30ed4339985d7e71737f6c2d, 07/01/19 -7258636486743144222
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* enter_data
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_howbuilt
    - action_faqs
* greet
    - action_greet_user
* ask_howbuilt
    - action_faqs
* ask_isbot
    - action_chitchat
* ask_howold
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* ask_restaurant
    - action_chitchat
* ask_whatismyname
    - action_chitchat
* ask_wherefrom
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* ask_whatspossible
    - action_default_ask_affirmation
* ask_whatspossible
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatspossible
    - action_chitchat
* ask_howdoing
    - action_chitchat
* deny
    - utter_nohelp
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities
* technical_question
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_not_sure
    - utter_possibilities
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_weather
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_built_bot_before
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* enter_data
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* ask_builder
    - action_chitchat
* enter_data
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_explain_nlucore
* canthelp
    - action_default_ask_affirmation
* canthelp
    - action_revert_fallback_events
    - rewind
    - rewind
* canthelp
    - utter_canthelp
* affirm
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* enter_data
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* greet
    - action_greet_user
* greet
    - action_greet_user
* greet
    - action_greet_user

## Generated Story goal:chitchat, id:88ebaeaad43746b780c71a5ebc8d38bb, 15/01/19 -8271989480098550076
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat

## Generated Story goal:1 step, id:e98d90f69e6a42caa755096d4abb3c32, 15/01/19 9189673651972713439
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* affirm
    - utter_quickstart
    - utter_anything_else
* affirm
    - utter_what_help
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
* deny
    - utter_quickstart
    - utter_anything_else
* affirm
    - action_default_fallback
    - rewind
* enter_data
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase

## Generated Story goal:1 step, id:6a2529aa1d884d31a8c7c0d6af469c2d, 15/01/19 7200423024140642742
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_thumbsup

## Generated Story goal:chitchat, id:5f62783b86044d23bd7794aea5e452ab, 15/01/19 8744703047075004721
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* greet
    - action_greet_user
* technical_question
    - action_default_ask_affirmation

## Generated Story goal:1 step, id:cf0133aaeb124daa9ca16f1eb347bf10, 15/01/19 2360949747906668266
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_builder
    - action_chitchat
* affirm
    - utter_thumbsup
    - utter_anything_else
* affirm
    - utter_thumbsup
    - utter_anything_else
* affirm
    - utter_what_help
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* ask_isbot
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
    - rewind
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind

## Generated Story goal:1 step, id:ba54c0bf83234d259d61cd4f47cc0539, 15/01/19 -6992858238711560495
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else
* bye
    - utter_bye

## Generated Story goal:1 step, id:ad0082d72d7e49d69808ad6f9bbaf188, 15/01/19 -3403665775285095855
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* telljoke
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - action_default_fallback
    - rewind
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_tryout
* ask_whatspossible
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_already_subscribed
    - action_store_problem_description
    - slot{"problem_description": "/technical_question"}
    - utter_direct_to_forum_for_help

## Generated Story goal:1 step, id:01ec0d8709774580be6bebccd5d4f304, 15/01/19 2789662006018320349
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_default_ask_affirmation
* greet
    - action_revert_fallback_events
    - rewind
    - rewind
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build

## Generated Story goal:1 step, id:8de3043014ab4fc9b93aa2dbc4a664bd, 15/01/19 -7389871270274305559
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* technical_question
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:chitchat, id:744e301ea3b24d7b81eaecaef484a78d, 15/01/19 6992719149773312499
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* ask_whoisit
    - action_chitchat
    - utter_ask_which_product
* ask_wherefrom
    - action_chitchat
    - utter_ask_which_product
* deny
    - utter_thumbsup
* ask_builder
    - action_chitchat
* ask_whoisit
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* ask_whatismyname
    - action_default_ask_affirmation
* out_of_scope
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_whoisit
    - form: feedback_form
    - slot{"feedback_message": "what's your name ? "}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* ask_whoisit
    - action_chitchat
* affirm
    - action_default_ask_affirmation
* ask_howold
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_howold
    - action_chitchat
* affirm
    - utter_thumbsup
    - utter_anything_else
* out_of_scope
    - action_default_ask_affirmation
* handleinsult
    - action_revert_fallback_events
    - rewind
    - rewind
* handleinsult
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* ask_whatspossible
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_builder
    - form: feedback_form
    - slot{"feedback_message": "do you know your creator?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* ask_builder
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:oos, id:ad5cb2e9ffd2475dbe292e78776059da, 07/01/19 1534267360063758451
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:1 step, id:580be59e052a493c8671425ba2091e3c, 15/01/19 418864053207021990
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - utter_not_sure
    - utter_possibilities
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_ask_jobfunction
* affirm
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* affirm
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:fa900520d5e64fbd8ae220d497dd52e4, 15/01/19 -6028052822562435970
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started
    - action_default_ask_affirmation
* greet
    - action_revert_fallback_events
    - rewind
    - rewind
* greet
    - action_greet_user
* affirm
    - utter_thumbsup
* handleinsult
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "AI"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "for shopping"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 1000}
    - action_store_budget
    - slot{"budget": 1000}
    - utter_sales_contact
    - utter_ask_name
* bye
    - utter_bye
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* bye
    - utter_bye
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* bye
    - utter_bye
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction

## Generated Story goal:1 step, id:fa57a60f59a2486fb19d6f42cbab70f9, 07/01/19 5988073508111598327
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:chitchat, id:0450b69ee3fe4e46a5066821c15e09be, 15/01/19 -7650645840543823668
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_isbot
    - action_default_ask_affirmation
* ask_whatspossible
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatspossible
    - action_chitchat
* ask_whatisrasa
    - action_default_ask_affirmation
* ask_whatisrasa
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - action_chitchat
* ask_builder
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:1 step, id:c715a29a766e400d84c6256f318a65d1, 07/01/19 -5364447702579674323
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_time
    - action_chitchat
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - action_default_ask_affirmation
* enter_data
    - action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - action_chitchat
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core

## Generated Story goal:2 step, id:fc252d1c4d3e4c0a8f875e803b7499cc, 15/01/19 6757292788445129790
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* affirm
    - utter_what_language
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_great
    - utter_anything_else
* how_to_get_started
    - action_default_ask_affirmation
* how_to_get_started
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: how_to_get_started
    - form: feedback_form
    - slot{"feedback_message": "How is RASA implemented?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* technical_question
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## Generated Story goal:1 step, id:cd121547e7fc42029d2c5e2fcf087720, 15/01/19 6948790501422549601
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet{"name": "Hello Sara"}
    - slot{"name": "Hello Sara"}
    - action_greet_user
* greet
    - action_greet_user
* ask_isbot
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - action_default_ask_affirmation
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_ask_affirmation
* how_to_get_started
    - action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:b65bed27b7074001b53ac39fdcceefb2, 07/01/19 -2129662501281030472
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* affirm
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:- , id:7bf50ce15a9f4676a7251a1224a22065, 07/01/19 3367136367191026706
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* enter_data
    - action_store_unknown_nlu_part
    - slot{"unknown_nlu_part": "Sabari"}
    - utter_also_explain_nlu
    - utter_explain_nlu
    - utter_tryout
* handleinsult
    - action_chitchat
    - utter_tryout
* enter_data
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:oos, id:c8eacfc7cce24b4d9baaa050d07650ba, 15/01/19 -7081680720226590930
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* bye
    - utter_bye
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:chitchat, id:f110cd4e94e74d18ad13bc3841cf1b3a, 07/01/19 -8418791999824156208
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_why_contribute
    - utter_reasons_to_contribute
* technical_question
    - action_default_ask_affirmation

## Generated Story goal:sales, id:569732e5b643453f83e7d8d0197c1a52, 07/01/19 1840925658634245894
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction

## Generated Story goal:3 step, id:7cfbec2eca784182b9a5ae8e3851ca15, 15/01/19 865677131177674452
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* install_rasa
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:19fbc64473284ed69f499d07080ddc8b, 15/01/19 -273240240198314851
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "lex"}
    - utter_no_guide_for_switch
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Generated Story goal:1 step, id:73d92392085d4da3a86b580a3b9d4248, 07/01/19 3775594580362055824
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before

## Generated Story goal:1 step, id:59e507a9ecc44c9798808c00042e70d8, 07/01/19 4447288418699935227
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:dd7c3e3d448a48edafbbbb74fc5246e1, 15/01/19 -1878090982363519595
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - utter_not_sure
    - utter_possibilities
* ask_faq_python_version
    - action_default_ask_affirmation
* ask_faq_python_version
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_python_version
    - action_faqs

## Generated Story goal:1 step, id:e2906f19c3ee42eab60d237f6a297359, 15/01/19 7760411919118564049
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:chitchat, id:20529eecff9b49f8bf078414db536645, 15/01/19 -6315971859175363985
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_weather
    - action_chitchat

## Generated Story goal:1 step, id:b9a078575f4f42afa78e100558926933, 15/01/19 -4790788206339395125
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:861051585c9948038e3267da99febf84, 07/01/19 -7800403332510320240
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* out_of_scope
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* out_of_scope
    - action_default_ask_affirmation

## Generated Story goal:1 step, id:df3590cfb4fa4bc392e33f362568509e, 07/01/19 293725981827925484
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_default_ask_affirmation
* ask_whatisrasa
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* thank
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:1 step, id:bd3617e5a9484e989a32e708bde9f45b, 15/01/19 1615601269360005792
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* enter_data
    - action_faqs
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:chitchat, id:3bd88ff734794ffd92ada7d1b76af5e0, 15/01/19 -5548846580224832469
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_howbuilt
    - action_faqs
* ask_wherefrom
    - action_chitchat
* deny
    - action_default_ask_affirmation
* ask_weather
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_howdoing
    - form: feedback_form
    - slot{"feedback_message": "how are you"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* enter_data
    - action_store_email
    - rewind
* handleinsult
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
* ask_languagesbot
    - action_default_ask_affirmation
* ask_languagesbot
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_languagesbot
    - action_chitchat
* deny
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* telljoke
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* telljoke
    - action_chitchat
* react_positive
    - utter_react_positive
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_languagesbot
    - action_chitchat
* human_handoff
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* greet
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* greet
    - action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_default_ask_affirmation
* enter_data
    - action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: technical_question
    - form: feedback_form
    - slot{"feedback_message": "how to set you on my computer"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* enter_data
    - utter_not_sure
    - utter_possibilities

## Generated Story goal:faq, id:6967554c12dc40aebf9a3b8a0c3b74d4, 07/01/19 166454228512366715
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope{"language": "french"}
    - slot{"language": "french"}
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* ask_faq_languages
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_faq_languages
    - action_faqs
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation
* ask_faq_differencecorenlu
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_differencecorenlu
    - action_faqs
* ask_faq_opensource{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_faqs
* thank
    - utter_noworries
    - utter_anything_else

## Generated Story goal:1 step, id:b7167aedaa2a4e3294e0fc73d14cd3ed, 15/01/19 4273706625809797937
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:1 step, id:acff2c771f5647198f579aea42f6c8af, 07/01/19 -6531370308264216877
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* affirm
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:chitchat, id:f2bee91f651246819ccae9d79c098da1, 15/01/19 1607697536649079281
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* out_of_scope
    - action_default_ask_rephrase
* ask_howdoing
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_howdoing
    - action_chitchat

## Generated Story goal:1 step, id:e623122741de482b8a9aaf06d17e517f, 07/01/19 554666083130913654
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* thank
    - utter_anything_else
* deny
    - utter_nohelp
* affirm
    - utter_thumbsup
* bye
    - utter_bye

## Generated Story goal:1 step, id:5ada6738d9bb48fd84030506d978c1a6, 15/01/19 -5182569078098808488
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind
* deny
    - action_default_fallback
    - rewind

## Generated Story goal:3 step, id:d1d88be66a994103ab27e6cae2c84fc8, 15/01/19 7654312050691501155
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* install_rasa
    - utter_moreinformation
    - utter_ask_jobfunction
* deny
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else

## Generated Story goal:chitchat, id:ae9b7b36cae746bf8981ab208f7c9c37, 07/01/19 4505107635077792707
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* rasa_cost
    - action_default_ask_affirmation
* rasa_cost
    - action_revert_fallback_events
    - rewind
    - rewind
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else

## Generated Story goal:chitchat, id:fc4b631beaae491aae8f583c55befe23, 07/01/19 -6864320238022187937
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy": true}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* greet
    - action_default_ask_affirmation
* ask_builder
    - action_revert_fallback_events
    - rewind
    - rewind
* ask_builder
    - action_chitchat
* out_of_scope
    - action_default_ask_affirmation
* deny
    - action_default_ask_rephrase
* affirm
    - action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* affirm
    - utter_thumbsup
* affirm
    - action_default_ask_affirmation
* technical_question
    - action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - action_store_problem_description
    - slot{"problem_description": "/technical_question"}
    - utter_direct_to_forum_for_help

