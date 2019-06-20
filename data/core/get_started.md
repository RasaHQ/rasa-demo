## prompt for getting started
* get_started_step1
    - action_greet_user

## prompt for getting started + confirm
* get_started_step1
    - action_greet_user
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa

## new to rasa at start, built bot before
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new
    - utter_built_bot_before
* affirm
    - utter_ask_migration

## new to rasa at start
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore

## new to rasa + not new to chatbots + not migrating
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + migrating from dialogflow
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api": "luis"}
    - utter_switch_luis
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from something else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch
    - action_store_unknown_product
    - utter_no_guide_for_switch
    - utter_anything_else

##  migrating from dialogflow
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"current_api": "luis"}
    - utter_switch_luis
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from something else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch OR enter_data
    - action_store_unknown_product
    - utter_no_guide_for_switch
    - utter_anything_else

## new to rasa/bots, explain stack
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain nlu
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu then core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_direct_to_step2

## not new to rasa/bots, explain difference between nlu and core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* explain
    - utter_explain_stack
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain difference between nlu and core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, don't explain
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2

## not new to rasa + not interested in products
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## skip to info on core
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## not new to rasa + nlu + nothing special
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + tool recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* nlu_generation_tool_recommendation
    - utter_nlu_tools

## not new to rasa + nlu + entity + no recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "name"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "SpacyEntityExtractor"}
    - utter_spacy
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline CRFEntityExtractor
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "CRFEntityExtractor"}
    - utter_crf
    - utter_anything_else

## not new to rasa + nlu + entity + duckling info
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else

## skip to info on nlu entities
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else

## switch immediately to luis
* switch{"current_api":"luis"}
    - utter_switch_luis
    - utter_anything_else

## switch immediately to dialogflow
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## how much does rasa cost
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else

## source code
* source_code
    - utter_source_code
    - utter_anything_else
