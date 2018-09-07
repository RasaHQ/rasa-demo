## story number 1
* greet
    - utter_greet
    - utter_inform_privacypolicy
* out_of_scope
    - utter_must_accept
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
* enter_data{"email":"hi@rasa.com"}
    - slot{"email":"hi@rasa.com"}
    - action_store_email
    - slot{"email":"hi@rasa.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":false}
    - utter_already_subscribed
    - utter_docu
* thank
    - utter_noworries
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

## story number 2
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 3
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

## story number 4
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* thank
    - utter_noworries
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 5
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* thank
    - utter_noworries
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 6
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat

## story number 7
* greet
    - utter_greet
    - utter_inform_privacypolicy
* greet
    - utter_must_accept
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* greet
    - utter_possibilities
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

## story number 8
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## story number 9
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* enter_data
    - utter_possibilities
* deny
    - utter_nohelp

## story number 10
* greet
    - utter_greet
    - utter_inform_privacypolicy
* greet
    - utter_must_accept
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup

## story number 11
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
* enter_data
    - utter_possibilities

## story number 12
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
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - action_store_email
    - slot{"email":"test@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
* enter_data
    - utter_possibilities

## story number 13
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
* enter_data{"email":"test@gmail.com"}
    - slot{"email":"test@gmail.com"}
    - action_store_email
    - slot{"email":"test@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed":true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_thumbsup

## story number 14
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* greet
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat

## story number 15
* greet
    - utter_greet
    - utter_inform_privacypolicy
* greet
    - utter_must_accept
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* ask_weather
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities

## story number 16
* greet
    - utter_greet
    - utter_inform_privacypolicy
* greet
    - utter_must_accept
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* enter_data
    - utter_possibilities

## story number 17
* greet
    - utter_greet
    - utter_inform_privacypolicy
* greet
    - utter_must_accept
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
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
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_awesome
    - utter_ask_goal
* ask_weather
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp
* enter_data
    - utter_possibilities
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"number":5}
    - utter_possibilities
* enter_data
    - utter_possibilities
