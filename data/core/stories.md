## deny privacy policy
* greet
    - utter_greet
    - utter_inform_privacypolicy
* deny
    - utter_no_speak

## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## just newsletter (with email already) + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* signup_newsletter{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## just newsletter (with email already)
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu

## just newsletter (with email already) + confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm

## just newsletter (with email already) - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
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
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm

## just newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu

## just newsletter - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## newsletter then sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest

## newsletter (already subscribed) then sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest

## sales then newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu

## sales then newsletter - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## newsletters, confirm, then sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest

## newsletters (already subscribed), confirm, then sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest

## sales, then newsletter, then confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## sales, then newsletter (already subscribed), then confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - action_store_job
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu
* mood_confirm
