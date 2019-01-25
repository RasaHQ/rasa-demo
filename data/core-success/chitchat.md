## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - chitchat: action_chitchat
* deny
    - chitchat: utter_nohelp

## more chitchat
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat

## ask_whatspossible
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat

## ask_whatspossible more
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat


## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - subscribe: action_chitchat
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter (with email already)
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter (with email already) + confirm - already subscribed
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter (with email already) - already subscribed
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## just newsletter
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just sales
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
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

## just sales
* greet
    - greet_success: action_greet_user
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
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

## just sales
* greet
    - greet_success: action_greet_user
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - sales: action_store_job
    - slot{"job_function": "Product Manager"}
    - sales: utter_ask_usecase
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
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


## just sales
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
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



## just sales
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
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

## just sales
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
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

## just sales
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt OR ask_whatspossible
    - chitchat: action_chitchat
    - sales: utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback

## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
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
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
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
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* how_to_get_started
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa + not new to chatbots + not migrating
* greet
    - greet_success: action_greet_user
* how_to_get_started
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
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, explain stack and try it out
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain stack and try it out
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain stack and try it out
* greet
    - greet_success: action_greet_user
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
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain core and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_also_explain_nlu
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain core and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* deny
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, explain core, then nlu and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain core, then nlu and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, explain nlu and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_also_explain_core
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain nlu and try out stack
* greet
    - greet_success: action_greet_user
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
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* deny
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, don't explain and try out stack
* greet
    - greet_success: action_greet_user
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, don't explain and try out stack
* greet
    - greet_success: action_greet_user
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
* deny
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, explain and skip to installation
* greet
    - greet_success: action_greet_user
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
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else


## not new to rasa + not interested in products
* greet
    - greet_success: action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup

## not new to rasa + not interested in products
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup

## not new to rasa + not interested in products
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup


## not new to rasa + nlu + nothing special
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
    - rasa_help: utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* deny
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
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
    - rasa_help: utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - rasa_help: action_store_unknown_nlu_part
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + no recommendation
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
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
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
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - rasa_help_success: utter_spacy_or_tensorflow
    - chitchat: utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
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
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": false}
    - rasa_help_success: utter_tensorflow
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
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
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
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
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_ask_entities
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## how to get started without privacy policy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - chitchat: action_chitchat
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
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart
