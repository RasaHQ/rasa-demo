## just newsletter + confirm
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## just newsletter
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu

## newsletter then sales
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest

## just newsletter
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest

## sales then newsletter
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## newsletters, confirm, then sales
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest

## sales, then newsletter, then confirm, then newsletter
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## Generated Story -8040213628850829742
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm

## Generated Story 8318399839020984146
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest

## Generated Story -886733977132472019
* greet
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* signup_newsletter
    - utter_ask_email
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirmationemail
    - utter_docu
* mood_confirm
    - utter_greet
    - utter_ask_goal
    - utter_inform_privacypolicy
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "Product Manager"}
    - slot{"jobfunction": "Product Manager"}
    - utter_ask_usecase
* enter_data
    - utter_ask_budget
* enter_data{"budget": "100k"}
    - slot{"budget": "100k"}
    - utter_sales_contact
* enter_data{"name": "Max Meier"}
    - slot{"name": "Max Meier"}
    - utter_ask_company
* enter_data{"company": "Allianz"}
    - slot{"company": "Allianz"}
    - utter_ask_businessmail
* enter_data{"email": "maxmeier@firma.de"}
    - slot{"email": "maxmeier@firma.de"}
    - utter_confirm_salesrequest
