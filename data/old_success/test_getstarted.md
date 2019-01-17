## Generated Story goal:getstarted, id:95df664afe4a4c8ca912dc187266b1f3 -5279527964718861841
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:e533c3a14c1b498ab67fac7127670b07 -2404378447758647418
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_default_fallback
    - rewind
* ask_whoisit
    - action_default_fallback
    - rewind
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* thank
    - utter_noworries
* enter_data
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"name": "sara"}
    - utter_possibilities
* enter_data
    - utter_possibilities
* ask_whatisrasa
    - action_chitchat
* ask_builder
    - action_chitchat
* ask_howdoing
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:7ccf985ca5bb4474a83f1fff4d1a5098 -153170677336640345
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:641e17503cfe485da09c4153a8eb277a 5139666573282387064
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_isbot
    - action_chitchat
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* mood_confirm
    - utter_thumbsup
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_howdoing
    - action_chitchat
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_ask_entities
* mood_confirm
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_moreinformation
    - utter_ask_jobfunction
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_duckling_info
    - utter_anything_else
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_store_usecase
    - slot{"use_case": "I want to know about nlu"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 1000000000}
    - utter_contact_email
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* out_of_scope
    - action_default_fallback
    - rewind
* nlu_info{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_contact_email
* bye
    - utter_bye
* enter_data
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:ee3aceb2fa0949249e5378ece75b004b -3334794131879128150
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* greet
    - utter_quickstart
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:818b3f4616aa4a6cbea8341ecd5a8a57 -7535481903890064753
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - utter_greet
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - fail

## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_whoisit
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* canthelp
    - utter_canthelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* out_of_scope
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:a0a053da26be4f82a9d90879888de5b8 -4006138024073392343
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - fail

## Generated Story goal:getstarted, id:758fc306c8f44a3cb2f30181df522f49 -9085318817530331958
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - action_default_fallback
    - rewind
    - fail

