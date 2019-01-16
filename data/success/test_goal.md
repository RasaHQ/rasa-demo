## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* affirm
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* affirm
    - getstarted_3: action_default_ask_affirmation
* ask_whatspossible
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_whatismyname
    - form: feedback: feedback_form
    - slot{"feedback_message": "what i have to do"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart

## Generated Story goal:1 step, id:93b8b449ab074a6f973da26067b5c163, 12/17/18 -6676267086559597786
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* technical_question
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
* enter_data{"number": 1}
    - getstarted_1_fail: utter_great
    - getstarted_1: utter_ask_email
* deny
    - subscribe: utter_cantsignup

## Generated Story goal:1 step, id:5b7be2c22b874342aeca4216cfd5d35a, 12/15/18 1624335723075150223
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_fallback
    - rewind
* out_of_scope
    - oos: utter_out_of_scope
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:1 step, id:3a1c70eaf9234bb6b27160abfb6d1f88, 12/15/18 3863097957169160390
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_possibilities
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
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* affirm
    - chitchat: utter_thumbsup

## Generated Story goal:1 step, id:ef54f3457dd947be9f7ccdfa66d146ce, 12/17/18 -4040032104474387651
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
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
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore
* out_of_scope{"product": "core", "number": 1}
    - slot{"product": "core"}
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup

## Generated Story goal:1 step, id:19722107f07a4120bef398ea514e00de, 12/15/18 3342731703903234413
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"language": "chinese"}
    - slot{"language": "chinese"}
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
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:3 step, id:6ce300612cda42c1a084c292455056f7, 12/15/18 3997558787082995527
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build

## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
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
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - faq: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* enter_data
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Generated Story goal:1 step, id:3c9cd2509a78495bb5fd306618a9ba8e, 12/17/18 3076997113982385599
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* enter_data
    - onboarding_fail: action_greet_user
* affirm
    - getstarted_1_fail: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_fail: utter_quickstart
    - chitchat: utter_anything_else
* source_code
    - faq: utter_source_code
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:3914c48acca940c5bd30abc469b30e63, 05/01/19 9035562821004117390
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat

## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e, 12/15/18 3415830769284134354
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howold{"number": 42}
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: utter_possibilities

## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* out_of_scope
    - oos: action_default_ask_affirmation
* out_of_scope
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: out_of_scope
    - form: feedback: feedback_form
    - slot{"feedback_message": "docs"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart

## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_default_fallback
    - rewind
* nicetomeeyou
    - chitchat: action_default_fallback
    - rewind
* nicetomeeyou
    - chitchat: action_default_fallback
    - rewind
* nicetomeeyou
    - chitchat: action_default_fallback
    - rewind
* nicetomeeyou
    - chitchat: action_default_fallback
    - rewind
* canthelp
    - chitchat: action_default_fallback
    - rewind
* ask_faq_opensource
    - faq: action_default_fallback
    - rewind
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* affirm
    - chitchat: action_default_fallback
    - rewind
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - subscribe: action_default_fallback
    - rewind
* enter_data
    - subscribe: action_store_email
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - subscribe: utter_direct_install
    - subscribe_fail: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:3 step, id:953db2ccbe0748c586f5904a1b9b4432, 12/15/18 -2802431565840004587
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* ask_howdoing
    - chitchat: action_chitchat

## Generated Story goal:oos, id:ed1418fcc3884157bcc96a7c43d21ec0, 05/01/19 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
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
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_default_ask_affirmation
* ask_whatspossible
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_default_ask_affirmation
* install_rasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* install_rasa
    - getstarted_3: utter_ask_python_installed
* enter_data
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build

## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - utter_first_bot_with_rasa
* ask_whatspossible
    - chitchat: action_chitchat
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
    - slot{"unknown_product": "Cleverbot"}
    - getstarted_1_success: utter_no_guide_for_switch
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* affirm
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_weather
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_weather
    - chitchat: action_chitchat

## Generated Story goal:faq, id:db852c1fc7144db09e449fec4567614e, 12/17/18 -5129452726289215743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else

