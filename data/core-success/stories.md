## thanks
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else

## bye
* bye
    - chitchat: utter_bye

## greet
* greet OR enter_data{"name": "akela"}
    - greet_success: action_greet_user

## sales
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletter + feedback
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletter + affirm feedback
* greet
    - greet_success: action_greet_user
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


## newsletter + deny feedback
* greet
    - greet_success: action_greet_user
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
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## newsletter, don't give email once
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* enter_data{"email": "maxmeier@firma.de"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## newsletter, don't give email then contact sales
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
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
* feedback{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletter, don't give email twice then contact sales
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - subscribe: utter_cantsignup
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
* feedback{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletter, don't give email twice
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - subscribe: utter_cantsignup
* enter_data{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback

## just newsletter (with email already) + confirm
* greet
    - greet_success: action_greet_user
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## just newsletter (with email already)
* greet
    - greet_success: action_greet_user
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
* signup_newsletter{"email": "maxmeier@firma.de"}
    - subscribe: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## just newsletter (with email already) - already subscribed
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## just newsletter
* greet
    - greet_success: action_greet_user
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

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
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

## newsletter then sales
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletter (already subscribed) then sales
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## just sales + confirm
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## sales then newsletter
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
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

## sales then newsletter - already subscribed
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
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

## newsletters, confirm, then sales
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## newsletters (already subscribed), confirm, then sales
* greet
    - greet_success: action_greet_user
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
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## sales, then newsletter, then confirm
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
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
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## sales, then newsletter (already subscribed), then confirm
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
* enter_data{"email": "maxmeier@firma.de"} OR enter_data{"number":"1"}
    - sales: action_store_email
    - slot{"email": "maxmeier@firma.de"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
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
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## neither options
* greet
    - greet_success: action_greet_user
* deny
    - chitchat: utter_nohelp

## deny, then accept privacy policy - neither options
* greet
    - greet_success: action_greet_user
* deny
    - chitchat: utter_nohelp

## neither --> newsletter
* greet
    - greet_success: action_greet_user
* deny
    - chitchat: utter_nohelp
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

## neither --> sales
* greet
    - greet_success: action_greet_user
* deny
    - chitchat: utter_nohelp
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
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else

## chitchat --> email --> no email
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
* affirm
    - chitchat: utter_thumbsup
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## anything else? - yes
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help

## anything else? - no
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_thumbsup

## anything else?
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## positive reaction
* react_positive
    - chitchat: utter_react_positive

## negative reaction
* react_negative
    - chitchat: utter_react_negative
