## out of scope
* out_of_scope
    - respond_out_of_scope
    - utter_possibilities

## say enter data outside the flows
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities

## say confirm outside the flows 2
* greet
    - action_greet_user
* affirm
    - utter_thumbsup

## say greet outside the flows
* greet
    - action_greet_user
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## just newsletter + confirm
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* out_of_scope
    - respond_out_of_scope
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
