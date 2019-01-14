## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - fallback: action_default_fallback
    - rewind
* handleinsult
    - fallback: action_default_fallback
    - rewind
* nicetomeeyou
    - fallback: action_default_fallback
    - rewind
* nicetomeeyou
    - fallback: action_default_fallback
    - rewind
* nicetomeeyou
    - fallback: action_default_fallback
    - rewind
* nicetomeeyou
    - fallback: action_default_fallback
    - rewind
* canthelp
    - fallback: action_default_fallback
    - rewind
* ask_faq_opensource
    - fallback: action_default_fallback
    - rewind
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* affirm
    - fallback: action_default_fallback
    - rewind
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - fallback: action_default_fallback
    - rewind
* enter_data
    - subscribe_fail: action_store_email
    - rewind
* bye
    - fallback: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* deny
    - subscribe_success: utter_cantsignup
* deny
    - chitchat: utter_direct_install
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:faq, id:1b9d609211b74674844d925461b24744, 12/15/18 -4573659050616064820
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_faq_voice
    - faq: action_faqs
* affirm
    - chitchat: utter_thumbsup

## Generated Story goal:1 step, id:fe9205767e5540319511248ba2d7aa7d, 12/15/18 -1169614020695031757
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* enter_data
    - greet_success: action_greet_user

## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - fallback: action_default_fallback
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

## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_chitchat
    - fallback: action_default_fallback
    - rewind
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - fallback: action_default_fallback
    - rewind
* affirm
    - fallback: action_default_fallback
    - rewind

## Generated Story goal:chitchat, id:2721ae89d30d4c28964ac367c2e553ed, 12/15/18 -3646576092582365265
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_time
    - chitchat: action_chitchat
* source_code
    - faq: utter_source_code
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916, 12/15/18 -5644677460292251299
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

## Generated Story goal:1 step, id:8affa7a6082945a09f031db186ec22eb, 12/15/18 -5307346528120334917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_chitchat
    - fallback: action_default_fallback
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* enter_data
    - fallback: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:15f92cc91e4e4c86826ffd023f4d1ef7, 12/15/18 -5922610915225646491
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
* enter_data
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "yes"}
    - getstarted_3: utter_direct_to_forum_for_help

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
    - fallback: action_default_fallback
    - rewind
* handleinsult
    - fallback: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* out_of_scope
    - fallback: action_default_ask_affirmation
* out_of_scope
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: out_of_scope
    - form: feedback_form
    - slot{"feedback_message": "docs"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart

