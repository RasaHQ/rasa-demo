## Generated Story goal:getstarted, id:ee3aceb2fa0949249e5378ece75b004b -3334794131879128150
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ee3aceb2fa0949249e5378ece75b004b -3334794131879128150
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatisrasa
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:a0a053da26be4f82a9d90879888de5b8 -4006138024073392343
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:641e17503cfe485da09c4153a8eb277a 5139666573282387064
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_isbot
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_howdoing
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_what_language   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language   <!-- predicted: success -->
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_getstarted   <!-- predicted: success -->
    - utter_first_bot_with_rasa   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* deny
    - action_set_onboarding   <!-- predicted: success -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_ask_entities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - action_store_entity_extractor   <!-- predicted: success -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_duckling_info   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_store_usecase   <!-- predicted: success -->
    - slot{"use_case": "I want to know about nlu"}
    - utter_thank_usecase   <!-- predicted: success -->
    - utter_ask_budget   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"amount-of-money": 1000000000}
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* out_of_scope
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:641e17503cfe485da09c4153a8eb277a 5139666573282387064
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_isbot
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_howdoing
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_what_language   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language   <!-- predicted: success -->
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_getstarted   <!-- predicted: success -->
    - utter_first_bot_with_rasa   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* deny
    - action_set_onboarding   <!-- predicted: success -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_ask_entities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - action_store_entity_extractor   <!-- predicted: success -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_duckling_info   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_store_usecase   <!-- predicted: success -->
    - slot{"use_case": "I want to know about nlu"}
    - utter_thank_usecase   <!-- predicted: success -->
    - utter_ask_budget   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"amount-of-money": 1000000000}
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* bye
    - utter_bye   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:641e17503cfe485da09c4153a8eb277a 5139666573282387064
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_isbot
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_howdoing
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_what_language   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language   <!-- predicted: success -->
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_getstarted   <!-- predicted: success -->
    - utter_first_bot_with_rasa   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* deny
    - action_set_onboarding   <!-- predicted: success -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_ask_entities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - action_store_entity_extractor   <!-- predicted: success -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_duckling_info   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_store_usecase   <!-- predicted: success -->
    - slot{"use_case": "I want to know about nlu"}
    - utter_thank_usecase   <!-- predicted: success -->
    - utter_ask_budget   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"amount-of-money": 1000000000}
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* bye
    - utter_bye   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* out_of_scope
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:758fc306c8f44a3cb2f30181df522f49 -9085318817530331958
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:758fc306c8f44a3cb2f30181df522f49 -9085318817530331958
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:758fc306c8f44a3cb2f30181df522f49 -9085318817530331958
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* out_of_scope
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* canthelp
    - utter_canthelp   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: success -->
    - utter_ask_goal   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* out_of_scope
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:e533c3a14c1b498ab67fac7127670b07 -2404378447758647418
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* out_of_scope
    - action_default_fallback   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: fail -->
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_core_tutorial   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core   <!-- predicted: fail -->
    - utter_also_explain_nlu   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: success -->
    - utter_tryout   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* thank
    - utter_noworries   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: fail -->
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_core_tutorial   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core   <!-- predicted: fail -->
    - utter_also_explain_nlu   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: success -->
    - utter_tryout   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* thank
    - utter_noworries   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: success -->
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"name": "sara"}
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_whatisrasa
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_builder
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: success -->


## Generated Story goal:getstarted, id:ee3aceb2fa0949249e5378ece75b004b -3334794131879128150
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatisrasa
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - slot{"product": "both"}
    - utter_explain_core   <!-- predicted: fail -->
    - utter_also_explain_nlu   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_quickstart   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - fail
    - action_listen   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:95df664afe4a4c8ca912dc187266b1f3 -5279527964718861841
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_howdoing
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_ask_migration   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_ask_which_tool   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* greet
    - utter_greet   <!-- predicted: success -->
    - utter_inform_privacypolicy   <!-- predicted: success -->
    - utter_ask_goal   <!-- predicted: success -->
    - success
    - action_listen   <!-- predicted: success -->


## Generated Story goal:getstarted, id:a0a053da26be4f82a9d90879888de5b8 -4006138024073392343
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - action_set_onboarding   <!-- predicted: fail -->
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - fail
    - action_listen   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:7ccf985ca5bb4474a83f1fff4d1a5098 -153170677336640345
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core   <!-- predicted: fail -->
    - utter_also_explain_nlu   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - success
    - action_listen   <!-- predicted: success -->


## Generated Story goal:getstarted, id:641e17503cfe485da09c4153a8eb277a 5139666573282387064
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_isbot
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_howdoing
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_what_language   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language   <!-- predicted: success -->
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_getstarted   <!-- predicted: success -->
    - utter_first_bot_with_rasa   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* deny
    - action_set_onboarding   <!-- predicted: success -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - slot{"nlu_part": "intent"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"language": "hindi"}
    - slot{"language": "hindi"}
    - slot{"language": "hindi"}
    - utter_ask_entities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - action_store_entity_extractor   <!-- predicted: success -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_duckling_info   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_moreinformation   <!-- predicted: success -->
    - utter_ask_jobfunction   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_store_usecase   <!-- predicted: success -->
    - slot{"use_case": "I want to know about nlu"}
    - utter_thank_usecase   <!-- predicted: success -->
    - utter_ask_budget   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"amount-of-money": 1000000000}
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* nlu_info{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - slot{"nlu_part": "entity"}
    - utter_nlu_entity_tutorial   <!-- predicted: success -->
    - utter_offer_recommendation   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* mood_confirm
    - utter_contact_email   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* bye
    - utter_bye   <!-- predicted: success -->
    - success
    - action_listen   <!-- predicted: success -->


## Generated Story goal:getstarted, id:758fc306c8f44a3cb2f30181df522f49 -9085318817530331958
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - fail
    - action_listen   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:818b3f4616aa4a6cbea8341ecd5a8a57 -7535481903890064753
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_thumbsup   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_nohelp   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - fail
    - action_listen   <!-- predicted: fail -->


## Generated Story goal:getstarted, id:ed0d25fa6352458eb89f7856c775eec6 -1464773912700148023
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* canthelp
    - utter_canthelp   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: success -->
    - utter_ask_goal   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - fail   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->


## Generated Story goal:getstarted, id:e533c3a14c1b498ab67fac7127670b07 -2404378447758647418
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* enter_data
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: fail -->
    - utter_explain_core   <!-- predicted: fail -->
    - utter_tryout   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - success
    - action_listen   <!-- predicted: success -->


## Generated Story goal:getstarted, id:558d3cce56a74cbd8a25a195c947e9e9 -5724240141577552002
* greet
    - utter_greet   <!-- predicted: fail -->
    - utter_inform_privacypolicy   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whoisit
    - action_chitchat   <!-- predicted: fail -->
    - utter_ask_goal   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: fail -->
    - utter_possibilities   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_core_tutorial   <!-- predicted: fail -->
    - utter_anything_else   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: fail -->
    - utter_first_bot_with_rasa   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* mood_confirm
    - action_set_onboarding   <!-- predicted: fail -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* deny
    - utter_explain_stack   <!-- predicted: fail -->
    - utter_stack_details   <!-- predicted: fail -->
    - utter_explain_nlucore   <!-- predicted: fail -->
    - action_listen   <!-- predicted: fail -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core   <!-- predicted: fail -->
    - utter_also_explain_nlu   <!-- predicted: fail -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: success -->
    - utter_tryout   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: success -->
    - utter_anything_else   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* thank
    - utter_noworries   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: success -->
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data{"name": "sara"}
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* enter_data
    - utter_possibilities   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_whatisrasa
    - action_chitchat   <!-- predicted: success -->
    - action_listen   <!-- predicted: success -->
* ask_builder
    - action_chitchat   <!-- predicted: success -->
    - success
    - action_listen   <!-- predicted: success -->


