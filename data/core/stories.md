## thanks
* thank
    - utter_noworries
    - utter_anything_else

## bye
* bye
    - utter_bye

## greet
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## sales
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## newsletter + feedback
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## newsletter + affirm feedback
* greet
    - action_greet_user
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

## newsletter + deny feedback
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else

## newsletter, don't give email once
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter, continue, affirm, then contact sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## newsletter, don't continue, then contact sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## newsletter, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
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
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter then sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## sales then newsletter
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter, confirm, then sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## newsletter + ask why email

* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* explain
    - utter_response_why_email
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter + ask why email

* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* explain
    - utter_response_why_email
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - utter_anything_else

## sales, then newsletter, then confirm
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

## neither options
* greet
    - action_greet_user
* deny
    - utter_nohelp

## neither --> newsletter
* greet
    - action_greet_user
* deny
    - utter_nohelp
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## neither --> sales
* greet
    - action_greet_user
* deny
    - utter_nohelp
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - action_tag_feedback
    - utter_great
    - utter_anything_else

## chitchat --> email --> no email
* greet
    - action_greet_user
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* chitchat
    - respond_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
* affirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

## anything else? - yes
    - utter_anything_else
* affirm
    - utter_what_help

## anything else? - no
    - utter_anything_else
* deny
    - utter_thumbsup

## anything else?
    - utter_anything_else
* enter_data
    - utter_not_sure
    - utter_possibilities

## positive reaction
* react_positive
    - utter_react_positive

## negative reaction
* react_negative
    - utter_react_negative

## why rasa
* why_rasa
    - utter_why_rasa
    - utter_ask_more
* affirm
    - utter_why_rasa_research
    - utter_why_rasa_nlu
    - utter_why_rasa_dialogue
    - utter_why_rasa_os
    - utter_why_rasa_compliant

## why rasa
* why_rasa{"current_api":"tensorflow"}
    - slot{"current_api":"__other__"}
    - utter_why_rasa
    - utter_ask_more
* affirm
    - utter_why_rasa_research
    - utter_why_rasa_nlu
    - utter_why_rasa_dialogue
    - utter_why_rasa_os
    - utter_why_rasa_compliant

## why rasa
* why_rasa{"current_api":"luis"}
    - slot{"current_api":"luis"}
    - utter_why_rasa
    - utter_switch_luis
    - utter_ask_more_migrate
* affirm
    - utter_why_rasa_research
    - utter_why_rasa_nlu
    - utter_why_rasa_dialogue
    - utter_why_rasa_os
    - utter_why_rasa_compliant


## why rasa
* why_rasa{"current_api":"dialogflow"}
    - slot{"current_api":"dialogflow"}
    - utter_why_rasa
    - utter_switch_dialogflow
    - utter_ask_more_migrate
* affirm
    - utter_why_rasa_research
    - utter_why_rasa_nlu
    - utter_why_rasa_dialogue
    - utter_why_rasa_os
    - utter_why_rasa_compliant

## why rasa
* why_rasa
    - utter_why_rasa
    - utter_ask_more
* deny
    - utter_anything_else

## why rasa
* why_rasa{"current_api":"tensorflow"}
    - slot{"current_api":"__other__"}
    - utter_why_rasa
    - utter_ask_more
* deny
    - utter_anything_else

## why rasa
* why_rasa{"current_api":"luis"}
    - slot{"current_api":"luis"}
    - utter_why_rasa
    - utter_switch_luis
    - utter_ask_more_migrate
* deny
    - utter_anything_else

## why rasa
* why_rasa{"current_api":"dialogflow"}
    - slot{"current_api":"dialogflow"}
    - utter_why_rasa
    - utter_switch_dialogflow
    - utter_ask_more_migrate
* deny
    - utter_anything_else
