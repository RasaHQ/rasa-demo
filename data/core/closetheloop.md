## story number 1
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - action_store_email
    - slot{"email":"hi@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"job_function": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"person_name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company_name": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"} OR enter_data
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback

## story number 2
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - action_store_email
    - slot{"email":"hi@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* out_of_scope
    - utter_thumbsup
    - utter_anything_else

## story number 3
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* enter_data{"jobfunction":"engineer"}
    - action_store_job
    - slot{"job_function": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"person_name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company_name": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback

## story number 4
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - action_store_email
    - slot{"email":"hi@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 5
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data
    - action_store_email
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - action_store_email
    - slot{"email":"hi@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 6
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## story number 7
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"job_function": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"person_name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company_name": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback

## story number 8
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## story number 9
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* deny
    - utter_nohelp

## story number 11
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* deny
    - utter_cantsignup

## story number 12
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - action_store_email
    - slot{"email":"test@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## story number 12
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_email
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - action_store_email
    - slot{"email":"test@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## story number 14
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat

## story number 15
* greet
    - action_greet_user
* ask_weather
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## story number 17
* greet
    - action_greet_user
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## story number 18
* greet
    - action_greet_user
* ask_weather
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp
* enter_data
    - utter_not_sure
    - utter_possibilities
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"number":5}
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 00e7815f79e4413abb0dfb4b392f1099 on November 15th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa


# story from linda
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with dfbb633d10854f97b880a2496d632f0d on November 16th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa


## Story from conversation with alan on November 16th 2018
* nlu_info{"nlu_part":"duckling"}
    - slot{"nlu_part":"duckling"}
    - utter_duckling_info
    - utter_anything_else
* affirm
    - utter_what_help

## Story from conversation with alan on November 16th 2018 2
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* affirm
    - utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa


## Story from conversation with linda on November 15th 2018
* greet
    - action_greet_user
* ask_whatisrasa
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with 477ddbe73e374eedb07104c5d9f42c31 on November 16th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - action_greet_user

## Story from conversation with 4986d88ccb784dc19dc5a553a8e07890 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_direct_to_step2


## Story from conversation with 7830abb04e1c49809d89b0d420443928 on November 19th 2018
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product":"nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with 29d264d8ce574a11bde572f0e79b73f3 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_isbot
    - action_chitchat
* affirm
    - utter_thumbsup

## Story from conversation with 6fd65c93e374489f9c8d76697ab9c493 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* affirm
    - utter_thumbsup

## Story from conversation with 35d1ecc91c364cbf8a6edf006e5d8c9a on November 19th 2018

* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function":"test"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case":"test"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data
    - action_store_budget
    - slot{"budget":"not sure yet"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name":"akela"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name":"muster"}
    - utter_ask_businessmail
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - action_store_email
    - slot{"email":"test@gmail.com"}
    - action_store_sales_info
    - slot{"data_stored":true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else
* affirm
    - utter_thumbsup

## Story from conversation with 4c274f8d470e4b77adbfefe7cda7cad7 on October 27th 2018

* greet
    - action_greet_user
* greet
    - action_greet_user
* affirm
    - utter_thumbsup
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with d041ba4b0a89479e9bb6a5007f2cdc87 on November 15th 2018
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function":"repair ac"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case":"for some eamples"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money":1}
    - action_store_budget
    - slot{"budget":1}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name":"xijinping"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name":"USA."}
    - utter_ask_businessmail
* enter_data{"email":"abc@163.com"}
    - slot{"email":"abc@163.com"}
    - action_store_email
    - slot{"email":"abc@163.com"}
    - action_store_sales_info
    - slot{"data_stored":true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else
* ask_weather
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with dominik on November 19th 2018
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
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api":"luis"}
    - slot{"current_api":"luis"}
    - utter_switch_luis
    - utter_anything_else
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - utter_explain_nlu
    - utter_anything_else

## Story from conversation with dominik
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* affirm
    - utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data{"language":"french"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## Story from conversation with dominik on November 19th 2018
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding":false}
    - utter_ask_which_product
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - utter_ask_for_nlu_specifics

## Story from conversation with 201bb55841154f858f524a485f8816c3 on November 18th 2018

* greet
    - action_greet_user
* how_to_get_started{"product":"nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with cd483ab3456d47dfb40bd1f51043fb54 on November 18th 2018

* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started{"product":"core"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with cfa8bb9deaf0427498c662745431a282 on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_whatisrasa
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with cdd14d763a664a5b95e998ce165bd86f on December 16th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_faq_languages
    - action_faqs
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_faq_languages
    - action_faqs
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 030829eb30ed4339985d7e71737f6c2d on January 1st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with e977c395a2404bef8ba7f0c3b7e65970 on January 8th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## Story from conversation with 602ddccbe2de4f46822e06e2781cf02d on January 8th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* affirm
    - utter_thumbsup
* affirm
    - utter_thumbsup

## Story from conversation with 03727bb9d4cb4f64afdc383818739680 on January 17th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* how_to_get_started{"user_type":"new"}
    - action_set_onboarding
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"stack"}
    - slot{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* get_started_step2
    - action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa
    - utter_ask_python_installed


## Story from conversation with 4cdb0b3c6f6c4b3694fcb311ae72743b on January 21st 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu


## Story from conversation with 4b7ecc2cab6e42c5b1fedb8ab4056866 on December 29th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_whoami
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* ask_howold
    - action_chitchat
* out_of_scope{"number":42}
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope{"number":42}
    - utter_out_of_scope
    - utter_possibilities


## Story from conversation with af5a6b3c39d04c6db2b682960e63f01c on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* react_positive
    - utter_react_positive
* enter_data{"jobfunction":"dancer"}
    - utter_not_sure
    - utter_possibilities


## Story from conversation with 53d4ca53494d4469b7d94aca2f7b3fec on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu{"product":"nlu"}
    - slot{"product":"nlu"}
    - action_faqs
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu


## Story from conversation with 4a4e903fc43940db9ccdb9153dfdadcb on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager":"pip"}
    - slot{"package_manager":"pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* enter_data
    - action_store_problem_description
    - slot{"problem_description":"tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible."}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* enter_data
    - utter_not_sure
    - utter_possibilities


## Story from conversation with 5f3a2ea92d184a9f96df7240e4f7e2d9 on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## Story from conversation with ced8c1eb9a8d485f88a02d931b2879bd on January 16th 2019
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy":true}
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* affirm
    - utter_what_help
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
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
    - utter_direct_to_step2
