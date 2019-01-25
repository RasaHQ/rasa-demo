## chitchat
* human_handoff
    - handoff: utter_contact_email

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* human_handoff
    - handoff: utter_contact_email

## just newsletter (with email already) + confirm
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* human_handoff
    - handoff: utter_contact_email

## just newsletter
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email

## just newsletter
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email

## just newsletter
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* human_handoff
    - handoff: utter_contact_email

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email


## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* human_handoff
    - handoff: utter_contact_email


## just sales
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email


## just sales
* greet
    - greet_success: action_greet_user
* human_handoff
    - handoff: utter_contact_email


## just sales
* greet
    - greet_success: action_greet_user
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* human_handoff
    - handoff: utter_contact_email


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
* human_handoff
    - handoff: utter_contact_email


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
* human_handoff
    - handoff: utter_contact_email



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
* human_handoff
    - handoff: utter_contact_email

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
* human_handoff
    - handoff: utter_contact_email

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
* human_handoff
    - handoff: utter_contact_email
