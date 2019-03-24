## chitchat
* human_handoff
    - utter_contact_email

## greet + handoff
* greet
    - action_greet_user
* human_handoff
    - utter_contact_email

## just newsletter + handoff
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - action_deactivate_form
    - form{"name": null}

## just sales
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* human_handoff
    - utter_contact_email
    - action_deactivate_form
    - form{"name": null}
