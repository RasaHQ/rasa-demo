## Generated Story goal:whatspossible, id:804addd312184e3384716589128ae5ad -842626910449672469
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* greet
    - greet: utter_greet
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - getstarted_1: utter_getstarted
    - getstarted_1: utter_first_bot_with_rasa
* mood_confirm
    - getstarted_1/rasa_help: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* mood_confirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* enter_data
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:804addd312184e3384716589128ae5ad -842626910449672469
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* greet
    - greet: utter_greet
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - getstarted_1: utter_getstarted
    - getstarted_1: utter_first_bot_with_rasa
* mood_confirm
    - getstarted_1/rasa_help: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* mood_confirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* enter_data
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:ed59d34c380042c280a9d61003f4c3ad 6362323570205639368
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* ask_whatisrasa
    - chitchat: action_chitchat
    - whatspossible: utter_ask_goal
* enter_data
    - whatspossible: utter_possibilities

## Generated Story goal:oos, id:ed59d34c380042c280a9d61003f4c3ad 6362323570205639368
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* ask_whatisrasa
    - chitchat: action_chitchat
    - whatspossible: utter_ask_goal
* enter_data
    - whatspossible: utter_possibilities

## Generated Story goal:oos, id:3b991ef763054302bc9dc3ec15c7dcfb -9205316803704739657
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* rasa_cost
    - action_default_fallback
    - event_rewind
* rasa_cost
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind

## Generated Story goal:oos, id:ea8fae49656c4b7285d07635e3d8dd99 7867441463491940167
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* greet
    - greet: utter_greet
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* technical_question
    - chitchat: action_chitchat

## Generated Story goal:oos, id:2cdd986e4ced48cf8463552af064a969 -8299759567436188929
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - whatspossible: utter_ask_goal
* ask_whatisrasa
    - chitchat: action_chitchat
    - whatspossible: utter_ask_goal
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* bye
    - chitchat: utter_bye
* out_of_scope
    - oos: utter_out_of_scope
    - whatspossible: utter_possibilities
* mood_confirm
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "quit"}
    - sales: utter_ask_usecase
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "emotional"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": 0}
    - sales: action_store_budget
    - slot{"budget": "0"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "Pepe"}
    - sales: utter_ask_company
* enter_data{"number": 0}
    - sales: action_store_company
    - slot{"company_name": "none"}
    - sales: utter_ask_businessmail
* enter_data{"email": "pepegotera@gmail.com"}
    - slot{"email": "pepegotera@gmail.com"}
    - sales: action_store_email
    - slot{"email": "pepegotera@gmail.com"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* canthelp
    - chitchat: utter_canthelp

## Generated Story goal:oos, id:2cdd986e4ced48cf8463552af064a969 -8299759567436188929
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - greet_success: utter_ask_goal
* ask_whatisrasa
    - chitchat: action_chitchat
    - whatspossible: utter_ask_goal
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* bye
    - chitchat: utter_bye
* out_of_scope
    - oos: utter_out_of_scope
    - whatspossible: utter_possibilities
* mood_confirm
    - whatspossible_fail: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "quit"}
    - sales: utter_ask_usecase
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "emotional"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": 0}
    - sales: action_store_budget
    - slot{"budget": "0"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "Pepe"}
    - sales: utter_ask_company
* enter_data{"number": 0}
    - sales: action_store_company
    - slot{"company_name": "none"}
    - sales: utter_ask_businessmail
* enter_data{"email": "pepegotera@gmail.com"}
    - slot{"email": "pepegotera@gmail.com"}
    - sales: action_store_email
    - slot{"email": "pepegotera@gmail.com"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* canthelp
    - chitchat: utter_canthelp

## Generated Story goal:rasa_help, id:d01be9f6d34c48b3b7df6302d86f1270 -8053849272121101126
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - greet_success: utter_ask_goal
* greet
    - greet: utter_greet
* how_to_get_started
    - getstarted_1: utter_getstarted
    - getstarted_1: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - rasa_help: utter_core_tutorial
    - rasa_help: utter_anything_else
* ask_weather
    - action_default_fallback
    - event_rewind
* out_of_scope
    - oos: utter_out_of_scope
    - whatspossible: utter_possibilities

## Generated Story goal:oos, id:f584c3757e304ed39c22c2d017aaeb09 -5826455714001724980
* greet
    - greet: utter_greet
    - greet: utter_inform_privacypolicy
    - greet_success: utter_ask_goal
* greet
    - greet: utter_greet
* ask_howdoing
    - chitchat: action_chitchat
* greet
    - greet: utter_greet
    - greet_fail: utter_inform_privacypolicy
    - greet_fail: utter_ask_goal
* out_of_scope
    - oos: utter_out_of_scope
    - whatspossible: utter_ask_goal

