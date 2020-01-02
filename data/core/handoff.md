## chitchat
* human_handoff
    - utter_contact_email

## greet + handoff
* greet
    - action_greet_user
* human_handoff
    - utter_contact_email

## just newsletter + handoff, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter + handoff, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* human_handoff
    - utter_contact_email
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
* human_handoff
    - utter_contact_email
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales, explain, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* explain
    - action_explain_sales_form
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, explain, stop
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* explain
    - action_explain_sales_form
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
