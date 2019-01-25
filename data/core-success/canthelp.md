## chitchat
* canthelp
    - chitchat: utter_canthelp

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter + confirm
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) + confirm
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) + confirm
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already)
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already)
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) + confirm - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) + confirm - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter (with email already) - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter +confirm - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* canthelp
    - chitchat: utter_canthelp

## just newsletter
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* canthelp
    - chitchat: utter_canthelp

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp


## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp

## just newsletter - already subscribed
* greet
    - greet_success: action_greet_user
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* canthelp
    - chitchat: utter_canthelp


## just sales
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp


## just sales
* greet
    - greet_success: action_greet_user
* canthelp
    - chitchat: utter_canthelp


## just sales
* greet
    - greet_success: action_greet_user
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* canthelp
    - chitchat: utter_canthelp


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
* canthelp
    - chitchat: utter_canthelp


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
* canthelp
    - chitchat: utter_canthelp



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
* canthelp
    - chitchat: utter_canthelp

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
* canthelp
    - chitchat: utter_canthelp

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
* canthelp
    - chitchat: utter_canthelp
