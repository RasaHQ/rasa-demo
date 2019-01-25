## chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities

## say enter data outside the flows
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## say confirm outside the flows 2
* greet
    - greet_success: action_greet_user
* affirm
    - chitchat: utter_thumbsup

## say greet outside the flows
* greet
    - greet_success: action_greet_user
* greet OR enter_data{"name": "akela"}
    - greet_success: action_greet_user

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
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
    - chitchat: utter_great
    - subscribe: utter_ask_email
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
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
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - sales: utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
