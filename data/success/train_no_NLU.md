## Generated Story goal:oos, id:ca672123deee42f3a39ddab393df550a -7544176553772191309
* ask_whatspossible
    - action_chitchat
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:98ffd6a608dd480196011d4952f65929 1911556782908513314
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - action_default_fallback
    - event_rewind
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:oos, id:c3ae6708ad8147cc9a6cc88994ad0d58 -2489073378823378250
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:chitchat, id:fe4f04a83ece4168a81db6ccaf25dc93 -6811014238179839278
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whoisit
    - action_chitchat

## Generated Story goal:oss, id:555b2de2b8eb4c488c79c669d89b6c0e 718994536149191750
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_isbot
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet

## Generated Story goal:chitchat, id:ce0384bba8f24ca9892134f4be01940c 2884291399475986093
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* canthelp
    - utter_canthelp

## Generated Story goal:1 step, id:cfc9d23839974db8a822cd7a1ba5fa1b 261036980615358864
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
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:rasa_help, id:c689c4e5077444dcb9abae16cb1ef056 -3565881678591948494
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
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
* enter_data
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:8ea61bcfe1c94feea443d224d5b737f4 9032731066057427144
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather
    - action_default_fallback
    - event_rewind
* ask_weather
    - action_default_fallback
    - event_rewind
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_ask_migration
* enter_data
    - utter_ask_which_tool
* enter_data
    - utter_greet
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "klaus"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "atleta.co"}
    - utter_ask_businessmail
* enter_data{"email": "klaus@atleta.co"}
    - slot{"email": "klaus@atleta.co"}
    - action_store_email
    - slot{"email": "klaus@atleta.co"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Generated Story goal:1 step, id:8a2e9462510745f69e101fca7a7ba335 -4723717375194165105
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:chitchat, id:e9f6b5ff2c3f41cdac8134256c08b655 7370096374779455002
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_default_fallback
    - event_rewind
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

## Generated Story goal:1 step, id:2c217d9b5fa44472b86aafa9e75a064a -6177916407562427286
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else

## Generated Story goal:1 step, id:ced4cc1aff614809a9e847da70fba49c 7823482312725170905
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* deny
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - event_rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:8a2bc20edd8e4e39b3fb49e662d47e8f -5677279810188197264
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
* enter_data
    - utter_tryout
* enter_data
    - utter_quickstart
    - utter_anything_else
* enter_data{"number": 7}
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:1 step, id:de34f86714fe4325875b24c55b12554d -6485527428897308503
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather
    - action_default_fallback
    - event_rewind
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* contact_sales
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:chitchat, id:39fe88d4b5454e7faafc0a414cecb934 2041711534130626840
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_howdoing
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - event_rewind
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* out_of_scope{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_ask_goal
    - utter_anything_else
* ask_whatisrasa
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:7d2ff25e291c40d2a6d5833abd6bd5b2 339760679551169809
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
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
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore

## Generated Story goal:1 step, id:0e7924235b744a8f92a671e3aaf62c3c 1343866674497983662
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
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
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:2f4945611ec5456eafc9c43f3a5a19ec 2744259509352556449
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* mood_confirm
    - utter_ask_migration
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* bye{"name": "Good Bye"}
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* canthelp
    - utter_canthelp

## Generated Story goal:1 step, id:d5cb8eca8da84808b3120f68885621d3 378092498454228307
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
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

## Generated Story goal:1 step, id:e6385339f24944f8a24c292c222b3e14 -5308129887755878221
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
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu

## Generated Story goal:1 step, id:1a9e43aadf5749baaedf3b5ccada46cf -2631220862342703900
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - action_default_fallback
    - event_rewind
* mood_confirm
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* ask_weather
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_builder
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* out_of_scope
    - action_default_fallback
    - event_rewind
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* bye
    - utter_bye

## Generated Story goal:1 step, id:b6be4b6887654f0483b9f185ad8ce193 210527505520178689
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* out_of_scope
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - event_rewind
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - event_rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* nlu_generation_tool_recommendation
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:rasa_help, id:ddeb400cdede4d2795986a5e532bacc0 -3068468198820851318
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
* ask_whoisit
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* technical_question
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
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:rasa_help, id:9e010bccce1e4ae5aff01cbd03ab4578 7580879271494574389
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_whatisrasa
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
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_whatisrasa{"product": "core"}
    - slot{"product": "core"}
    - action_chitchat
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:e9ecc761cff04e9b9e2578c0b575614f -3171612578263789466
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:207b0767095b4cd7878e551853ce9dd6 2252454680301706096
* out_of_scope
    - action_default_fallback
    - event_rewind
* out_of_scope
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_thumbsup
    - utter_anything_else
* bye
    - utter_bye
* enter_data
    - utter_thumbsup
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:4764846e09df412a89db296bf7e34360 991771366496670363
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:8a12201f561542d7ab3fa83714c0ad21 -7003639062983410651
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:09120b9c2ceb4476b311d2804c352cf0 2443021565178283850
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* source_code
    - action_default_fallback
    - event_rewind
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
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data{"company": "microsoft"}
    - action_default_fallback
    - event_rewind
* how_to_get_started
    - action_store_unknown_product
    - slot{"unknown_product": "how can i get rasa"}
    - utter_no_guide_for_switch
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:ba496d95869d457d9956a40f1d9393b3 -437370484714520122
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_tryout
* enter_data
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:chitchat, id:e3941f1c46ba45c2a15c06090032d9ba -1421753784655186482
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_isbot
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
* ask_isbot
    - action_default_fallback
    - event_rewind
* out_of_scope
    - action_default_fallback
    - event_rewind
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_getstarted
* mood_confirm
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet

## Generated Story goal:rasa_help, id:f7ee04cb5ded407ca3cbfaaf1a6e6ccd 8770809357412576392
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
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
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - action_default_fallback
    - event_rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Generated Story goal:1 step, id:6fa4940c6860441b9c697d2fce21f26f 6871398079407181354
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_ask_migration
* out_of_scope
    - action_default_fallback
    - event_rewind
* mood_confirm
    - utter_ask_which_tool
* enter_data
    - action_store_budget
    - slot{"budget": "rasa"}
    - utter_sales_contact
    - utter_ask_name

## Generated Story goal:1 step, id:0bf96a04308746deaf57284ae1f505f6 -1521938769623966519
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:82a84b4f30154227b6ab1c74b21f3697 561239258012017185
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_isbot
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
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
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:3d73547690a146bc8956efa1721d830a 8991903938763902496
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* out_of_scope
    - utter_out_of_scope
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:?, id:cd678203af814fe6809c5c1758578e7a -3912157083290158111
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
* ask_isbot
    - action_chitchat
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_great
    - utter_anything_else
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core

## Generated Story goal:1 step, id:851219f6966a4ff68eda504e92ee1800 4183813613945141006
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
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
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* signup_newsletter
    - action_store_unknown_product
    - slot{"unknown_product": "subscribe"}
    - utter_no_guide_for_switch
    - utter_anything_else
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "michaelsuccess35@gmail.com"}
    - slot{"email": "michaelsuccess35@gmail.com"}
    - action_store_email
    - slot{"email": "michaelsuccess35@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## Generated Story goal:1 step, id:8c97cf83f2424fd0bf98106b81e29b77 -69091200961764888
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet{"name": "Hi Sara"}
    - utter_greet
* out_of_scope
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
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

## Generated Story goal:1 step, id:eb117502087b45b4a05ab33b148315f5 1181441383680892234
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else
* thank
    - utter_noworries
    - utter_anything_else

## Generated Story goal:1 step, id:e534f2427a524a96b0dc633b6f738ad0 -5965402682088083887
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:21ee481460224b6d8b4c483e9c6f3558 7424913629025657751
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
* deny
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* source_code
    - utter_source_code
    - utter_anything_else
* ask_weather
    - action_chitchat
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:suggestion, id:7755f1fa952f4694b85fd5fd4b1002b4 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:adf2df92e24d4fbd9d08fe75c4f5405f -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:4284e9640fbd4f9b9e746502bdacdc8a 5114563254026021804
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: enter_data
    - form: suggestion_form
    - slot{"suggestion": "can i integrate you to facebook?"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:e82e789c29da4e3a821f02b3b3313f47 3839758098278404083
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "Hello"}
    - form{"name": null}
    - slot{"requested_slot": null}
* enter_data
    - action_store_email
    - event_rewind
* enter_data{"email": "valid@gmail.com"}
    - slot{"email": "valid@gmail.com"}
    - action_store_email
    - slot{"email": "valid@gmail.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:suggestion, id:5e0b0f7f1cef43a9abedc6bbcd8f7399 1816249457063249809
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:suggestion, id:def3c3ddea8e49e7870acefc71b8803f -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:ddf0d6a0123d4da2a073bf0ca9d08547 7736032371816930724
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: ask_whatspossible
    - form: suggestion_form
    - slot{"suggestion": "what are you doing now?"}
    - form{"name": null}
    - slot{"requested_slot": null}
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:suggestion, id:9bdcfc353ded4a3dacb437db97c53f83 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:099248bc16ea445abe4beec64b1f09f7 1758838983709233062
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: deny
    - form: suggestion_form
    - slot{"suggestion": "but thats bad"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:a305867d571443b2a6e2da85690f145d -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:d084f3464e1a47dc83fe007583304eee -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:bffe2263404943489c5f182df76e02eb -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:chitchat, id:e9cb53d3a9de45049946ac7b23b874b8 -1219827075036063127
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities

## Generated Story goal:oos, id:68f3b38f8c88423aba5a2b6f5733e5ea -1610529620802613734
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:f12b8c1873db4fcfa5e170282cc4529f 4378123197332360374
* greet{"name": "Hola Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_isbot
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet

## Generated Story goal:chitchat, id:c7fc7a50438f46588b12e2e9132c3f1e -4653556363776339675
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* None
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:db64faf0c1304b4381f2e41d33a7d50a -1597663376357006658
* ask_howdoing
    - action_chitchat
* ask_isbot
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - event_rewind

## Generated Story goal:oos, id:29c6131a2fac46849c93da0e664e6a4a 269722786334557232
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_default_fallback
    - event_rewind

## Generated Story goal:chitchat, id:344e44f690a8482b800d698dc1151663 2796735675022632438
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* out_of_scope
    - action_default_fallback
    - event_rewind
* enter_data{"jobfunction": "developer"}
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:6242555cedfe47d780c02ce0f327a5df 5277955105532853469
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:chitchat, id:1b2e4c0a0d3945eb9b936b7da1057ee7 7565778831381151048
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:chitchat, id:f8a59dd16a0b4cfa8bfaf3e3a546b00a -1736430577713931271
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* ask_isbot
    - action_chitchat
    - utter_ask_goal

## Generated Story goal:1 step, id:7f06bca281be4b30b8baa86395cfc42e 7053904375831603070
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_chitchat

## Generated Story goal:chitchat, id:7085b3fccefa465fbe06f325da241747 4670196383732081190
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal

## Generated Story goal:chitchat, id:1fcde9442f784bacbe1b7d3c7eca603d -401056071036208481
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_builder
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* out_of_scope{"number": 1}
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:chitchat, id:1eb83efafee54007b12761660593850f 3511290615741462637
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope{"language": "danish"}
    - slot{"language": "danish"}
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat

## Generated Story goal:chitchat, id:97d9f198142f4300b364df6cec3ee9c4 8071521317749628654
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
* out_of_scope{"language": "chinese"}
    - slot{"language": "chinese"}
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:chitchat, id:4087d18832de4be5ad840e83ed5e9e2d 8762996506136495072
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:chitchat, id:a2f01eeaf8f24d19a9d98cf6cb0a81ae 2681982339449711367
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:oos, id:701390c6e773448fa9b616e5caf44de8 6472442402164167979
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:d5156c9f24c94f8abb93b2c6d3f97c68 2546431609318228425
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* ask_whoisit
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* mood_confirm
    - utter_thumbsup

## Generated Story goal:chitchat, id:3b24a4733c4f4a31889361fa1260ab0b -5101247318484886045
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet

## Generated Story goal:sales, id:817110817eaa49b394290737b9518a24 -462566369003474901
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_default_fallback
    - event_rewind
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "CTO"}
    - action_store_job
    - slot{"job_function": "CTO"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "dealer bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 10000}
    - action_store_budget
    - slot{"budget": 10000}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "Bruno Moreno"}
    - action_store_name
    - slot{"person_name": "Bruno Moreno"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "justto"}
    - utter_ask_businessmail
* enter_data{"email": "bruno@justto.com.br"}
    - slot{"email": "bruno@justto.com.br"}
    - action_store_email
    - slot{"email": "bruno@justto.com.br"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* canthelp
    - utter_canthelp

## Generated Story goal:oos, id:4594fd20825943288663a4a07e653c35 5076569460582843912
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:7624501739e047b7bfc0f589f5fa01e4 -7200134889673720566
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat

## Generated Story goal:chitchat, id:a0e8c8db1f8c431ca29544c60ce17f40 1572893672572215924
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope
    - action_default_fallback
    - event_rewind
* deny
    - utter_nohelp
* out_of_scope
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet

## Generated Story goal:chitchat, id:3b925461d97d4aa285f8bbe480d764cf -6254580709014713361
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind

## Generated Story goal:rasa_help, id:767c28121cd6439da94048442778cd9a 3363891258915656167
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* switch
    - action_chitchat
    - utter_ask_goal
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## Generated Story goal:chitchat, id:968cf701cdff47fc932e0be9959766d7 -1339550475365178328
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_default_fallback
    - event_rewind
* ask_whoisit
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:f121cb938fc14cf899e8cdfceaf6bf8f 2933433786369135389
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:sales, id:9e977cb78a6d438db900f04db58b920a 4419810639068783199
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"number": 0}
    - action_store_email
    - event_rewind
* enter_data{"number": 0}
    - action_store_email
    - event_rewind
* enter_data{"number": 0}
    - action_store_email
    - event_rewind
* enter_data
    - action_store_email
    - event_rewind
* enter_data{"number": 8}
    - action_store_email
    - event_rewind
* enter_data
    - action_store_email
    - event_rewind

## Generated Story goal:chitchat, id:865b754cc0284ca58c982ae20363b830 -883383238601963447
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities

## Generated Story goal:chitchat, id:0791f5cbbbac4fd09b26493fa4b94140 -3711277283141995909
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:rasa_help, id:5046ba43896f4182a0abaa56d7a88963 1099711539139696443
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation

## Generated Story goal:oos, id:80bf2b5a9173432daf4279d6b5db9455 1655297703188992639
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities

## Generated Story goal:1 step, id:12cb8140b3254ee596f4db7dc4a586f0 5919604054030769931
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* ask_whatisrasa{"product": "core"}
    - slot{"product": "core"}
    - action_chitchat
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:a172c8045f9045f789eb8ba23605942a 5026767906399176162
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:oos, id:16942b7d96674419a32ffaae2a3a4a25 -1721852574907787953
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* technical_question
    - action_default_fallback
    - event_rewind
* technical_question
    - action_chitchat

## Generated Story goal:oos, id:83e33cfc72d74f2a9080ba78db263227 -4160392066964314948
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:oos, id:cc15de625e8144cd9e851af2268fe679 4742354566058284251
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal

## Generated Story goal:1 step, id:e527a7be4cf24a45a491dd3b6cdfe7f0 5824221324980568987
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
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
* contact_sales
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:6a876df894a94626ae6dc05d46ac253b -5815976175188942981
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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

## Generated Story goal:1 step, id:745b4915d5c845fda14621c606651405 -3305333448167692692
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* mood_confirm
    - utter_thumbsup
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope{"product": "stack"}
    - slot{"product": "stack"}
    - action_default_fallback
    - event_rewind
* ask_whatisrasa{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:573ed9fbb537471b967ff5b1a3d63e55 -8958741670993427277
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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

## Generated Story goal:1 step, id:f143fecbfc0546d593bcb206c25362af 1990785055584402338
* greet{"name": "sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_default_fallback
    - event_rewind
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* deny
    - utter_thumbsup
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:35dfb78844e443c29fcf259121ebf364 -3162611685614736743
* greet{"name": "Hi Sara"}
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
* enter_data
    - action_default_fallback
    - event_rewind
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:8d159e7f93c843d5bc0325bc7012c894 -879519054223126572
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
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
* ask_whatisrasa{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:e92e70d3e29d483dbb2b04fb69c141d0 -205114075715080892
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* greet
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## Generated Story goal:1 step, id:1397120860494880a91a0c983effc2e7 -553487913843673840
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
* out_of_scope
    - utter_out_of_scope
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
* deny
    - utter_nohelp
* enter_data
    - utter_possibilities

## Generated Story goal:1 step, id:aba27ac7b5a84d93b57ddac0ea03b18e 1658446157400113038
* out_of_scope
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_ask_migration
* enter_data
    - utter_ask_which_tool
* deny
    - utter_nohelp
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
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:f610ab250c7c4469a374482a015c5da8 1736113655662359928
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:21827132bb594f9da84437414b5bc3d1 -3399097523691223779
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* greet
    - utter_explain_stack
    - utter_ask_businessmail

## Generated Story goal:1 step, id:51960406adaf48bbb06c2a9ce9a1aea8 -6525319208719722554
* greet{"name": "Hi Sara"}
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else

## Generated Story goal:1 step, id:611bef8d94c8436bb3ab34639c3c4a63 -8505272618868443090
* contact_sales
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* how_to_get_started
    - action_default_fallback
    - event_rewind
* enter_data{"number": 1}
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "yeetboi"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "ui bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "sam"}
    - action_store_name
    - slot{"person_name": "sam"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "pigeon"}
    - utter_ask_businessmail
* enter_data{"email": "pigeo@yeet.tt"}
    - slot{"email": "pigeo@yeet.tt"}
    - action_store_email
    - slot{"email": "pigeo@yeet.tt"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:sales, id:611bef8d94c8436bb3ab34639c3c4a63 -8505272618868443090
* contact_sales
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* how_to_get_started
    - action_default_fallback
    - event_rewind
* enter_data{"number": 1}
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "yeetboi"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "ui bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data{"name": "sam"}
    - action_store_name
    - slot{"person_name": "sam"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "pigeon"}
    - utter_ask_businessmail
* enter_data{"email": "pigeo@yeet.tt"}
    - slot{"email": "pigeo@yeet.tt"}
    - action_store_email
    - slot{"email": "pigeo@yeet.tt"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp

## Generated Story goal:chitchat, id:910627904d75440a96dd1b9cb6e5f07f 3483683702425772116
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_builder
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:6bb9b78cbf314871ade17e6683ff8254 1703463696223417944
* out_of_scope
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - event_rewind
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
* greet
    - utter_tryout

## Generated Story goal:1 step, id:5b546da9203f41c5b9583ebbd0b0f6d2 8961956952959429597
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:86ea81ed7aea40518acaeb4446b055ac 1091126462443299346
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
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
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* greet
    - utter_explain_stack
    - utter_first_bot_with_rasa

## Generated Story goal:chitchat, id:fb06c4df58ac4e309595257a59580cd8 2907455319795166655
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - event_rewind
* contact_sales
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:fb06c4df58ac4e309595257a59580cd8 2907455319795166655
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* technical_question
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* out_of_scope
    - action_default_fallback
    - event_rewind
* contact_sales
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:9e4d2d8aaf984e4dad330c5fe1035690 -7453740906946405582
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
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:d6a2e0ea362947a4947434c0f9ac6a7d 8359890351414886109
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
    - utter_quickstart
    - utter_anything_else
* enter_data
    - action_default_fallback
    - event_rewind
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:f39db309bee847b49fe7003347d35cde -333375805818234002
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_default_fallback
    - event_rewind
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## Generated Story goal:oos, id:b005e866d34941568797b93ef7b2ace1 -7828816354812164083
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before

## Generated Story goal:oos, id:55cd82730f964d91a90d0a32f74cce0a 719841707429005250
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* mood_confirm
    - utter_thumbsup
* how_to_get_started
    - action_default_fallback
    - event_rewind
* enter_data
    - action_store_name
    - slot{"person_name": "chatbot"}
    - utter_ask_company
* mood_confirm
    - action_store_company
    - slot{"company_name": "why"}
    - utter_ask_businessmail
* mood_confirm
    - utter_great
    - utter_great
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:1 step, id:637434d0b0a94946bd50c8d9a73043f4 5743461929503497811
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else
* bye
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:0965cb4091774aef85734d4b6d0de315 8709169130179758844
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* out_of_scope
    - utter_out_of_scope
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

## Generated Story goal:1 step, id:150138f93e464145b4a077cc2db66703 -8958741670993427277
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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

## Generated Story goal:1 step, id:0c8ff265ed8148e4830edf94cc992151 -2353440429161883876
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data{"name": "sara"}
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "engineer"}
    - action_store_job
    - slot{"job_function": "engineer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "talk shopping bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 100000}
    - action_store_budget
    - slot{"budget": 100000}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "wanze"}
    - utter_ask_company
* bye
    - action_default_fallback
    - event_rewind
* bye
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data{"name": "sara"}
    - utter_possibilities
* human_handoff
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
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
* out_of_scope{"language": "chinese"}
    - slot{"language": "chinese"}
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* greet
    - action_default_fallback
    - event_rewind

## Generated Story goal:1 step, id:5cca14d56ed14870ad3a776fda9166ba 6322958258869991089
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

## Generated Story goal:1 step, id:864858e7e4954c2ba84ded9eea474e1a -3948207465971999619
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - utter_greet
* enter_data
    - utter_possibilities

## Generated Story goal:1 step, id:ecf67ea99f56437ca8a517f7fc981783 8232253210697895883
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Generated Story goal:1 step, id:7d1a79339f884cdda58548c6ed037d2e 7608332096802259654
* enter_data
    - utter_possibilities
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
* greet
    - utter_tryout

## Generated Story goal:1 step, id:06f5c790fd0648bf897bf613f3de93bb 1661155499008052735
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - action_default_fallback
    - event_rewind
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
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:a3a1ee0c071545948d457cc06b6732da -7945898186554378490
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
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
* thank
    - utter_noworries
    - utter_anything_else
* bye
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:1 step, id:6caa5e0488bc4dd2b60475ee4e4fb0f5 -8958741670993427277
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
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

## Generated Story goal:1 step, id:fdee58cd0c1c4714a060ef8d3df2f007 7183712999783119268
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before

## Generated Story goal:1 step, id:b894d19547a943f4839e97ed062bda92 -4427508585986333658
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* enter_data
    - action_default_fallback
    - event_rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* mood_confirm
    - utter_ask_migration
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout

## Generated Story goal:1 step, id:8c7ce1d3b2d0463cb748c7663e606d61 7586910295361454172
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* greet
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## Generated Story goal:1 step, id:7ce34a049c864f519a62700dcd3a72a8 -1754693312557091885
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_howdoing
    - action_chitchat
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else

## Generated Story goal:1 step, id:a3ded79809224dc5b7b8e072cdb45a9e -6322570846449902800
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
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

## Generated Story goal:suggestion, id:3540fa81942d478f80b0ae84a653efd5 -7803291517410501787
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: ask_whatspossible
    - form: suggestion_form
    - slot{"suggestion": "what can you do"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:2b0377ccea644fe883d40b36b2548a50 2596969016449473789
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "hello"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:suggestion, id:d8655ef211704160802bbfbac6d0ed98 -8453634618662847960
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "hello"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:a3f14a5feed140ef91a97f8cd5fcbbbc -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:f6f457a64b4744f0867ecfdf9b0639a5 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:0e4ea15355a54b99a2d5f1b02fde6a93 -3308369119183290776
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: out_of_scope
    - form: suggestion_form
    - slot{"suggestion": "do you know about lowcode ?"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_default_fallback
    - event_rewind
* out_of_scope
    - suggestion_form
    - slot{"suggestion": "you're dumb"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:afff261a99f54beeb4ab66ecc2c65898 201431246813901462
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: mood_confirm
    - form: suggestion_form
    - slot{"suggestion": "ok"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:b68afdc546134a28845f72591062bef1 -268011429153802369
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: ask_howdoing
    - form: suggestion_form
    - slot{"suggestion": "How are you, sara?"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_whoisit
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* technical_question
    - utter_contact_email
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* ask_howdoing
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:suggestion, id:37b10f1129914193891c535a56eb4520 -8453634618662847960
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "hello"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:9c618a99605d4ba6ad5d86c4ee89a9a2 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:a754b2faaa87491eb266c6f8c0d63ca5 1844389941356085282
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: greet
    - form: suggestion_form
    - slot{"suggestion": "cheer  me up"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_default_fallback
    - event_rewind
* enter_data
    - suggestion_form
    - slot{"suggestion": "smile"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story goal:suggestion, id:297bdc280ea246f0964891eccfc905a7 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:298107610b264b9bab8f12818c2fec5f -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:a6b0efd5dae042efb4f1527d9a5f2fff 151307185002112964
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}
* form: enter_data
    - form: suggestion_form
    - slot{"suggestion": "\u6211\u7231\u5317\u4eac"}
    - form{"name": null}
    - slot{"requested_slot": null}
* enter_data
    - action_store_email
    - event_rewind
* enter_data
    - action_store_email
    - event_rewind

## Generated Story goal:suggestion, id:2bcde084c26c4806b5daac777efa1a0c -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:suggestion, id:d9c060bbe28d458795271eb00aafc343 -8566049040987755299
* suggestion
    - utter_greet
    - utter_suggestion
    - suggestion_form
    - form{"name": "suggestion_form"}
    - slot{"requested_slot": "suggestion"}

## Generated Story goal:sales, id:14806816b3bb4a01a3be69f557cfcf9b -8858440635568394693
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "boss"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "soldier"}
    - utter_thank_usecase
    - utter_ask_budget
* mood_confirm{"name": "Very Big"}
    - action_default_fallback
    - event_rewind
* enter_data{"name": "Big Budget"}
    - action_store_budget
    - slot{"budget": "Very Big Budget"}
    - utter_sales_contact
    - utter_ask_name
* out_of_scope
    - action_default_fallback
    - event_rewind
* enter_data
    - action_store_name
    - slot{"person_name": "I am Me"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Government"}
    - utter_ask_businessmail
* enter_data{"email": "me@private.gov"}
    - slot{"email": "me@private.gov"}
    - action_store_email
    - slot{"email": "me@private.gov"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_great
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* enter_data
    - action_store_bot_language
    - slot{"language": "that language"}
    - slot{"can_use_spacy": false}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data
    - action_default_fallback
    - event_rewind

## Generated Story goal:oos, id:b5e755fbe8a642629bdd033a26b44ef0 3975814311615056907
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:signup, id:e048f0f2a37a4be9a74cad836772248b 4463018865749181992
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
    - utter_ask_feedback
* out_of_scope
    - action_default_fallback
    - event_rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:rasa_help, id:6b7b736c03ae41feac79cd01d2fce02b 4292740991537278046
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - event_rewind
* mood_confirm
    - utter_thumbsup
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - event_rewind
* technical_question
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:sales, id:03d9b6b4a0514a9ab38dcf11093b48fa 2948880294589921443
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* human_handoff
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "designer"}
    - action_store_job
    - slot{"job_function": "designer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "goal oriented"}
    - utter_thank_usecase
    - utter_ask_budget
* contact_sales
    - action_default_fallback
    - event_rewind
* ask_builder
    - action_chitchat
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 10}
    - action_store_budget
    - slot{"budget": 10}
    - utter_sales_contact
    - utter_ask_name
* deny
    - utter_nohelp
* enter_data
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction

## Generated Story goal:rasa_help, id:1a1e9c9ac8e9420bb001af17025ffe4f 6911663837891690917
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data
    - action_store_bot_language
    - slot{"language": "that language"}
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:chitchat, id:59a654701d284d08a6bb2e5591617876 7574401130023926272
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:oos, id:1c644e761eb140628c1a645bbdc17f47 7548330955375630748
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal

## Generated Story goal:signup, id:ed20845e0530453dbc0a6588357af715 -2702472658507410712
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "alsls@anthem.com"}
    - slot{"email": "alsls@anthem.com"}
    - action_store_email
    - slot{"email": "alsls@anthem.com"}
    - action_subscribe_newsletter
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail
    - utter_docu
    - utter_ask_feedback

## Generated Story goal:oos, id:c1e876ea97ad460a9c29963e20875922 7915395410086866049
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities

## Generated Story goal:oos, id:b9230d081df3413db9b5c101ff3d83f0 5873933706324771993
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal

## Generated Story goal:chithcat, id:c377f426f543424c880029bc6841c178 -8586104615159816494
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_isbot
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* ask_whoisit
    - action_chitchat

## Generated Story goal:oos, id:05d927542b284dc9871f246029ea814c 4496863020738867723
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
* enter_data
    - utter_getstarted
    - utter_first_bot_with_rasa
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - utter_greet

## Generated Story goal:chitchat, id:4e340a531b3944208e6f993ca3c80e28 -2878792886660069271
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:sales, id:5c41f99aeeb94c4281e46855eaa398df 2078458553945923070
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_isbot
    - action_chitchat
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "i clean space toilets"}
    - utter_ask_usecase
* enter_data{"number": 1}
    - action_default_fallback
    - event_rewind
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
* enter_data
    - action_default_fallback
    - event_rewind

## Generated Story goal:signup, id:5b67655b1dbb4429b0096ba62fd96d90 -4954657822558321243
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data
    - action_store_email
    - event_rewind
* out_of_scope
    - action_default_fallback
    - event_rewind
* bye
    - action_store_email
    - event_rewind
* bye
    - action_store_email
    - event_rewind

## Generated Story goal:oos , id:3fe006cd184e45b6be842b45d94eef21 -880929751402420714
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* ask_whatisrasa
    - action_default_fallback
    - event_rewind

## Generated Story goal:other, id:6f7e747466fa413190a22c25c4767a0a 3092403914152802984
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## Generated Story goal:other, id:307afc3749b248929c429a49850ea2a4 337772325179164178
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* ask_howdoing
    - action_default_fallback
    - event_rewind
* enter_data{"language": "english"}
    - slot{"language": "english"}
    - action_default_fallback
    - event_rewind
* out_of_scope{"language": "french"}
    - slot{"language": "french"}
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:other, id:da7738dcdf47434199593b879f98fcee 4742354566058284251
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
    - utter_ask_goal

## Generated Story goal:other, id:6fb7c1bc901349aa93d975afc1e3b721 6901718858589713494
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:other, id:a19457735b3c4fb6a4e21f18fd447b57 8685252419251766669
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatisrasa
    - action_chitchat
    - utter_ask_goal

## Generated Story goal:other, id:e8f4b09e5d0f4bfda460fb9bd6b7b380 2681982339449711367
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:other, id:ccf4eb721cbd4ef192735a8a1f3e35c2 551087610883986355
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data
    - action_store_job
    - slot{"job_function": "QA"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "educational"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 0}
    - action_store_budget
    - slot{"budget": "0"}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Faith"}
    - utter_ask_company
* enter_data{"name": "Tezza"}
    - action_store_company
    - slot{"company_name": "Tezza Business Solutions"}
    - utter_ask_businessmail
* enter_data{"email": "faith.kangichu@tezzasolutions.com"}
    - slot{"email": "faith.kangichu@tezzasolutions.com"}
    - action_store_email
    - slot{"email": "faith.kangichu@tezzasolutions.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* signup_newsletter
    - utter_great
    - utter_ask_email
* out_of_scope
    - action_default_fallback
    - event_rewind
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else

## Generated Story goal:other, id:834969104fef4ba6b5286fcfa7b3bb2d -1610529620802613734
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities

## Generated Story goal:other, id:015e3fdbf4384982a4fb83a150b30287 8854941946432854731
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* greet
    - action_chitchat

## Generated Story goal:other, id:4e184785387041f8908db3c633e2774c -1276756175749411584
* enter_data
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "enginer"}
    - action_store_job
    - slot{"job_function": "enginer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "it"}
    - utter_thank_usecase
    - utter_ask_budget
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal

## Generated Story goal:other, id:a2c708c4e4d54b458485d8e516e7f681 4744019118843106339
* enter_data
    - utter_possibilities

## Generated Story goal:other, id:820bb0bbd8cd4390a8ebe5c00e0485d7 1317782767465542934
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_chitchat

## Generated Story goal:other, id:d59b028d90c74e0096c36ed6d4206024 -3684213327778739610
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet

## Generated Story goal:other, id:a6eef7a7d68b43d9a7bea5ae4ed45b2a 3961679617377316029
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - event_rewind

## Generated Story goal:other, id:[Interactive Learning] 1bc3f920-f225-11e8-8a59-8fc855eba32c -4243677523515256203
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - utter_ask_budget

## Generated Story goal:other, id:bc77bf060a714e638926252a47506dec -3684213327778739610
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet

## Generated Story goal:other, id:[Interactive Learning] fe251e30-f224-11e8-8a59-8fc855eba32c 3543416627907431243
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "AI engieer"}
    - action_store_job
    - slot{"job_function": "AI engieer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "customer service bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 6000000}
    - action_store_budget
    - slot{"budget": 6000000}
    - utter_sales_contact
    - utter_ask_name
* out_of_scope

## Generated Story goal:other, id:b4f2114734b24179804cd56c2ea677d2 1364127346520211592
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities

## Generated Story goal:other, id:9be93ba64d4142298be95cfd0b617aad -6724554839931216891
* enter_data
    - utter_possibilities
* ask_whatisrasa
    - action_chitchat
* ask_whatisrasa
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat
* ask_whatisrasa
    - action_default_fallback
    - event_rewind

## Generated Story goal:other, id:542a4150a2d24e56959d01559d41790b -4729525068991848806
* mood_confirm
    - utter_thumbsup

## Generated Story goal:other, id:[Interactive Learning] 4b7dddf0-f222-11e8-8a59-8fc855eba32c -9154805483533917822
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "AI engieer"}
    - action_store_job
    - slot{"job_function": "AI engieer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "customer service bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 6000000}
    - action_store_budget
    - slot{"budget": 6000000}
    - utter_sales_contact
    - utter_ask_name
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:other, id:50cb078e35cf4d92904a23b645f05221 -7196473446182282603
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* signup_newsletter
    - utter_great
    - utter_ask_email

## Generated Story goal:other, id:12f9da33da884c439a96cf1767f2dc50 6041019239708959807
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* contact_sales
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities

## Generated Story goal:other, id:[Interactive Learning] c3ae3ef0-f21d-11e8-8a59-8fc855eba32c -2336210443530326887
* greet
    - utter_greet
    - utter_inform_privacypolicy

## Generated Story goal:other, id:[Interactive Learning] a7db7170-f21d-11e8-8a59-8fc855eba32c -9154805483533917822
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "AI engieer"}
    - action_store_job
    - slot{"job_function": "AI engieer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "customer service bot"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"number": 6000000}
    - action_store_budget
    - slot{"budget": 6000000}
    - utter_sales_contact
    - utter_ask_name
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:other, id:824b11e108204f328dd32b1da22f42bc -7159725659265099190
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
* greet{"name": "sara"}
    - utter_greet
* enter_data
    - utter_possibilities

## Generated Story goal:other, id:35262206aafa4738b4138f099d8a4fbc 7339215050501037556
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* greet
    - utter_greet

## Generated Story goal:other, id:75da10afff23437d9d1f3778d1b27b25 4321276287908638663
* greet
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat

## Generated Story goal:other, id:90a1145585c24069abb834483e4aaf61 8988195740072355248
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## Generated Story goal:other, id:e89425d2be38404c946f18650bf2bee4 -1226267625474711300
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal

## Generated Story goal:other, id:e82b739c087f4126a1efadbe756dea82 -1332767191189858903
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* deny
    - action_default_fallback
    - event_rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data
    - action_store_email
    - event_rewind
* deny
    - utter_cantsignup
* ask_isbot
    - action_default_fallback
    - event_rewind
* ask_isbot
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback
    - event_rewind
* ask_whatspossible
    - action_chitchat

## Generated Story goal:other, id:a6ed78075675447db8806d9ce072d73c 6627085675043129918
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data{"number": 5002}
    - utter_possibilities

