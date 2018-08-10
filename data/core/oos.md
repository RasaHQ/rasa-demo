## chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## say random stuff outside the flows 1
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* greet OR enter_data OR mood_confirm
    - utter_possibilities

## say random stuff outside the flows 2
* greet
    - utter_greet
    - utter_inform_privacypolicy
* deny
    - utter_no_speak
    - utter_change_mind
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* greet OR enter_data OR mood_confirm
    - utter_possibilities


## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
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
* mood_confirm
    - utter_thumbsup

## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_thumbsup

## just newsletter (with email already) + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_thumbsup

## just newsletter (with email already)
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu

## just newsletter (with email already) + confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm
    - utter_thumbsup

## just newsletter (with email already) - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## just newsletter +confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
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
* mood_confirm
    - utter_thumbsup

## just newsletter +confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm
    - utter_thumbsup

## just newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
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

## just newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu

## just newsletter - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
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

## just newsletter - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
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

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"job_function": "Product Manager"}
    - utter_ask_usecase
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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


## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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



## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
