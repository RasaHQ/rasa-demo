## next step prompt
* next_step
    - action_next_step

## faqs
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs

## more faqs
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs

## just newsletter
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
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

## just newsletter, continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR  ask_faq_channels OR  ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + nlu + nothing special
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_for_nlu_specifics
* deny
    - utter_ask_faq_tutorialnlu
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* greet
    - action_greet_user
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
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - action_greet_user
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
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* greet
    - action_greet_user
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
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
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
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
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
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## FAQ - tell more about rasa x ee
* ask_faq_ee
    - action_faqs
* explain
    - utter_faq_ee_more

## FAQ - tell more about languages
* ask_faq_languages OR ask_faq_is_programming_required
    - action_faqs
* explain
    - utter_faq_language_more

## FAQ - tell more about voice
* ask_faq_voice
    - action_faqs
* explain
    - utter_faq_voice_more

## FAQ - tell more about slots
* ask_faq_slots
    - action_faqs
* explain
    - utter_faq_slots_more

## FAQ - tell more about channels
* ask_faq_channels
    - action_faqs
* explain
    - utter_faq_channels_more

## FAQ - Step 2 flow interrupted
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build

## FAQ - Step 2 flow interrupted
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_ready_to_build

## FAQ - Step 2 flow interrupted
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_ready_to_build
* affirm
    - utter_run_rasa_init
    - utter_direct_to_step3

## FAQ - Step 2 flow interrupted
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## technical_question - deny
* technical_question
    - action_docs_search
    - utter_ask_docs_help
* deny
    - action_forum_search

## technical_question - affirm
* technical_question
    - action_docs_search
    - utter_ask_docs_help
* affirm
    - utter_great

## FAQ - Step 2 flow interrupted
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## FAQ - Step 2 flow interrupted
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - action_store_problem_description
    - utter_installation_instructions
    - utter_direct_to_forum_for_help
    - utter_run_rasa_init
    - utter_direct_to_step3

## FAQ - Step 2 flow interrupted
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_ready_to_build

## Just don't want to continue
* install_rasa
    - utter_installation_command
    - utter_having_trouble_installing
    - utter_ask_ready_to_build
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_ready_to_build

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"all"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_explain_x
    - utter_direct_to_step2

## new to rasa/bots, explain x and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* affirm OR how_to_get_started{"product":"x"}
    - slot{"product": "x"}
    - utter_explain_x
    - utter_also_explain_nlucore
* deny
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain core and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain x, then direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "x"}
    - slot{"product": "x"}
    - utter_explain_x
    - utter_also_explain_nlucore
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs

## new to rasa/bots, explain core, then nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain x and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "x"}
    - slot{"product": "x"}
    - utter_explain_x
    - utter_also_explain_nlucore
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, don't explain and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_ask_explain_nlucorex
* deny
    - utter_direct_to_step2

## new to rasa/bots, don't explain and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_rasa_components
    - utter_rasa_components_details
    - utter_ask_explain_nlucorex
* deny
    - utter_direct_to_step2
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
    - utter_direct_to_step2

## not new to rasa + not interested in products
* greet
    - action_greet_user
* ask_faq_ee OR ask_faq_languages OR ask_faq_is_programming_required OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource_cost OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials OR ask_faq_differencerasarasax OR ask_faq_rasax
    - action_faqs
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup
