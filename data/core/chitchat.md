## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat

## ask_whatspossible
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat

## ask_whatspossible more
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat


## just newsletter + confirm
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## just newsletter (with email already) + confirm - already subscribed
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) - already subscribed
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback

## just newsletter +confirm - already subscribed
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter +confirm - already subscribed
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## just newsletter
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## just newsletter - already subscribed
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback

## just newsletter - already subscribed
* greet
    - action_greet_user
* signup_newsletter
    - utter_great
    - utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
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

## just sales
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
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

## just sales
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"job_function": "Product Manager"}
    - utter_ask_usecase
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
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


## just sales
* greet
    - action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
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



## just sales
* greet
    - action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
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

## just sales
* greet
    - action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
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

## just sales
* greet
    - action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
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
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2


## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
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
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2


## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
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
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2


## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
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
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, explain core and try out stack
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
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core and try out stack
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
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2


## new to rasa/bots, explain core, then nlu and try out stack
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
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and try out stack
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
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2


## new to rasa/bots, explain nlu and try out stack
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
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and try out stack
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
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, don't explain and try out stack
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2

## new to rasa/bots, don't explain and try out stack
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
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_direct_to_step2


## not new to rasa + not interested in products
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_ask_which_product
* deny
    - utter_thumbsup


## not new to rasa + nlu + nothing special
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else


## not new to rasa + nlu + intent + no recommendation
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - utter_duckling
    - utter_anything_else


## how to get started without privacy policy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
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
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
