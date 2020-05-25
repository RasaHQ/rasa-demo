## faqs
* faq: what is [Rasa X](product)?
    - slot{"product": "x"}
    - respond_faq
    - action_set_faq_slot

## faqs
* faq: Can you tell which messaging channels does rasa support?
    - respond_faq
    - action_set_faq_slot

## FAQ - tell more about rasa x ee
* faq: Can you tell me about the enterprise edition?
    - respond_faq
    - action_set_faq_slot
    - slot{"faq":"ee"}
* explain: can you elaborate
    - action_explain_faq

## new to rasa at start
* how_to_get_started: I'm [new](user_type) to Rasa
    - slot{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new
    - utter_built_bot_before
* deny: No
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* faq: you are [open source](product:rasa) ?
    - slot{"product":"rasa"}
    - utter_explain_nlu
    - utter_explain_core

## not new to rasa/bots, faq rasa
* how_to_get_started: How do I get started 
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny: No
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* faq: ed in [RASA open source](product:rasa) edition?
    - slot{"product":"rasa"}
    - utter_explain_nlu
    - utter_explain_core

## get started rasa open source
* how_to_get_started: How do I get started 
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny: No
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started: [rasa open source](product:rasa) first
    - slot{"product":"rasa"}
    - utter_explain_core
    - utter_explain_nlu

## just newsletter + confirm
* greet: hi!
    - action_greet_user
* chitchat: who built you?
    - respond_chitchat
* signup_newsletter: can I sign up for the newsletter?
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm: Yes please
    - utter_thumbsup
    - utter_anything_else

## just newsletter, continue, + confirm
* greet: hi
    - action_greet_user
* signup_newsletter: can i get emailed a newsletter?
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* chitchat: are you a bot?
    - respond_chitchat
    - utter_ask_continue_newsletter
* affirm: yep
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm: sure
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + rasa
* how_to_get_started: help me get started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny: no
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* faq: [rasa open source](product)
    - slot{"product": "rasa"}
    - utter_explain_core
    - utter_explain_nlu

## not new to rasa + rasax
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* faq: [rasa x](product)
    - slot{"product": "x"}
    - utter_explain_x
    - utter_also_explain_nlucore

## faq with entities
* faq: what's the difference between [rasa](product) and [rasa x](product)
    - slot{"product": "x"}
    - respond_faq
    - action_set_faq_slot

## chitchat 
* chitchat: By what means were you made?
    - respond_chitchat