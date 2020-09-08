## chitchat
* canthelp
    - utter_canthelp

## greet + canthelp
* greet
    - action_greet_user
* canthelp
    - utter_canthelp

## greet + newsletter + canthelp + continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu

## greet + newsletter + canthelp + don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales + continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales + don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## Story from conversation with 3db7df5613a2487a809694e2f6b2b34e on November 25th 2019

* greet
    - action_greet_user
    - slot{"shown_privacy":true}
* nlu_generation_tool_recommendation{"product":"nlu"}
    - slot{"product":"nlu"}
    - utter_nlu_tools

## Story from conversation with f5a068e6fc79471e9e4e7fb3eb3fbf56 on September 8th 2020

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* enter_data{"language":"python"}
    - slot{"language":"python"}
    - slot{"language":"python"}
    - action_store_unknown_product
    - slot{"unknown_product":"python"}
    - utter_no_guide_for_switch
    - utter_anything_else
* chitchat
    - respond_chitchat
* faq{"company":"c"}
    - slot{"company":"c"}
    - slot{"company":"c"}
    - respond_faq
    - action_set_faq_slot
    - slot{"faq":"is_programming_required"}
* bye
    - slot{"language":"python"}
    - slot{"company":"c"}
    - utter_ask_budget
