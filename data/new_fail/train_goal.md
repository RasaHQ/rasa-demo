## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - getstarted_1_success: action_default_fallback
    - rewind
* how_to_get_started
    - getstarted_1_success: utter_quickstart_nlu_only -> fail
    - getstarted_1: utter_anything_else
* enter_data
    - fallback: action_default_fallback
    - rewind
* enter_data
    - fallback: action_default_fallback
    - rewind

## Generated Story goal:oos, id:697db34a22db4c089e85f2c9ae3ee88f, 05/01/19 8439639792622345614
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: action_default_ask_affirmation

## Generated Story goal:chitchat, id:ada5f58b5ea4436fb1993578ca7fc805, 12/15/18 8327066330043087187
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_weather{"name": "New York"}
    - slot{"name": "New York"}
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:4f647cb2427c495dbff5cf6fa1d7feb9, 12/15/18 -1171376024735749581
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_greet_user -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_anything_else -> fail
* affirm
    - chitchat: utter_quickstart  -> fail
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:99ca2d48ec6b4563a09b13303f4b6960, 12/17/18 4281123642591350586
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted -> fail
    - onboarding: utter_first_bot_with_rasa -> fail
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* telljoke
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore -> fail

## Generated Story goal:chitchat, id:debe18e2325840aeb5313ad18a27fa42, 05/01/19 1747852281231103127
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_isbot
    - chitchat: action_chitchat
* bye
    - chitchat: utter_bye

## Generated Story goal:chitchat, id:624b61bee53b411bac4a3855343dd0c7, 12/15/18 -8806002753186605917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* out_of_scope
    - oos: action_default_fallback
    - rewind
* ask_howold
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_faq_languages
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_faq_languages
    - faq: action_faqs
* enter_data{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* enter_data
    - getstarted_1: action_chitchat -> fail
    - getstarted_1: utter_ask_migration
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation

## Generated Story goal:chitchat, id:455210c2c7c9471194a7faaf2e63579f, 12/15/18 7957735631208973079
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: action_default_fallback
    - rewind
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* ask_isbot
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* ask_faq_platform
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_platform
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: action_default_ask_affirmation
* affirm
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:2f822433f6a9427c8bff569c676d824e, 12/15/18 -6375541493127917237
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* handleinsult
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* ask_whoisit
    - chitchat: action_chitchat

## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - oos: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* install_rasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:chitchat, id:0f8142515810483a8c2e777909c37c2c, 12/17/18 -8573563216604908022
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_select_installation_command -> fail
    - getstarted_3: utter_ask_ready_to_build -> fail
* enter_data
    - getstarted_3: action_store_problem_description -> fail
    - slot{"problem_description": "i have installed rasa_core"}
    - getstarted_3_success: utter_direct_to_forum_for_help -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* affirm
    - chitchat: utter_thumbsup
    - getstarted_1: action_listen -> fail
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - rasa_help: utter_core_tutorial
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:db1d15d9e40047ebb3e8c13bbd0810b3, 12/15/18 2742610268326907746
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore

## Generated Story goal:3 step, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_what_help
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* affirm
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_select_installation_command -> fail
    - getstarted_3: utter_ask_ready_to_build -> fail
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user -> fail
    - chitchat: action_listen -> fail
* bye
    - chitchat: action_default_fallback
    - rewind
* technical_question
    - faq: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_greet_user -> fail
    - getstarted_1: utter_stack_details -> fail
    - utter_anything_else -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: action_default_fallback
    - rewind
* enter_data
    - getstarted_1: action_default_fallback
    - rewind
* bye
    - chitchat: utter_bye
* nlu_info
    - rasa_help: action_default_fallback
    - rewind
* deny
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916, 12/15/18 -5644677460292251299
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: utter_ask_migration -> fail
* enter_data
    - getstarted_1: utter_contact_email
* ask_howdoing
    - chitchat: action_default_ask_affirmation
* telljoke
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* react_negative
    - chitchat: action_default_ask_affirmation
* ask_faq_channels
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_faq_channels
    - faq: action_faqs
* technical_question
    - faq: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* ask_whatspossible
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:e14eddaf8dc14ff7bb8104696c4eb1d2, 05/01/19 7896940127074527179
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_whatisrasa
    - chitchat: action_chitchat

## Generated Story goal:chitchat, id:94f6b465ee3e4a9297dcf1ed5ed22c27, 12/17/18 -2986161335647465616
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:cfa8bb9deaf0427498c662745431a282, 12/15/18 -56217783078242536
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_greet_user -> fail
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* deny
    - chitchat: utter_nohelp
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:16439d767388463d93e9c827767bca96, 05/01/19 -5426994757726665781
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* greet
    - greet_success: action_greet_user

## Generated Story goal:chitchat, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_what_help
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Generated Story goal:chitchat, id:9e785c9f586b48b7affc592dd2d499fb, 12/17/18 8538685554217994801
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities

## Generated Story goal:oos , id:5a1c8e47b3ba4dc38b2a3de3ffedee30, 12/17/18 4221492392327213787
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_whoisit
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup -> fail
    - rasa_help: action_listen -> fail
* ask_whatspossible
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:fe9205767e5540319511248ba2d7aa7d, 12/15/18 -1169614020695031757
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user -> fail

## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c, 12/15/18 4546830120439352871
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"name": "sara"}
    - slot{"name": "sara"}
    - getstarted_1: action_default_fallback
    - rewind
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started
    - getstarted_1: action_chitchat -> fail
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_nlu  -> fail
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_whatspossible
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities

## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_store_email
    - rewind
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - fallback: action_store_email
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_default_fallback
    - rewind
* deny
    - chitchat: utter_great
    - chitchat: utter_anything_else
* ask_wherefrom
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_fallback
    - rewind
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat: utter_anything_else
* handleinsult
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:c1712b9b83444c4d950fb1d0c06ee81e, 05/01/19 -4543793503788733794
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - chitchat: utter_thumbsup
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_store_email
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* greet
    - greet_success: action_default_ask_affirmation
* ask_restaurant
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_restaurant
    - chitchat: action_chitchat
* affirm
    - chitchat: action_default_fallback
    - rewind
* out_of_scope
    - oos: action_default_fallback
    - rewind
* deny
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* deny
    - chitchat: action_default_fallback
    - rewind
* greet
    - greet_success: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* canthelp
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: action_default_fallback
    - rewind
* signup_newsletter
    - subscribe: utter_great
    - subscribe: action_listen
* out_of_scope
    - oos: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_ask_name -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - chitchat: utter_spacy_or_tensorflow -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - chitchat: utter_spacy_or_tensorflow -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_spacy_or_tensorflow -> fail
    - chitchat: utter_anything_else -> fail
* signup_newsletter
    - subscribe: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* canthelp
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* canthelp
    - chitchat: utter_canthelp
* bye
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* bye
    - chitchat: action_default_fallback
    - rewind
* greet
    - greet_success: action_greet_user
* bye
    - chitchat: utter_ask_company -> fail
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - sales: action_store_company -> fail
    - slot{"company_name": "google"}
    - sales: utter_ask_businessmail -> fail
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - sales: action_store_email -> fail
    - slot{"email": "arvind@google.com"}
    - sales: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - sales: utter_awesome -> fail
    - sales_success: utter_confirmationemail -> fail
    - sales: utter_docu -> fail
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_thumbsup -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_thumbsup -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_anything_else -> fail
    - chitchat: action_listen -> fail
* thank
    - chitchat: utter_anything_else -> fail
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_get_community_events -> fail
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_faqs
* greet
    - greet_success: action_default_fallback
    - rewind
* ask_howold
    - chitchat: action_default_ask_affirmation
* ask_howold
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_howold
    - chitchat: action_default_fallback
    - rewind
* ask_howold
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - chitchat: action_store_unknown_nlu_part -> fail
    - slot{"unknown_nlu_part": "nopes"}
    - chitchat: action_store_unknown_nlu_part -> fail
    - slot{"unknown_nlu_part": "nopes"}
    - chitchat: utter_dont_know_nlu_part -> fail
    - chitchat: utter_duckling -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_switch_dialogflow -> fail
    - chitchat: utter_anything_else -> fail
* ask_weather
    - chitchat: action_default_ask_affirmation
* ask_languagesbot
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_languagesbot
    - chitchat: utter_switch_dialogflow -> fail
    - chitchat: utter_anything_else -> fail

## Generated Story goal:1 step, id:c1413213af684cbd952299e5b640a174, 12/15/18 5367922669514830768
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* technical_question
    - faq: action_default_fallback
    - rewind
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:chitchat, id:7daa8ec84bbe48a6a154517eacd06560, 12/15/18 737373360707803542
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_opensource
    - faq: action_faqs

## Generated Story goal:1 step, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_what_help
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa

## Generated Story goal:1 step, id:3b58d04997b343dca11db2d8b09d5f56, 12/17/18 -5919216385967754526
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_faqs
    - getstarted_1_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - rasa_help: action_store_unknown_nlu_part
    - slot{"unknown_nlu_part": "classification"}
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else

## Generated Story goal:FAQ, id:3ae94172c7864fb59ab78db2334db86c, 05/01/19 2833611311799497832
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_core_tutorial
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user

## Generated Story goal:sales, id:d89912f620b6495d9cf2ff3d71176375, 05/01/19 -8922460127438793877
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* out_of_scope
    - oos: utter_out_of_scope
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "asd"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "asdas"}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data
    - sales: action_store_budget
    - slot{"budget": "sdfsd"}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "saaf"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name": "asfadf"}
    - sales: utter_ask_businessmail
* enter_data
    - sales: action_store_email
    - rewind
* enter_data
    - sales: action_store_email
    - rewind
* enter_data
    - sales: action_store_email
    - rewind
* enter_data{"email": "a.b@c.com"}
    - slot{"email": "a.b@c.com"}
    - sales: action_store_email
    - slot{"email": "a.b@c.com"}
    - sales: action_store_sales_info
    - slot{"data_stored": true}
    - sales_success: utter_confirm_salesrequest
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - feedback_success: utter_thumbsup
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:7c9b8897dcbe4b46af67aa5b2290dc4f, 12/17/18 -1844283597923529811
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: action_store_unknown_product
    - slot{"unknown_product": "hubot"}
    - getstarted_1_success: utter_no_guide_for_switch
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
* ask_time
    - chitchat: action_chitchat
* telljoke{"user_type": "new"}
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities

## Generated Story goal:chitchat, id:ed1418fcc3884157bcc96a7c43d21ec0, 12/15/18 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Generated Story goal:1 step, id:321d95bf0cb14dc8b09f3f9a62827081, 12/15/18 6069986032596098095
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: action_default_fallback
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1_fail: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1_success: utter_core_tutorial
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:618cb7db283a4c0ea000cd60e198e6b0, 05/01/19 -391894298907133881
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* deny
    - chitchat: utter_ask_if_problem
* deny
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_ask_describe_problem
* enter_data
    - chitchat: action_default_ask_affirmation
* greet
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* greet
    - greet_success: action_default_fallback
    - rewind
* affirm
    - chitchat: action_store_problem_description
    - slot{"problem_description": "yes"}
    - chitchat_fail: action_faqs
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* affirm
    - chitchat: action_default_ask_affirmation
* telljoke
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* telljoke
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user

## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* enter_data
    - chitchat: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* nlu_generation_tool_recommendation
    - rasa_help: utter_already_subscribed
* nlu_generation_tool_recommendation
    - rasa_help: action_default_fallback
    - rewind
* nlu_generation_tool_recommendation
    - rasa_help: action_default_fallback
    - rewind
* greet
    - greet_success: action_store_problem_description
    - slot{"problem_description": "Hello"}
    - greet_fail: action_faqs
* ask_whoisit
    - chitchat: action_chitchat
* nlu_generation_tool_recommendation
    - rasa_help: action_default_fallback
    - rewind
* nlu_generation_tool_recommendation{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: action_default_fallback
    - rewind
* nlu_generation_tool_recommendation
    - rasa_help: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: action_faqs
    - getstarted_1_fail: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* how_to_get_started
    - getstarted_1: utter_ask_which_tool
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* nlu_generation_tool_recommendation
    - rasa_help_success: utter_nlu_tools

## Generated Story goal:1 step, id:cdd14d763a664a5b95e998ce165bd86f, 12/15/18 5883009647019170057
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: action_listen

## Generated Story goal:subscribe, id:ee59175ac0a64f468b1b4559296f359a, 12/17/18 7101882852510041551
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "blah"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "chat "}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": 1}
    - sales: action_store_budget
    - slot{"budget": 1}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "bi"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name": "q"}
    - sales: utter_ask_businessmail
* enter_data
    - sales: action_store_email
    - rewind
* enter_data
    - sales: action_store_email
    - rewind
* bye
    - sales_fail: utter_bye

## Generated Story goal:1 step, id:dab1fc88af214c1abb57334f72b8cfb2, 12/17/18 1502159966905958231
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: action_default_ask_affirmation
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* switch{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:3 step, id:49e29935e38740429d10ae50045b11a6, 12/15/18 -1571430978479800820
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* ask_faq_differencecorenlu
    - faq: action_select_installation_command
    - faq_fail: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "i'm sad"}
    - getstarted_3_success: utter_direct_to_forum_for_help

## Generated Story goal:1 step, id:2de75b1f7d17449a8e8a6e481f6d14bd, 05/01/19 8262034575362695580
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* deny
    - chitchat: action_default_ask_affirmation

## Generated Story goal:faq, id:1b9d609211b74674844d925461b24744, 12/15/18 -4573659050616064820
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_faq_voice
    - faq: action_faqs
* affirm
    - chitchat: utter_thumbsup

## Generated Story goal:1 step, id:318f6636b6c842f6a330b015599e8f7d, 05/01/19 -2612547548431379099
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data{"number": 1}
    - chitchat: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: action_faqs
    - chitchat_fail: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1_fail: utter_explain_core
    - getstarted_1: utter_tryout
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* ask_howdoing
    - chitchat: action_default_ask_affirmation

## Generated Story goal:1 step, id:2d42a9856ff545b5a1705e76aa2024ce, 12/17/18 -3109717157276131254
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:92128e5e2ea74967876544a30c37b41a, 12/15/18 7589135915048511041
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:33a2877c49944765a102c0a215632b8a, 12/15/18 3487883399882115987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_builder
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* how_to_get_started
    - fallback: action_default_ask_affirmation
* technical_question
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* technical_question
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:oos, id:c750b33383004b0da4da73284fe9fa48, 12/15/18 9035562821004117390
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat

## Generated Story goal:chitchat, id:1277dc2ceae04fe0b963c7786a41f750, 05/01/19 806262383242887293
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* ask_time
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_time
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat

## Generated Story goal:chitchat, id:bbf4baacf5e34a358eaaa875721bdf5b, 12/15/18 4017343442768204250
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* handleinsult
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat

## Generated Story goal:1 step , id:7146d879adc44cf5947ffe723015f02a, 12/15/18 7977723706233268217
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "done"}
    - getstarted_3_success: utter_direct_to_forum_for_help
* affirm
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1_fail: utter_core_tutorial
    - chitchat: utter_anything_else
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* greet
    - greet_success: action_default_fallback
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
    - subscribe: utter_ask_email
* signup_newsletter
    - subscribe_success: utter_already_subscribed
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:9978f875abec4c3c9955ec3d5dae51b1, 12/15/18 1526679696595893973
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core
* enter_data{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - chitchat: utter_tryout
    - chitchat_fail: action_listen
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart
    - getstarted_1_fail: utter_anything_else

## Generated Story goal:1 step, id:decd65b902e148baac9a1e373c056474, 12/17/18 2076418664202927492
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart
    - getstarted_1_fail: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:chitchat, id:bc6723f023be41cb9516b53781448272, 12/15/18 6369486256094570096
* get_started_step2
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:ad02fffc3bd841788f5b10e283fe2ab8, 12/17/18 7345417199532554495
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_faqs
    - getstarted_1_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* affirm
    - rasa_help: utter_ask_migration
* deny
    - rasa_help: utter_explain_stack
    - rasa_help: utter_stack_details
    - rasa_help: utter_explain_nlucore
* affirm
    - rasa_help: utter_explain_nlu
    - rasa_help: utter_also_explain_core
* affirm
    - rasa_help: utter_tryout
* enter_data
    - chitchat: action_store_email
    - rewind
* affirm
    - rasa_help: action_faqs
    - rasa_help_fail: utter_tryout
* enter_data{"email": "urandombg@abv.bg"}
    - slot{"email": "urandombg@abv.bg"}
    - subscribe: action_store_email
    - slot{"email": "urandombg@abv.bg"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - chitchat: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat_fail: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat_fail: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat_fail: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else

## Generated Story goal:1 step, id:5458e9cbe0be44a589ad3c8b89d77642, 12/17/18 -981377364561820576
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* technical_question
    - faq: action_store_problem_description
    - slot{"problem_description": "How Rasa works?"}
    - faq_success: utter_direct_to_forum_for_help
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* enter_data{"number": 9}
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* greet
    - greet_success: action_store_problem_description
    - slot{"problem_description": "hello"}
    - greet_fail: action_faqs
* affirm
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny{"email": "no@nonono.no"}
    - slot{"email": "no@nonono.no"}
    - subscribe: action_store_email
    - slot{"email": "no@nonono.no"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - chitchat: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* greet
    - greet_success: action_greet_user

## Generated Story goal:sales, id:e1ae1d77ce414451966eae0e29478965, 12/15/18 5656589108300468794
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_fallback
    - rewind
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "it"}
    - sales: utter_ask_usecase
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - chitchat: action_default_fallback
    - rewind
* affirm
    - chitchat: action_default_fallback
    - rewind

## Generated Story goal:1 step, id:269eec083b394990820028bb4ef61d01, 12/17/18 -7615535506954100338
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:2a075ca47bd942e29e99c10ef9b2533a, 12/17/18 -6381151701767496471
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp
* source_code
    - faq: utter_source_code
    - chitchat: utter_anything_else

## Generated Story goal:1 step, id:320e02b044fe472389b0e486833aab2c, 12/17/18 5108855124096892797
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* out_of_scope
    - oos: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase

## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - getstarted_3: action_faqs
    - getstarted_3_fail: utter_explain_nlucore
* how_to_get_started
    - getstarted_1: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* out_of_scope
    - fallback: action_default_ask_affirmation
* greet
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* greet
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* greet
    - greet_success: action_greet_user
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
* technical_question
    - faq: action_greet_user
    - faq_fail: action_listen
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* enter_data
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: greet
    - form: feedback: feedback_form
    - slot{"feedback_message": "hi"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* how_to_get_started
    - fallback: action_default_ask_affirmation
* how_to_get_started{"user_type": "new"}
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* install_rasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* technical_question
    - faq: action_store_problem_description
    - slot{"problem_description": "error syntax"}
    - faq_success: utter_direct_to_forum_for_help
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - getstarted_3_fail: utter_duckling
    - getstarted_3_fail: utter_anything_else
* install_rasa
    - getstarted_3: action_store_budget
    - slot{"budget": "i need to install in my computer"}
    - getstarted_3_fail: utter_sales_contact
* install_rasa
    - getstarted_3: action_faqs
* install_rasa
    - getstarted_3_fail: action_default_fallback
    - rewind
* greet
    - greet_success: action_store_budget
    - slot{"budget": "hello"}
    - greet_fail: utter_quickstart_nlu_only
    - greet_fail: utter_quickstart
    - greet_fail: utter_direct_install
    - greet_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: action_default_ask_affirmation
* install_rasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* install_rasa
    - getstarted_3: utter_quickstart_nlu_only
    - getstarted_3_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - onboarding_fail: utter_thumbsup
* ask_howdoing
    - chitchat: action_chitchat
* ask_how_contribute
    - getstarted_4: utter_not_sure
    - getstarted_4_fail: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else
* ask_whatisrasa
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:1bc7a86220da42588b30b2a5566b00dc, 12/17/18 940448344067621014
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_getstarted
    - chitchat_fail: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - getstarted_1: utter_great
    - getstarted_1_fail: utter_ask_email
* enter_data{"email": "f.madureira@gmail.com"}
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_store_email
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": true}
    - subscribe: utter_awesome
    - subscribe_success: utter_confirmationemail
    - subscribe: utter_docu
    - feedback: utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_great
    - chitchat: utter_anything_else
* enter_data
    - chitchat: utter_great
    - chitchat: utter_spacy_or_tensorflow
    - chitchat_fail: utter_anything_else

## Generated Story goal:1 step, id:6baa606f62c54e888053bcbc934eff8d, 05/01/19 6925132852772246229
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:8d69c4b1d6db489789fe20e2bbeec153, 12/15/18 -7810778017142759063
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_getstarted_new
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:35dc087ff6084dc087a9b5d1fda96d60, 12/17/18 5905188858882087469
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - getstarted_1: utter_ask_which_product
    - getstarted_1_fail: action_listen
* affirm
    - chitchat: utter_thumbsup
    - chitchat_fail: action_listen

## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* ask_whoisit
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_whoisit
    - chitchat: action_chitchat
* ask_why_contribute
    - getstarted_4: action_default_ask_affirmation
* enter_data
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* canthelp
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* canthelp
    - chitchat: utter_canthelp

## Generated Story goal:1 step, id:8f756ee8a18e4f658946110f224aeb78, 05/01/19 -2911689985886478407
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_also_explain_core

## Generated Story goal:faq, id:b7c01a1b3b034a59b74a25e4ffd94b12, 12/15/18 1531624798006099569
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_builder
    - chitchat: action_default_fallback
    - rewind
* ask_faq_languages
    - faq: action_faqs

## Generated Story goal:1 step, id:8bfddbb9e63f47a5b1da9fd4f46a521e, 05/01/19 4337175060932118406
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_weather
    - chitchat: action_chitchat
* enter_data{"name": "Hanoi Vietnam"}
    - slot{"name": "Hanoi Vietnam"}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:chitchat, id:2721ae89d30d4c28964ac367c2e553ed, 12/15/18 -3646576092582365265
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_time
    - chitchat: action_chitchat
* source_code
    - faq: utter_source_code
    - chitchat: utter_anything_else

## Generated Story goal:chitchat, id:912897e570334aa0bf5360977052e95b, 12/17/18 -1934419123625089053
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* deny
    - chitchat: utter_nohelp
* human_handoff
    - handoff: action_default_ask_affirmation
* human_handoff
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* human_handoff
    - handoff: utter_contact_email
* deny
    - chitchat: utter_nohelp
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities

## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - faq: utter_not_sure
    - faq_fail: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: how_to_get_started
    - form: feedback: feedback_form
    - slot{"feedback_message": "teach me nlp"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_isbot
    - fallback: action_default_ask_affirmation
* ask_isbot
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_isbot
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: action_chitchat
    - getstarted_1: utter_built_bot_before
* enter_data
    - chitchat: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* thank
    - chitchat: action_default_ask_affirmation
* bye
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_time
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* ask_why_contribute
    - getstarted_4_success: utter_reasons_to_contribute
* handleinsult
    - chitchat: action_default_ask_affirmation
* handleinsult
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart

## Generated Story goal:chitchat, id:67a8696eb5894b25a800b6cbd7a695bb, 12/15/18 -1322664348979395741
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* ask_faq_languages
    - faq: action_store_problem_description
    - slot{"problem_description": "what languages do you support?"}
    - faq_fail: action_faqs
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* enter_data
    - chitchat: action_store_problem_description
    - slot{"problem_description": "ofcouse"}
    - chitchat_fail: utter_direct_to_forum_for_help
* affirm
    - chitchat: utter_anything_else
* handleinsult
    - chitchat: action_default_fallback
    - rewind
* deny
    - chitchat: utter_nohelp
* out_of_scope
    - oos: action_default_fallback
    - rewind
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:2979714d45bc445e9d7241fdc3ad64c1, 12/15/18 -3947067250872774786
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* handleinsult
    - chitchat: action_chitchat
* deny
    - chitchat: action_default_fallback
    - rewind
* handleinsult
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* enter_data
    - chitchat: action_set_onboarding
    - chitchat_fail: utter_built_bot_before
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem

## Generated Story goal:1 step, id:1cf5bff6668140a3978700059f6edb83, 12/17/18 -303270644112371083
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* enter_data
    - chitchat: utter_possibilities

## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* ask_whatisrasa
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_whatisrasa
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* ask_wherefrom
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* how_to_get_started
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:15f92cc91e4e4c86826ffd023f4d1ef7, 12/15/18 -5922610915225646491
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_select_installation_command
    - chitchat_fail: utter_ask_ready_to_build
* affirm
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "yes"}
    - getstarted_3_success: utter_direct_to_forum_for_help

## Generated Story goal:1 step, id:8affa7a6082945a09f031db186ec22eb, 12/15/18 -5307346528120334917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat

## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* ask_isbot
    - chitchat: action_default_fallback
    - rewind
* affirm
    - chitchat: utter_quickstart
    - chitchat_fail: utter_anything_else
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_possibilities
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* ask_whatisrasa
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* deny
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* deny
    - chitchat: utter_nohelp
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* thank
    - chitchat: utter_noworries
    - chitchat: utter_anything_else
* bye
    - chitchat: utter_bye
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* enter_data
    - chitchat: utter_quickstart_nlu_only
    - chitchat_fail: utter_anything_else
* affirm
    - chitchat: utter_thumbsup
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_ask_affirmation
* out_of_scope
    - fallback: action_default_ask_rephrase
* deny
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
    - rewind
* deny
    - chitchat: utter_nohelp

## Generated Story goal:1 step, id:8861ebbcdb684fb98a66f65a357d07b0, 12/15/18 -217273042631869968
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout

## Generated Story goal:1 step, id:120a458cbe094db9b49c0d2a9adca7ca, 12/15/18 -7037911620927207371
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - getstarted_1_success: utter_quickstart_nlu_only
    - getstarted_1_fail: utter_anything_else

## Generated Story goal:3 step, id:a1abb0d5bd294bb083c03f73eeb5e786, 05/01/19 -8888358178538347654
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* enter_data
    - chitchat: action_greet_user
    - chitchat_fail: action_listen
* how_to_get_started
    - getstarted_1: utter_getstarted
    - getstarted_1: utter_first_bot_with_rasa

## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_ask_affirmation
* deny
    - fallback: action_default_ask_rephrase
* ask_whatisrasa
    - fallback: action_default_ask_affirmation
* deny
    - fallback: action_default_fallback
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form: followup{"name": "feedback_form"}
    - form: feedback: feedback_form
    - slot{"requested_slot": "feedback_message"}
* form: ask_wherefrom
    - form: feedback: feedback_form
    - slot{"feedback_message": "what is your address?"}
    - form: followup{"name": "action_listen"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart
    - restart
* ask_wherefrom
    - chitchat: action_default_ask_affirmation
* ask_wherefrom
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* ask_wherefrom
    - chitchat: action_chitchat

## Generated Story goal:FAQ, id:3256c66e60aa42c7bc33f915dfa0d728, 05/01/19 -7313640270495983501
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else
* rasa_cost
    - faq: action_default_ask_affirmation
* rasa_cost
    - fallback: action_revert_fallback_events
    - rewind
    - rewind
* rasa_cost
    - faq: utter_rasa_cost
    - chitchat: utter_anything_else

## Generated Story goal:sales, id:c08c1942644d489ea1995880bf043a85, 12/15/18 8980344777735687263
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: action_default_fallback
    - rewind
* enter_data
    - chitchat: utter_possibilities
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction

## Generated Story goal:chitchat, id:8ea529575d1e471383b23c054caf3673, 12/17/18 -4775544525012944248
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - chitchat: action_default_ask_affirmation

## Generated Story goal:1 step, id:0da3c44e9839403eafaa89050e2b8d3e, 12/15/18 726412975159353253
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* enter_data
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - chitchat: utter_anything_else
* deny
    - chitchat: utter_nohelp

## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897, 12/15/18 -6282839839722846955
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* enter_data
    - sales: action_store_job
    - slot{"job_function": "ohh sorry then"}
    - sales: utter_ask_usecase
* ask_faq_languages
    - faq: action_default_fallback
    - rewind

## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* nlu_info
    - rasa_help: action_default_fallback
    - rewind
* ask_howdoing
    - chitchat: action_default_fallback
    - rewind
* ask_whatspossible
    - chitchat: action_default_fallback
    - rewind
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_default_fallback
    - rewind
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - chitchat: utter_possibilities
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* enter_data
    - getstarted_1: action_default_fallback
    - rewind
* bye
    - chitchat: utter_bye

