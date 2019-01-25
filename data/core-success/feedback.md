## feedback1
    - feedback: utter_ask_feedback
* out_of_scope
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## feedback2
    - feedback: utter_ask_feedback
* enter_data
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## feedback3
    - feedback: utter_ask_feedback
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else

## feedback deny
    - feedback: utter_ask_feedback
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## feedback thumbsup
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## feedback thumbsup
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - chitchat: utter_great
    - chitchat: utter_anything_else
