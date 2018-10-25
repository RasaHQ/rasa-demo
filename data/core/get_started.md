## new to rasa + not new to chatbots + not migrating
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* deny
    - utter_are_you_new_to_chatbots
* deny
    - utter_ask_migration
* deny
    - utter_encourage_building_bot
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from dialogflow
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* deny
    - utter_are_you_new_to_chatbots
* deny
    - utter_ask_migration
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from luis
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* deny
    - utter_are_you_new_to_chatbots
* deny
    - utter_ask_migration
* switch{"current_api": "luis"}
    - utter_switch_luis
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from something else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* deny
    - utter_are_you_new_to_chatbots
* deny
    - utter_ask_migration
* switch
    - action_store_unknown_product
    - utter_no_guide_for_switch
    - utter_anything_else

## new to rasa + new to chatbots
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* deny
    - utter_are_you_new_to_chatbots
* mood_confirm
    - utter_chatbot_tutorial
    - utter_anything_else

## not new to rasa + core
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## skip to info on core 
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## not new to rasa + nlu + nothing special
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* deny
    - utter_great
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR mood_confirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR mood_confirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow

## not new to rasa + nlu + intent + tool recommendation
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* nlu_generation_tool_recommendation
    - utter_nlu_tools

## not new to rasa + nlu + entity + no recommendation
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* deny
    - utter_great
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline spacy
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR mood_confirm
    - utter_ask_entities
* enter_data{"entity": "name"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_spacy"}
    - utter_spacy

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR mood_confirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - utter_duckling

## not new to rasa + nlu + entity + pipeline ner_crf
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR mood_confirm
    - utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - utter_crf

## not new to rasa + nlu + entity + duckling info
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_quickstart
    - utter_have_you_used_rasa_before
* mood_confirm
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "duckling"}
    - utter_duckling_info

## skip to info on nlu
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
