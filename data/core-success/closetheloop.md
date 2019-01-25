## story number 1
* greet
    - greet_success: action_greet_user
* out_of_scope
    - oos: utter_out_of_scope
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_store_email
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - sales: action_store_job
    - slot{"job_function": "Product Manager"}
    - sales: utter_ask_usecase
* enter_data    
    - sales: action_store_usecase
    - slot{"use_case": "bots"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - sales: action_store_budget
    - slot{"budget": "100k"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data{"name": "Max Meier"}
    - sales: action_store_name
    - slot{"person_name": "Max Meier"}
    - sales: utter_ask_company
* enter_data{"company": "Allianz"}
    - sales: action_store_company
    - slot{"company_name": "Allianz"}
    - sales: utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"} OR enter_data
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback

## story number 2
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_store_email
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_anything_else

## story number 3
* greet
    - greet_success: action_greet_user
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - sales: utter_ask_jobfunction
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - sales: utter_ask_jobfunction
* enter_data{"jobfunction":"engineer"}
    - sales: action_store_job
    - slot{"job_function": "Product Manager"}
    - sales: utter_ask_usecase
* enter_data    
    - sales: action_store_usecase
    - slot{"use_case": "bots"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - sales: action_store_budget
    - slot{"budget": "100k"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data{"name": "Max Meier"}
    - sales: action_store_name
    - slot{"person_name": "Max Meier"}
    - sales: utter_ask_company
* enter_data{"company": "Allianz"}
    - sales: action_store_company
    - slot{"company_name": "Allianz"}
    - sales: utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback

## story number 4
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_store_email
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* ask_whatspossible
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities

## story number 5
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data
    - subscribe: action_store_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_store_email
    - slot{"email":"hi@rasa.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities

## story number 6
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat

## story number 7
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - sales: action_store_job
    - slot{"job_function": "Product Manager"}
    - sales: utter_ask_usecase
* enter_data    
    - sales: action_store_usecase
    - slot{"use_case": "bots"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - sales: action_store_budget
    - slot{"budget": "100k"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data{"name": "Max Meier"}
    - sales: action_store_name
    - slot{"person_name": "Max Meier"}
    - sales: utter_ask_company
* enter_data{"company": "Allianz"}
    - sales: action_store_company
    - slot{"company_name": "Allianz"}
    - sales: utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback

## story number 8
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## story number 9
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* deny
    - chitchat: utter_nohelp

## story number 11
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup

## story number 12
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - subscribe: action_store_email
    - slot{"email":"test@gmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* enter_data
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## story number 12
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - subscribe: utter_ask_email
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - subscribe: action_store_email
    - slot{"email":"test@gmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* enter_data
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## story number 13
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - subscribe: utter_ask_email
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - subscribe: action_store_email
    - slot{"email":"test@gmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed":true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## story number 14
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat

## story number 15
* greet
    - greet_success: action_greet_user
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## story number 16
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## story number 17
* greet
    - greet_success: action_greet_user
* deny
    - chitchat: utter_nohelp
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat

## story number 18
* greet
    - greet_success: action_greet_user
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* deny
    - chitchat: utter_nohelp
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* deny
    - chitchat: utter_nohelp
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* enter_data{"number":5}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 00e7815f79e4413abb0dfb4b392f1099 on November 15th 2018
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa


# story from linda
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with dfbb633d10854f97b880a2496d632f0d on November 16th 2018
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa


## Story from conversation with alan on November 16th 2018
* nlu_info{"nlu_part":"duckling"}
    - slot{"nlu_part":"duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help

## Story from conversation with alan on November 16th 2018 2
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy":true}
    - rasa_help_success: utter_spacy_or_tensorflow
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa


## Story from conversation with linda on November 15th 2018
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with 477ddbe73e374eedb07104c5d9f42c31 on November 16th 2018
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* greet
    - greet_success: action_greet_user

## Story from conversation with d75d1ac725164b3c976193eb54feb756 on November 19th 2018
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding":false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else
* how_to_get_started{"product":"nlu"}
    - rasa_help: utter_ask_for_nlu_specifics

## Story from conversation with 4986d88ccb784dc19dc5a553a8e07890 on November 19th 2018
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
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - getstarted_1: utter_explain_nlu


## Story from conversation with 7830abb04e1c49809d89b0d420443928 on November 19th 2018
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started{"product":"nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with 29d264d8ce574a11bde572f0e79b73f3 on November 19th 2018
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_isbot
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup

## Story from conversation with 6fd65c93e374489f9c8d76697ab9c493 on November 19th 2018
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup

## Story from conversation with 35d1ecc91c364cbf8a6edf006e5d8c9a on November 19th 2018

* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function":"test"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case":"test"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data
    - sales: action_store_budget
    - slot{"budget":"not sure yet"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name":"akela"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name":"muster"}
    - sales: utter_ask_businessmail
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - sales: action_store_email
    - slot{"email":"test@gmail.com"}
    - sales: action_store_sales_info
    - slot{"data_stored":true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* deny
    - chitchat: utter_nohelp
* affirm
    - chitchat: utter_thumbsup

## Story from conversation with 4c274f8d470e4b77adbfefe7cda7cad7 on October 27th 2018

* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* affirm
    - chitchat: utter_thumbsup
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with d041ba4b0a89479e9bb6a5007f2cdc87 on November 15th 2018
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function":"repair ac"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case":"for some eamples"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"amount-of-money":1}
    - sales: action_store_budget
    - slot{"budget":1}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name":"xijinping"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name":"USA."}
    - sales: utter_ask_businessmail
* enter_data{"email":"abc@163.com"}
    - slot{"email":"abc@163.com"}
    - sales: action_store_email
    - slot{"email":"abc@163.com"}
    - sales: action_store_sales_info
    - slot{"data_stored":true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with dominik on November 19th 2018
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api":"luis"}
    - slot{"current_api":"luis"}
    - getstarted_1_success: utter_switch_luis
    - chitchat: utter_anything_else
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - getstarted_1: utter_explain_core
    - chitchat: utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - getstarted_1: utter_explain_nlu
    - chitchat: utter_anything_else

## Story from conversation with dominik
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy":true}
    - rasa_help_success: utter_spacy_or_tensorflow
    - chitchat: utter_anything_else
* enter_data{"language":"french"}
    - slot{"language":"spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy":true}
    - rasa_help_success: utter_spacy_or_tensorflow
    - chitchat: utter_anything_else

## Story from conversation with dominik on November 19th 2018
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding":false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - rasa_help: utter_ask_for_nlu_specifics

## Story from conversation with 201bb55841154f858f524a485f8816c3 on November 18th 2018

* greet
    - greet_success: action_greet_user
* how_to_get_started{"product":"nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with cd483ab3456d47dfb40bd1f51043fb54 on November 18th 2018

* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* how_to_get_started{"product":"core"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with d75d1ac725164b3c976193eb54feb756 on November 19th 2018

* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding":false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics

## Story from conversation with 7830abb04e1c49809d89b0d420443928 on November 19th 2018
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started{"product":"nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Story from conversation with cfa8bb9deaf0427498c662745431a282 on December 15th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with cdd14d763a664a5b95e998ce165bd86f on December 16th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"stack"}
    - slot{"product":"stack"}
    - getstarted_1_success: utter_quickstart
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 15f92cc91e4e4c86826ffd023f4d1ef7 on December 16th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Story from conversation with 030829eb30ed4339985d7e71737f6c2d on January 1st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* enter_data
    - chitchat: utter_not_sure
    - getstarted_1: utter_tryout

## Story from conversation with e977c395a2404bef8ba7f0c3b7e65970 on January 8th 2019

* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"stack"}
    - slot{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## Story from conversation with 602ddccbe2de4f46822e06e2781cf02d on January 8th 2019

* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* greet
    - greet_success: action_greet_user
* out_of_scope
    - oos: utter_out_of_scope
* affirm
    - chitchat: utter_thumbsup
* affirm
    - chitchat: utter_thumbsup

## Story from conversation with 03727bb9d4cb4f64afdc383818739680 on January 17th 2019

* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - greet_success: action_greet_user
* how_to_get_started{"user_type":"new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product":"stack"}
    - slot{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step":"3"}
* install_rasa
    - getstarted_3: utter_ask_python_installed


## Story from conversation with 4cdb0b3c6f6c4b3694fcb311ae72743b on January 21st 2019

* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu


## Story from conversation with 4b7ecc2cab6e42c5b1fedb8ab4056866 on December 29th 2018
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* ask_whoami
    - chitchat: action_chitchat
* ask_languagesbot
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* out_of_scope{"number":42}
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* out_of_scope{"number":42}
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities


## Story from conversation with af5a6b3c39d04c6db2b682960e63f01c on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* react_positive
    - chitchat: utter_react_positive
* enter_data{"jobfunction":"dancer"}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## Story from conversation with 53d4ca53494d4469b7d94aca2f7b3fec on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu{"product":"nlu"}
    - slot{"product":"nlu"}
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu


## Story from conversation with 4a4e903fc43940db9ccdb9153dfdadcb on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager":"pip"}
    - slot{"package_manager":"pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description":"tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible."}
    - getstarted_3_success: utter_direct_to_forum_for_help
    - getstarted_3_success: utter_direct_to_step4
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## Story from conversation with 5f3a2ea92d184a9f96df7240e4f7e2d9 on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## Story from conversation with ced8c1eb9a8d485f88a02d931b2879bd on January 16th 2019
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy":true}
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding":true}
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
* affirm
    - getstarted_1_success: utter_quickstart
