## prompt for getting started
* get_started_step1
    - greet_success: action_greet_user

## prompt for getting started + confirm
* get_started_step1
    - greet_success: action_greet_user
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## new to rasa at start, built bot before
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration

## new to rasa at start
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore

## new to rasa + not new to chatbots + not migrating
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa + not new to chatbots + migrating from dialogflow

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else

## new to rasa + not new to chatbots + migrating from luis

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api": "luis"}
    - getstarted_1_success: utter_switch_luis
    - chitchat: utter_anything_else

## new to rasa + not new to chatbots + migrating from something else

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch
    - rasa_help: action_store_unknown_product
    - getstarted_1: utter_no_guide_for_switch
    - chitchat: utter_anything_else

##  migrating from dialogflow

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else

## new to rasa + not new to chatbots + migrating from luis

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* switch{"current_api": "luis"}
    - getstarted_1_success: utter_switch_luis
    - chitchat: utter_anything_else

## new to rasa + not new to chatbots + migrating from something else

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* switch OR enter_data
    - getstarted_1: action_store_unknown_product
    - getstarted_1_success: utter_no_guide_for_switch
    - chitchat: utter_anything_else


## new to rasa/bots, explain stack and try it out

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain core and try out stack

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain core, then nlu and try out stack

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain nlu and try out stack

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart

## new to rasa/bots, explain nlu then core and try out stack

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, don't explain and try out stack

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart


## new to rasa/bots, explain and skip to installation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else

## new to rasa/bots, explain nlu and skip to installation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* deny
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else

## new to rasa/bots, explain core and skip to installation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* deny
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else

## new to rasa/bots, explain core and try nlu

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## new to rasa/bots, explain nlu and try nlu

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## new to rasa/bots, explain both and try nlu

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## new to rasa/bots, explain nlu then core and try nlu

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else


## not new to rasa + not interested in products

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup

## not new to rasa + core

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else

## skip to info on core
* how_to_get_started{"product": "core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else

## skip to info on core

* how_to_get_started{"product": "core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else

## not new to rasa + nlu + nothing special

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* deny
    - rasa_help_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## not new to rasa + nlu + unknown topic

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - rasa_help: action_store_unknown_nlu_part
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else

## not new to rasa + nlu + intent + no recommendation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - rasa_help_success: utter_spacy_or_tensorflow
    - chitchat: utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": false}
    - rasa_help_success: utter_tensorflow
    - chitchat: utter_anything_else

## not new to rasa + nlu + intent + tool recommendation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* nlu_generation_tool_recommendation
    - rasa_help_success: utter_nlu_tools

## not new to rasa + nlu + entity + no recommendation

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## not new to rasa + nlu + entity + pipeline spacy

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "name"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_spacy"}
    - rasa_help_success: utter_spacy
    - chitchat: utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else

## not new to rasa + nlu + entity + pipeline ner_crf

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation OR affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - rasa_help_success: utter_crf
    - chitchat: utter_anything_else

## not new to rasa + nlu + entity + duckling info

* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else

## skip to info on nlu entities
* nlu_info{"nlu_part": "entity recognition"}
    - rasa_help: utter_nlu_entity_tutorial
    - rasa_help: utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else

## switch immediately to luis
* switch{"current_api":"luis"}
    - getstarted_1_success: utter_switch_luis
    - chitchat: utter_anything_else

## switch immediately to dialogflow
* switch{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else

## how much does rasa cost
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else

## source code
* source_code
    - faq: utter_source_code
    - chitchat: utter_anything_else

## how to get started without privacy policy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product":"core"} OR affirm OR how_to_get_started{"product":"stack"}
    - getstarted_1_success: utter_quickstart
