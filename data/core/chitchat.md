## chitchat
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat

## deny privacy policy
* greet
    - utter_greet
    - utter_inform_privacypolicy
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_inform_privacypolicy
* deny
    - utter_no_speak

## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter + confirm
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
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
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_goal
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu

## just newsletter (with email already)
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter (with email already) + confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## just newsletter (with email already) - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter +confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter +confirm - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_confirmationemail
    - utter_docu

## just newsletter
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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

## just newsletter - already subscribed
* greet
    - utter_greet
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
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
    - utter_ask_goal
* signup_newsletter
    - utter_ask_email
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed
    - utter_docu

## just sales
* greet
    - utter_greet
    - utter_inform_privacypolicy
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_inform_privacypolicy
* mood_confirm
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
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
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
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
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data    
    - action_store_usecase
    - slot{"use_case": "bots"}
    - utter_ask_budget
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_budget
* enter_data{"number": "100"} OR enter_data{"amount-of-money": "100k"} OR enter_data{"number": "100", "amount-of-money": "100"}
    - action_store_budget
    - slot{"budget": "100k"}
    - utter_sales_contact
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
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_sales_contact
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
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
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
* enter_data{"name": "Max Meier"}
    - action_store_name
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - action_store_company
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* ask_weather OR ask_builder OR ask_whatspossible OR ask_howdoing
    - action_chitchat
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
