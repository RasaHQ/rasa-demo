## Generated Story goal:getstarted, id:804addd312184e3384716589128ae5ad 7225286321375551559
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* enter_data
    - utter_direct_install
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:ed59d34c380042c280a9d61003f4c3ad 1539688714909474049
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:oos, id:ed59d34c380042c280a9d61003f4c3ad 1539688714909474049
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:oos, id:2cdd986e4ced48cf8463552af064a969 8640731090527813058
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_default_fallback
    - rewind
* bye
    - utter_bye
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "quit"}
    - utter_ask_usecase
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_store_usecase
    - slot{"use_case": "emotional"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Pepe"}
    - utter_ask_company
* enter_data{"number": 0}
    - action_store_company
    - slot{"company_name": "none"}
    - utter_ask_businessmail
* enter_data{"email": "pepegotera@gmail.com"}
    - slot{"email": "pepegotera@gmail.com"}
    - action_store_email
    - slot{"email": "pepegotera@gmail.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* canthelp
    - utter_canthelp
    - success

## Generated Story goal:rasa_help, id:d01be9f6d34c48b3b7df6302d86f1270 -3911298519625388677
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* ask_weather
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - success

## Generated Story goal:chitchat, id:939b1248d0094ded82f7c0b8e62b06fa -2258547822299641125
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - success

## Generated Story goal:rasa_help, id:3f1b14835d9d4855bccffd6aed2778b6 -6609615338485643827
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:e6fa071ff0e94499b4a7bac0edd18227 -1135811984055669407
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whoisit
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:1140ececf0ec473180799dd4d598672d -6391045995910006908
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* None
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data{"number": 1}
    - utter_direct_install
    - utter_anything_else
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* ask_whoisit
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* ask_isbot
    - action_chitchat
* enter_data
    - utter_possibilities
* technical_question
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* out_of_scope{"language": "french"}
    - slot{"language": "french"}
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* thank
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "vincediegane@gmail.com"}
    - slot{"email": "vincediegane@gmail.com"}
    - action_store_email
    - slot{"email": "vincediegane@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:rasa_help, id:3cf5435672ce4dfa95875f35a3d1df01 -3253988521985148575
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* nlu_info{"nlu_part": "entity extraction"}
    - slot{"nlu_part": "entity extraction"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
    - success

## Generated Story goal:whatspossible, id:8760964ea2ac4cd9bb6bb84a3c561db0 483786942898621087
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_chitchat
    - success

## Generated Story goal:subscribe, id:6422344c4803405494dc6c17e07b58d6 -8952212793634298420
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "filippo.minutella@youtilitycenter.it"}
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
    - action_store_email
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:6422344c4803405494dc6c17e07b58d6 -8952212793634298420
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "filippo.minutella@youtilitycenter.it"}
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
    - action_store_email
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:rasa_help, id:b292c360fac9429f8a621a8e95ba411c 2875278033518753373
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:ad5fb80204444eaa8a2bca3ac0c4183b 5787120610023818368
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whatspossible
    - action_chitchat
* technical_question
    - utter_nohelp
* technical_question
    - utter_possibilities
* technical_question
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else
    - success

## Generated Story goal:oos, id:93adb050946d4efda4d9d4eb9dc0027e 589496224787742298
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:ef1eafd9a1b04caa8782be82351ce33f -8550015207896305719
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* ask_whatspossible
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* thank
    - utter_noworries
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* enter_data
    - action_default_fallback
    - rewind
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* thank
    - utter_noworries
    - success

## Generated Story goal:rasa_help, id:0361e0c5e7f0431390c445454e9b837b 4501655518422960224
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classificaton"}
    - slot{"nlu_part": "intent classificaton"}
    - action_default_fallback
    - rewind
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:0f8813a190904078aa2cff1b7faa1e69 2483633972736899851
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_builder
    - action_chitchat
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch
    - action_store_unknown_product
    - slot{"unknown_product": "wit"}
    - utter_no_guide_for_switch
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:b38efbb91d3745fea37234277008fbd8 -8826923805113198293
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "virtual assistant"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 2}
    - action_store_budget
    - slot{"budget": 2}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Thorin"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Gandalfs company"}
    - utter_ask_businessmail
* enter_data{"email": "thorin@thorin.thorin.com"}
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_email
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:b38efbb91d3745fea37234277008fbd8 -8826923805113198293
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "virtual assistant"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 2}
    - action_store_budget
    - slot{"budget": 2}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Thorin"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Gandalfs company"}
    - utter_ask_businessmail
* enter_data{"email": "thorin@thorin.thorin.com"}
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_email
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:sales, id:b38efbb91d3745fea37234277008fbd8 -8826923805113198293
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "virtual assistant"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 2}
    - action_store_budget
    - slot{"budget": 2}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Thorin"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Gandalfs company"}
    - utter_ask_businessmail
* enter_data{"email": "thorin@thorin.thorin.com"}
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_email
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:chitchat, id:3985f7d893004d1aab3e5c72bdb6a68b 334613795968968615
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_builder
    - action_chitchat
* enter_data
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
    - success

## Generated Story goal:chitchat, id:4c56a6ff9c144aeb8f4d04053c31fb61 6263519605744000400
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:182ec26caec44bc1a5599afc4b899ba3 9195754664139970630
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "IBM watson"}
    - utter_no_guide_for_switch
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:7a7ef07424ac47ba83204cea50301ac7 8453052113926331374
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope{"language": "german"}
    - slot{"language": "german"}
    - utter_out_of_scope
    - utter_possibilities
* mood_confirm
    - utter_thumbsup
* ask_howdoing
    - action_chitchat
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:3056d16b1ef34735b867f0eb00da5a9e 3333718755217779700
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:03aec288fb8344dd9a6aa47d37af2e6d -9063334716126405558
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* enter_data
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:01b872dd65de4a86870be245dae0984c -4008979391761926606
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* ask_whatisrasa
    - action_chitchat
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:1fbc61697e0f4a149b6ff4a0fac4b64e 7076594325776430566
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:f741a37bd7454c07b48f79b07fec7ee3 -4236025117026757684
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whoisit
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_whatisrasa
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:2ac693732f3b4df492bf2ad72fea841d 7282290640424792666
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:3abd72781f064597bd667ca29705cece 6083257048931294483
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:chitchat, id:0b11a4b888994b4da9d251b36f566891 3462687184217837229
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
    - success

## Generated Story goal:chitchat, id:1928185e25494fb99edeead9e06b05e7 6036044543496284776
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_builder
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* Where can I integrate my bot
    - utter_nohelp
    - success

## Generated Story goal:chitchat, id:7ca7d2ae7abf47eaabbf4803b1df056d -5427746582461269099
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:87619e690d10457c932eba08f9ebf602 -588461147343309013
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:5f458669c6e04aa8b2f4e52cf81cffa1 -1510198585533270087
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:f6555b569bbb4a55a6edd7bc7f817a12 3975634412653776848
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
    - success

## Generated Story goal:oos, id:5ff63ec81980449fb652755cbf49c4d8 5046878220283547866
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:oos, id:3a75bcd065574a5bbd353e4fb2b49124 589496224787742298
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:chitchat, id:6062991312dc4f6292f78fdfc3f7a950 8663105657729884026
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
    - success

## Generated Story goal:rasa_help, id:1da93d6da09045f189563b672c2fc619 -5906049002399271335
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
    - success

## Generated Story goal:sales, id:35d1ecc91c364cbf8a6edf006e5d8c9a 2131324275632008970
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* out_of_scope
    - action_default_fallback
    - rewind
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* switch
    - action_default_fallback
    - rewind
* enter_data
    - action_store_job
    - slot{"job_function": "business anaylst"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "customer service chatbot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data
    - action_store_budget
    - slot{"budget": "not sure yet"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "april"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "boa financial group"}
    - utter_ask_businessmail
* enter_data{"email": "april.xiao@boafinancialgroup.com"}
    - slot{"email": "april.xiao@boafinancialgroup.com"}
    - action_store_email
    - slot{"email": "april.xiao@boafinancialgroup.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* deny
    - utter_nohelp
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_store_job
    - slot{"job_function": "introduce rasa service"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "digital banking chatbot"}
    - utter_thank_usecase
    - utter_ask_budget
* greet
    - utter_greet
    - utter_thank_usecase
    - utter_ask_budget
    - success

## Generated Story goal:getstarted, id:7830abb04e1c49809d89b0d420443928 8103804079007693517
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:oos, id:98b2bbce810744898967abad1e06586b 8865060135960159147
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - success

## Generated Story goal:oos, id:bb471d635a4f421d8f1b09fda79ed38a 5320536250699714119
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* technical_question
    - action_chitchat
* enter_data
    - utter_possibilities
* technical_question
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:49bbf948433247c784fe2ed199f7c931 -6822057689937111858
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data
    - utter_direct_install
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:5b72515d7e584a17aac1ca10eb53214b 2164085748464922413
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:c28fd8cf8e3c4bb89fd79922e74ddc6d 4726379811329892019
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - action_set_onboarding
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* enter_data
    - action_subscribe_newsletter
    - action_subscribe_newsletter
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:oos, id:10899e9317df4fa6aaaf1a64e7af8eff 589496224787742298
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:whatspossible, id:170ff96b03fe4624999fab5045f6f301 -5926831148837034674
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* ask_whatisrasa
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
    - success

## Generated Story goal:getstarted, id:a3c62ec26bd84b46adf61078d9b7e01f 606750322048733708
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - success

## Generated Story goal:getstarted, id:b33184c82c4b49e8bc52e5b141654865 -2426218508657778534
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_direct_install
    - utter_anything_else
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:bffb69a4cadf4a869cce7f5dc6697c18 7088543905590691654
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "watson"}
    - utter_no_guide_for_switch
    - utter_anything_else
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:oos, id:7065c97d8eb142a4bdcf75700a1efedd 6030260346461153495
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* technical_question
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:dd97568cca7047a8bb99be9f041b82bd 8922594620458208000
* suggestions
    - action_chitchat
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:oos, id:0030c323526f4ac8959c9f0b1ba172da 2458325671898431597
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - success

## Generated Story goal:getstarted, id:50ad2b993b10423d9ddd29c8be88ab29 -8163866633515756993
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:oos, id:4f765fe1222342bc9c01d49f90ff661d -5949688589066428290
* suggestions
    - action_chitchat
* mood_confirm
    - action_default_fallback
    - rewind
* None
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:bf26e70697f04378920c63969626983b -950120035011271909
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:3f91ca8a9a19474896f4adab215b57cb 3002101841828049418
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* enter_data
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:chitchat, id:0f25fc18fdd14ba586e9742db54eba50 -3440726117034561031
* ask_whoisit
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:4dfd10b7c4de4b7285af501e70713d81 6032599555972573384
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* deny
    - utter_thumbsup
    - success

## Generated Story goal:oos, id:76a9e7e2fbff4c75a7f1921a21b6b4a7 -742313344129651293
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:chitchat, id:91608afa94584dd4974d13be7f54b227 8066559326634917526
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_isbot
    - action_chitchat
    - utter_ask_goal
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:d0895ef800074d4789bd068717e10e9c -3632685140551545497
* ask_whoisit
    - action_chitchat
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:6afa2fd339334781bc97175ee2b05193 6748218506133865554
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* bye
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:8350a9684ee14756a5ad58eb04c7b689 3964150509455257122
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet{"name": "Hello Sara"}
    - utter_greet
* bye
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - success

## Generated Story goal:getstarted, id:2bf3e50bb96d48c3a6ff8b35e6a40ab4 809757456182353991
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* enter_data{"name": "Iam Jorge"}
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:9028a7bef4174c948ecb8de636be45af -9066548740019796988
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* thank
    - utter_noworries
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:41972a8ea1c4401e8a765d481763157d -7368167987920860439
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:7a1c1b5c0cb444c29f73b01d0b8c06a4 9091758904003219508
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data{"number": 0}
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* thank
    - utter_noworries
    - success

## Generated Story goal:rasa_help, id:2e4860de8f5d456e8ff73e4e4703e72b -9145227217484997087
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_thumbsup
    - utter_anything_else
* bye
    - utter_bye
* deny
    - utter_nohelp
    - success

## Generated Story goal:oos, id:fe0935087493480b948541185df15e51 -2815956840822792172
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_default_fallback
    - rewind
* technical_question
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* out_of_scope
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* technical_question
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:ab03e7289b9a44d099bce53798de9fe5 441847645207684396
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:a6b68460fd2e486ca17afdfb7356cd2f -6974982680890971993
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_default_fallback
    - rewind
* greet
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
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
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_direct_install
    - utter_anything_else
* greet
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:2a688257f572484eaf03df69d53fd9ef 2885280474659434668
* ask_isbot
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:94c1d05a42fa432fb71326bbffe8c50b 8049130048445434917
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "Dialogflow"}
    - slot{"current_api": "Dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:4ead4fe5fce941f49803825fe87cd922 6128142241568278816
* out_of_scope
    - action_default_fallback
    - rewind
* ask_whoisit{"jobfunction": "development"}
    - action_default_fallback
    - rewind
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:oos, id:3b991ef763054302bc9dc3ec15c7dcfb -618499479152484587
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - rewind
* rasa_cost
    - action_default_fallback
    - rewind
* rasa_cost
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:oos, id:ea8fae49656c4b7285d07635e3d8dd99 7059872869062776159
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_chitchat
    - fail

## Generated Story goal:oos, id:2cdd986e4ced48cf8463552af064a969 8640731090527813058
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_default_fallback
    - rewind
* bye
    - utter_bye
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "quit"}
    - utter_ask_usecase
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_store_usecase
    - slot{"use_case": "emotional"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Pepe"}
    - utter_ask_company
* enter_data{"number": 0}
    - action_store_company
    - slot{"company_name": "none"}
    - utter_ask_businessmail
* enter_data{"email": "pepegotera@gmail.com"}
    - slot{"email": "pepegotera@gmail.com"}
    - action_store_email
    - slot{"email": "pepegotera@gmail.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* canthelp
    - utter_canthelp
    - fail

## Generated Story goal:oos, id:f584c3757e304ed39c22c2d017aaeb09 2265865725916857143
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
    - fail

## Generated Story goal:rasa_help, id:7896c27f41274e62a6bca12dd2b02549 -1758998831618183292
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_core_tutorial
    - utter_anything_else
* ask_whatspossible{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - rewind
* out_of_scope{"product": "Core"}
    - slot{"product": "Core"}
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* out_of_scope
    - utter_thumbsup
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_core_tutorial
    - utter_anything_else
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - fail

## Generated Story goal:chitchat, id:30ca43db2c4349f69fa05936f07cf765 6466510726889279143
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* enter_data
    - action_default_fallback
    - rewind
* ask_builder
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_chitchat
    - fail

## Generated Story goal:oos, id:ad5fb80204444eaa8a2bca3ac0c4183b 5787120610023818368
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whatspossible
    - action_chitchat
* technical_question
    - utter_nohelp
* technical_question
    - utter_possibilities
* technical_question
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:oos, id:0c0346511d1346a8a64de9dbcb3bfa26 5299370479075321965
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* human_handoff
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - fail

## Generated Story goal:oos, id:ab9a433900594a55a10f44ad4bd33804 -5707355073661577703
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - fail

## Generated Story goal:chitchat, id:8cd30655583b4dc49ec795de9f0d9467 4897423373890041472
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
    - fail

## Generated Story goal:sales, id:6be442be8aec491d9d81115e9a32a89e -8121675236966542993
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "i aam aprogrammer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "BOT for my product information"}
    - utter_thank_usecase
    - utter_ask_budget
    - fail

## Generated Story goal:getstarted, id:f905fe9c8bc2472286d888a3d2bc2e99 4115093303662244698
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
    - fail

## Generated Story goal:oos, id:849fb835c5334776b5f08fe75e623961 -1872432412433415942
* enter_data
    - utter_thumbsup
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_howdoing
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:oos, id:ef1eafd9a1b04caa8782be82351ce33f -8550015207896305719
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* ask_whatspossible
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* thank
    - utter_noworries
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* enter_data
    - action_default_fallback
    - rewind
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* thank
    - utter_noworries
    - fail

## Generated Story goal:rasa_help, id:ccac7784eaf5418da2e3e384d0ec013a 7702782871487932676
* ask_whatspossible
    - action_chitchat
* technical_question
    - action_chitchat
    - fail

## Generated Story goal:getstarted, id:02094ca453f647e686d26181b4d03f4f 285835436521501832
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* technical_question
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:rasa_help, id:9ab81c4376c64922b9750bb4e6c56136 1185020935027716568
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* ask_whatspossible
    - action_chitchat
* ask_whatisrasa
    - action_default_fallback
    - rewind
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else
* technical_question
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_what_help
* mood_confirm
    - utter_what_help
* ask_weather
    - utter_what_help
* how_to_get_started
    - utter_what_help
* restart
    - action_restart
    - restart
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* technical_question{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* thank
    - utter_noworries
    - fail

## Generated Story goal:getstarted, id:bdda478467ce482190d6703d27ea2d53 8810074103022150505
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
    - fail

## Generated Story goal:oos, id:0f8813a190904078aa2cff1b7faa1e69 2483633972736899851
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_builder
    - action_chitchat
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch
    - action_store_unknown_product
    - slot{"unknown_product": "wit"}
    - utter_no_guide_for_switch
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:rasa_help, id:0d98218a201448089f3ef268486b5ccb -3489188094204184993
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else
* ask_builder
    - action_chitchat
* None
    - action_default_fallback
    - rewind
* enter_data{"language": "italian"}
    - slot{"language": "italian"}
    - action_store_usecase
    - slot{"use_case": "my bot can be in italian?"}
    - utter_thank_usecase
    - utter_ask_budget
    - fail

## Generated Story goal:getstarted, id:131b0646a27e4cf6aab2a86c5619b023 1957186685348396238
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* technical_question
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_howdoing
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:1246edc0c1384ad59b1554da3bbcf56d -3079800542573812286
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:6b5d9883a3cf4f8ba1817bf884e2e108 6460683172762636038
* enter_data
    - utter_thumbsup
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - fail

## Generated Story goal:oos, id:bf63d3a454534a8a88243fffb2678dd2 -2802179231585225610
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:chitchat, id:01b872dd65de4a86870be245dae0984c -4008979391761926606
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* ask_whatisrasa
    - action_chitchat
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:oos, id:01b872dd65de4a86870be245dae0984c -4008979391761926606
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* ask_whatisrasa
    - action_chitchat
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:9320945deed5459090e9971640365359 7225300078731012991
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* mood_confirm
    - utter_thumbsup
* enter_data
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:oos, id:216f35cf3e894c0bb13172f51b50dad4 6339986528410007685
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* technical_question
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:216f35cf3e894c0bb13172f51b50dad4 6339986528410007685
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* technical_question
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:chitchat, id:7f483a46919741c2bfdf7735c7b8fb1f 1990724930952607231
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* ask_whoisit
    - action_chitchat
* ask_whoisit
    - action_chitchat
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* technical_question
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
    - fail

## Generated Story goal:rasa_help, id:d75d1ac725164b3c976193eb54feb756 -2399396674828011007
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_nohelp
* bye
    - utter_bye
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - fail

## Generated Story goal:oos, id:fdcf9815d22040edbaf815762d312f1d -1269878816863735352
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_thumbsup
* out_of_scope
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:4986d88ccb784dc19dc5a553a8e07890 -7138330429390946500
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* deny
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:chitchat, id:29d264d8ce574a11bde572f0e79b73f3 4954335053140477032
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_isbot
    - action_chitchat
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "I am working as data scientist in kryptoblocks."}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "legal bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 1}
    - action_store_budget
    - slot{"budget": 1}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "kunal"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "we want to create speech bot"}
    - utter_ask_businessmail
    - fail

## Generated Story goal:chitchat, id:6fd65c93e374489f9c8d76697ab9c493 -6073101316338642065
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "nothing"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "chatbot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data
    - action_store_budget
    - slot{"budget": "nothing"}
    - utter_sales_contact
    - utter_ask_name
* ask_whoisit
    - action_chitchat
    - utter_ask_name
* deny
    - utter_direct_install
    - utter_anything_else
* enter_data
    - action_store_name
    - slot{"person_name": "nothing"}
    - utter_ask_company
* ask_whatisrasa
    - action_chitchat
    - utter_ask_company
* greet
    - action_store_company
    - slot{"company_name": "/greet"}
    - utter_ask_businessmail
    - fail

## Generated Story goal:chitchat, id:ceca8bb3def548f7800bd0b5fbb8b393 -2292470215387247775
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* thank
    - utter_noworries
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:oos, id:ee9402011d6a48fa9947eb85c39f4107 5778630178365581687
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
    - fail

## Generated Story goal:getstarted, id:ec346070b4734e00af295571f55837f7 3937001759518359192
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
    - fail

## Generated Story goal:oos, id:3edca807cef74408a624fb07ec5484cb 5441756646286714908
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* enter_data{"number": 600}
    - utter_thumbsup
    - fail

## Generated Story goal:chitchat, id:8a9679faae194de59a62d7131d1e90c4 356060911250884605
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_howdoing
    - action_chitchat
    - fail

## Generated Story goal:oos, id:35d1ecc91c364cbf8a6edf006e5d8c9a 2131324275632008970
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* out_of_scope
    - action_default_fallback
    - rewind
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* switch
    - action_default_fallback
    - rewind
* enter_data
    - action_store_job
    - slot{"job_function": "business anaylst"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "customer service chatbot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data
    - action_store_budget
    - slot{"budget": "not sure yet"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "april"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "boa financial group"}
    - utter_ask_businessmail
* enter_data{"email": "april.xiao@boafinancialgroup.com"}
    - slot{"email": "april.xiao@boafinancialgroup.com"}
    - action_store_email
    - slot{"email": "april.xiao@boafinancialgroup.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* deny
    - utter_nohelp
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_store_job
    - slot{"job_function": "introduce rasa service"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "digital banking chatbot"}
    - utter_thank_usecase
    - utter_ask_budget
* greet
    - utter_greet
    - utter_thank_usecase
    - utter_ask_budget
    - fail

## Generated Story goal:rasa_help, id:7830abb04e1c49809d89b0d420443928 8103804079007693517
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - fail

## Generated Story goal:chitchat, id:0f607b0ce1124067bb26fa3caff67e98 -7316900351940470654
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_isbot
    - action_chitchat
* enter_data
    - utter_possibilities
* bye
    - utter_bye
    - fail

## Generated Story goal:oos, id:c28fd8cf8e3c4bb89fd79922e74ddc6d 4726379811329892019
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - action_set_onboarding
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* enter_data
    - action_subscribe_newsletter
    - action_subscribe_newsletter
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
    - fail

## Generated Story goal:chitchat, id:c686bff9816e488ca45091afef5a83c7 -3557599662584248562
* ask_howdoing
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_chitchat
* bye
    - action_default_fallback
    - rewind
* ask_isbot
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:oos, id:0788b56853954840a55b8ee50e9b0b30 3093386586136361172
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* pipeline_recommendation
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
    - fail

## Generated Story goal:oos, id:9a5db7fa05e0493ba42ecb482a25f14c -2542044341560133338
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - fail

## Generated Story goal:getstarted, id:892498320d384a78aed6696f6e67a538 2758406977396380019
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - fail

## Generated Story goal:rasa_help, id:ba00f9a581f645fca89561ebf4a161a9 -4928493418355746146
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:fd0058985c3e45c4bf4aa94c997407ca -5959243819871802887
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* enter_data
    - utter_possibilities
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* human_handoff
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"number": 1}
    - utter_possibilities
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* bye
    - utter_bye
* enter_data
    - utter_possibilities
    - fail

## Generated Story goal:getstarted, id:e900e06d633e47c3b831f23425cd7d83 8536078750217323562
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
    - fail

## Generated Story goal:rasa_help, id:e178360c6e4e41cda03971ca618cb1c9 992691340439015578
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_core_tutorial
    - utter_anything_else
* out_of_scope
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:ad53b51192aa4bef8954393678d413a2 -5436498510117694639
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:d2b672f04dca45fdbed1ad627b5b3f49 7460061025584704171
* suggestions
    - action_chitchat
* ask_whatspossible
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:0f885021e48448f0a467b3addf5f6e78 428447117903737460
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* canthelp
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:21eb481b1e5742839fcd14967856e7d4 -6585149076198522394
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
    - fail

## Generated Story goal:getstarted, id:1d3f0ed42700470c92551c307a4bee3a 3322080963775725146
* ask_whoisit
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data
    - utter_direct_install
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:ac171abfe26347819d63e32761822f28 1003567858497349197
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started
    - utter_quickstart_nlu_only
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data{"number": 1}
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:04f11e5aef73408191a373cc370e6654 6997791890647313420
* suggestions
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_isbot
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:dcf5fd070ce44d8dad16adef14991aaf -1174805203229697062
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
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
    - utter_explain_nlu
    - utter_tryout
* greet
    - utter_quickstart
    - utter_anything_else
    - fail

## Generated Story goal:oos, id:6090ea051b714fc0897e5439d87facf4 -5761115022801837255
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* rasa_cost
    - action_default_fallback
    - rewind
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* ask_whatisrasa
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:oos, id:3c6ac2a24df24d1ba1455b22716e075e -3506526688795099184
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
    - fail

## Generated Story goal:oos, id:d03c901e9bb641c8b8277f291e75f8a6 -6990948437368887072
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:oos, id:6d9e6525e7e34a08b8f54aab13a10c22 6092953823859516393
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data{"jobfunction": "dialogue manager"}
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
    - fail

## Generated Story goal:getstarted, id:3af5aad1b1dd487fbba6bf84499c157c 1082174467868192642
* out_of_scope
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* enter_data
    - utter_direct_install
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:485b1dc8843140eb9ac7de845410dd3c -5237910970854027829
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
    - fail

## Generated Story goal:oos, id:fcc95f2d77dc4bc6bc4b1b5510d9b6b6 -1552103265204230301
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* technical_question
    - action_default_fallback
    - rewind
* greet
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - fail

## Generated Story goal:rasa_help, id:0f76d93827034065bbaaedceb5c0d1e3 1739785111023580194
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:b294305abf414f43bf95c259376bc20e -5106287164487535265
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_great
    - utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:rasa_help, id:1cf3c07a9c2940cf8d58115496ae491d 5625141441669248657
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* mood_confirm
    - utter_thumbsup
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
    - fail

## Generated Story goal:getstarted, id:4114e7e201264ebdbb8e2587aedc88b9 7985448692066050345
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_whatspossible
    - action_chitchat
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "LUIS"}
    - slot{"current_api": "LUIS"}
    - utter_switch_luis
    - utter_anything_else
* technical_question{"number": 2}
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:11ff91e7d8ad4958b776947f5ef028e1 -6877918746206397770
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* rasa_cost
    - action_default_fallback
    - rewind
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
    - fail

