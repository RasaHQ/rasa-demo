## Generated Story goal:sales, id:e1ae1d77ce414451966eae0e29478965 3813469956131177392
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* enter_data
    - action_default_fallback   <!-- predicted: whatspossible -->
    - event_rewind
* contact_sales
    - utter_moreinformation   <!-- predicted: action_default_fallback -->
    - utter_ask_jobfunction   <!-- predicted: sales -->
* enter_data
    - action_store_job   <!-- predicted: sales -->
    - slot{"job_function": "it"}
    - utter_ask_usecase   <!-- predicted: sales -->
* ask_whatspossible
    - action_default_fallback
    - event_rewind


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f -3193790453386953922
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_getstarted   <!-- predicted: utter_thumbsup -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* deny
    - utter_tryout   <!-- predicted: getstarted_1 -->
* ask_howold
    - action_chitchat   <!-- predicted: getstarted_1_success -->
    - utter_tryout   <!-- predicted: utter_anything_else -->
* deny
    - utter_direct_install   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* mood_confirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* ask_isbot
    - action_default_fallback
    - event_rewind
* mood_confirm
    - utter_quickstart   <!-- predicted: utter_thumbsup -->
    - utter_anything_else


## Generated Story goal:1 step, id:8d69c4b1d6db489789fe20e2bbeec153 359536621318615265
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: getstarted_1 -->
    - utter_getstarted_new   <!-- predicted: getstarted_1 -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:chitchat, id:ed1418fcc3884157bcc96a7c43d21ec0 6260517791662603475
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat   <!-- predicted: whatspossible -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107 -7846924235013194113
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* nlu_info
    - action_default_fallback
    - event_rewind
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_default_fallback   <!-- predicted: action_set_onboarding -->
    - event_rewind
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* enter_data
    - utter_possibilities   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* enter_data
    - action_default_fallback   <!-- predicted: getstarted_1_success -->
    - event_rewind
* bye
    - utter_bye


## Generated Story goal:1 step, id:33a2877c49944765a102c0a215632b8a -5101663944288452126
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_builder
    - action_chitchat   <!-- predicted: chitchat -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547 -2368390795593266214
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* mood_confirm
    - utter_thumbsup
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: getstarted_1 -->
    - utter_getstarted_new   <!-- predicted: getstarted_1 -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: getstarted_1 -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: getstarted_1 -->
    - utter_anything_else
* enter_data
    - action_greet_user   <!-- predicted: sales -->
    - action_listen   <!-- predicted: event_rewind -->
* bye
    - action_default_fallback   <!-- predicted: action_listen -->
    - event_rewind
* technical_question
    - action_default_fallback   <!-- predicted: utter_greet -->
    - event_rewind
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* enter_data
    - action_greet_user   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: getstarted_1 -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_set_onboarding -->
    - event_rewind
* handleinsult
    - action_chitchat   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* enter_data
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* bye
    - utter_bye   <!-- predicted: action_default_fallback -->
* nlu_info
    - action_default_fallback   <!-- predicted: rasa_help -->
    - event_rewind
* deny
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - event_rewind


## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c -939096969720361536
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started{"name": "sara"}
    - slot{"name": "sara"}
    - slot{"name": "sara"}
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* ask_whatisrasa
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* how_to_get_started
    - action_chitchat   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->


## Generated Story goal:1 step, id:321d95bf0cb14dc8b09f3f9a62827081 -5724607564025630073
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - action_default_fallback   <!-- predicted: whatspossible -->
    - event_rewind
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_migration   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_which_tool   <!-- predicted: getstarted_1 -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_default_fallback -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial   <!-- predicted: getstarted_1 -->
    - utter_anything_else
* deny
    - utter_thumbsup   <!-- predicted: getstarted_1 -->
    - utter_anything_else


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8 -2832431544839393815
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_time
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_weather
    - action_chitchat   <!-- predicted: chitchat -->
* ask_weather
    - action_default_fallback
    - event_rewind
* handleinsult
    - action_default_fallback
    - event_rewind
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->


## Generated Story goal:chitchat, id:bbf4baacf5e34a358eaaa875721bdf5b -3970559270584338323
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* handleinsult
    - action_chitchat   <!-- predicted: whatspossible -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_weather
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:1 step, id:cfa8bb9deaf0427498c662745431a282 7693250765518470056
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_chitchat   <!-- predicted: chitchat -->
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:19722107f07a4120bef398ea514e00de -1964274332519679275
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started{"language": "chinese"}
    - slot{"language": "chinese"}
    - slot{"language": "chinese"}
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b 8960079641748937294
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14 8397832515844528246
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_languagesbot
    - action_chitchat   <!-- predicted: whatspossible -->
* enter_data
    - action_default_fallback   <!-- predicted: whatspossible -->
    - event_rewind
* handleinsult
    - action_default_fallback
    - event_rewind
* nicetomeeyou
    - action_default_fallback
    - event_rewind
* nicetomeeyou
    - action_default_fallback   <!-- predicted: utter_greet -->
    - event_rewind
* nicetomeeyou
    - action_default_fallback   <!-- predicted: utter_greet -->
    - event_rewind
* nicetomeeyou
    - action_default_fallback
    - event_rewind
* canthelp
    - action_default_fallback   <!-- predicted: utter_canthelp -->
    - event_rewind
* ask_faq_opensource
    - action_default_fallback   <!-- predicted: utter_greet -->
    - event_rewind
* out_of_scope
    - utter_out_of_scope   <!-- predicted: oos -->
    - utter_possibilities   <!-- predicted: whatspossible -->
* mood_confirm
    - action_default_fallback   <!-- predicted: utter_thumbsup -->
    - event_rewind
* signup_newsletter
    - utter_great
    - utter_ask_email   <!-- predicted: subscribe -->
* deny
    - utter_cantsignup   <!-- predicted: subscribe -->
* deny
    - action_default_fallback
    - event_rewind
* enter_data
    - action_store_email   <!-- predicted: action_default_fallback -->
    - event_rewind
* bye
    - action_default_fallback
    - event_rewind
* handleinsult
    - action_chitchat   <!-- predicted: utter_greet -->
    - utter_ask_email   <!-- predicted: action_listen -->
* deny
    - utter_cantsignup   <!-- predicted: utter_nohelp -->
* deny
    - utter_direct_install   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:9978f875abec4c3c9955ec3d5dae51b1 -1115556105762185463
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_migration   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_which_tool   <!-- predicted: getstarted_1 -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_default_fallback -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_also_explain_core   <!-- predicted: getstarted_1 -->
* enter_data{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897 -7563329072543246003
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* contact_sales
    - utter_moreinformation   <!-- predicted: sales -->
    - utter_ask_jobfunction   <!-- predicted: sales -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* enter_data
    - action_store_job   <!-- predicted: whatspossible -->
    - slot{"job_function": "ohh sorry then"}
    - utter_ask_usecase   <!-- predicted: whatspossible -->
* ask_faq_languages
    - action_default_fallback
    - event_rewind


## Generated Story goal:chitchat, id:624b61bee53b411bac4a3855343dd0c7 -8142526563487221880
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* mood_confirm
    - utter_thumbsup
* out_of_scope
    - action_default_fallback   <!-- predicted: oos -->
    - event_rewind
* ask_howold
    - action_chitchat   <!-- predicted: utter_greet -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:1 step, id:2f822433f6a9427c8bff569c676d824e 8587624803761655375
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* deny
    - utter_tryout   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp
* ask_whoisit
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:chitchat, id:455210c2c7c9471194a7faaf2e63579f 4886035070370829562
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: oos -->
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_set_onboarding -->
    - utter_anything_else
* ask_isbot
    - action_chitchat   <!-- predicted: action_default_fallback -->


## Generated Story goal:3 step, id:6ce300612cda42c1a084c292455056f7 615476791518671688
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* install_rasa
    - utter_ask_python_installed   <!-- predicted: whatspossible -->
* mood_confirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_thumbsup -->
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:15f92cc91e4e4c86826ffd023f4d1ef7 5872737683778111883
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* enter_data
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build   <!-- predicted: utter_anything_else -->
* mood_confirm
    - action_store_problem_description   <!-- predicted: utter_thumbsup -->
    - slot{"problem_description": "yes"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:db1d15d9e40047ebb3e8c13bbd0810b3 -5120050494287481159
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_getstarted   <!-- predicted: utter_thumbsup -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->


## Generated Story goal:chitchat, id:7daa8ec84bbe48a6a154517eacd06560 2580029483773864897
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_faq_opensource
    - action_faqs   <!-- predicted: whatspossible -->


## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e 4148331427500451641
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_howold
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_howold{"number": 42}
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_howold
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6 -7446691118563902686
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* enter_data
    - action_default_fallback   <!-- predicted: whatspossible -->
    - event_rewind
* out_of_scope
    - utter_out_of_scope   <!-- predicted: oos -->
    - action_listen   <!-- predicted: whatspossible -->
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - action_greet_user   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: sales -->
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: sales -->
* enter_data
    - action_default_fallback   <!-- predicted: subscribe -->
    - event_rewind


## Generated Story goal:chitchat, id:2721ae89d30d4c28964ac367c2e553ed -8728345761108168210
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_time
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_time
    - action_chitchat   <!-- predicted: action_default_fallback -->
* source_code
    - utter_source_code   <!-- predicted: action_default_fallback -->
    - utter_anything_else   <!-- predicted: event_rewind -->


## Generated Story goal:1 step, id:0da3c44e9839403eafaa89050e2b8d3e 4876401631218801584
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_migration   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_ask_which_tool   <!-- predicted: getstarted_1 -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_default_fallback -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:8affa7a6082945a09f031db186ec22eb -4001005524002155722
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* enter_data
    - action_greet_user   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_inform_privacypolicy -->
* ask_howdoing
    - action_chitchat   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:953db2ccbe0748c586f5904a1b9b4432 1283565117102283474
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: action_default_fallback -->
* deny
    - utter_get_python   <!-- predicted: getstarted_1 -->
    - utter_ask_pip_or_conda   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->
* mood_confirm
    - utter_get_starter_pack   <!-- predicted: utter_thumbsup -->
    - utter_direct_to_step4   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:sales, id:c08c1942644d489ea1995880bf043a85 5904062332080740894
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: getstarted_1 -->
    - event_rewind
* enter_data
    - utter_possibilities   <!-- predicted: action_default_fallback -->
* contact_sales
    - utter_moreinformation   <!-- predicted: sales -->
    - utter_ask_jobfunction   <!-- predicted: sales -->


## Generated Story goal:1 step, id:3a1c70eaf9234bb6b27160abfb6d1f88 -7096667604269349049
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - action_listen   <!-- predicted: utter_anything_else -->


## Generated Story goal:oos, id:c750b33383004b0da4da73284fe9fa48 -1119210502632786213
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:1 step, id:120a458cbe094db9b49c0d2a9adca7ca 8276698609842762849
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_getstarted   <!-- predicted: utter_thumbsup -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:1 step, id:92128e5e2ea74967876544a30c37b41a 1702913253387903917
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:fe9205767e5540319511248ba2d7aa7d -7427065441319792243
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: getstarted_1 -->
    - utter_getstarted_new   <!-- predicted: getstarted_1 -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* thank
    - utter_noworries
    - utter_anything_else
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->


## Generated Story goal:1 step, id:29431126a80044e09522bce5e9fff1a7 -5391666320608473707
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial   <!-- predicted: getstarted_1 -->
    - utter_anything_else
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_thumbsup
* get_started_step1
    - action_greet_user   <!-- predicted: getstarted_1 -->
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_inform_privacypolicy -->
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* greet{"name": "Hey There"}
    - slot{"name": "Hey There"}
    - slot{"name": "Hey There"}
    - action_greet_user   <!-- predicted: utter_greet -->
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* enter_data
    - action_greet_user   <!-- predicted: whatspossible -->
* ask_whoisit
    - action_chitchat   <!-- predicted: chitchat -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind


## Generated Story goal:chitchat, id:ada5f58b5ea4436fb1993578ca7fc805 -3469876884661742012
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_whoisit
    - action_chitchat   <!-- predicted: chitchat -->
* ask_howold
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_weather{"name": "New York"}
    - slot{"name": "New York"}
    - slot{"name": "New York"}
    - action_chitchat   <!-- predicted: chitchat -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f -3789507224606616572
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_whoisit
    - action_chitchat   <!-- predicted: chitchat -->
* ask_howold
    - action_chitchat   <!-- predicted: action_default_fallback -->
* enter_data
    - action_store_email   <!-- predicted: whatspossible -->
    - event_rewind
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: action_default_fallback -->
    - slot{"email": "tens@da.ok"}
    - action_subscribe_newsletter   <!-- predicted: event_rewind -->
    - slot{"subscribed": true}
    - utter_awesome
    - utter_confirmationemail   <!-- predicted: subscribe_success -->
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* ask_restaurant
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - event_rewind
* enter_data
    - utter_great   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* mood_confirm
    - utter_great   <!-- predicted: utter_thumbsup -->
    - utter_anything_else
* mood_confirm
    - utter_great   <!-- predicted: utter_thumbsup -->
    - utter_anything_else
* ask_whoisit
    - action_default_fallback
    - event_rewind
* deny
    - utter_great   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* ask_wherefrom
    - action_chitchat   <!-- predicted: utter_nohelp -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - event_rewind
* mood_confirm
    - utter_great   <!-- predicted: utter_thumbsup -->
    - utter_anything_else
* enter_data
    - utter_great   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* handleinsult
    - action_chitchat   <!-- predicted: utter_nohelp -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - event_rewind
* enter_data
    - utter_great   <!-- predicted: utter_nohelp -->
    - utter_anything_else
* mood_confirm
    - utter_great   <!-- predicted: utter_thumbsup -->
    - utter_anything_else


## Generated Story goal:1 step, id:c1413213af684cbd952299e5b640a174 6184331545526864686
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* technical_question
    - action_default_fallback
    - event_rewind
* ask_whatisrasa
    - action_chitchat   <!-- predicted: chitchat -->
    - action_listen   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* deny
    - utter_nohelp
* thank
    - utter_noworries
    - utter_anything_else
* deny
    - utter_nohelp


## Generated Story goal:faq, id:1b9d609211b74674844d925461b24744 3916382684173895070
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_faq_voice
    - action_faqs   <!-- predicted: action_default_fallback -->
* mood_confirm
    - utter_thumbsup


## Generated Story goal:1 step, id:4f647cb2427c495dbff5cf6fa1d7feb9 112777051765457247
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_getstarted   <!-- predicted: utter_thumbsup -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* enter_data
    - action_greet_user   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_quickstart   <!-- predicted: getstarted_1 -->
    - utter_anything_else


## Generated Story goal:1 step, id:5b7be2c22b874342aeca4216cfd5d35a -4193596357122073034
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* out_of_scope
    - utter_out_of_scope   <!-- predicted: oos -->
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:1 step, id:8861ebbcdb684fb98a66f65a357d07b0 3588737890338167525
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->


## Generated Story goal:1 step, id:2979714d45bc445e9d7241fdc3ad64c1 -2658915758462411967
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* handleinsult
    - action_chitchat   <!-- predicted: whatspossible -->
* deny
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - event_rewind
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
* handleinsult
    - action_chitchat   <!-- predicted: action_default_fallback -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* enter_data
    - action_set_onboarding   <!-- predicted: action_default_fallback -->
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* enter_data
    - action_select_installation_command   <!-- predicted: getstarted_1 -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->
* deny
    - utter_ask_if_problem   <!-- predicted: getstarted_1 -->


## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916 -9074445332041262487
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* mood_confirm
    - utter_getstarted   <!-- predicted: utter_thumbsup -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else


## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc -3711814691468599799
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_default_fallback   <!-- predicted: chitchat -->
    - event_rewind
* greet
    - action_greet_user   <!-- predicted: utter_greet -->
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_wherefrom
    - action_chitchat   <!-- predicted: action_default_fallback -->
* mood_confirm
    - action_default_fallback   <!-- predicted: utter_thumbsup -->
    - event_rewind
* mood_confirm
    - action_default_fallback   <!-- predicted: utter_thumbsup -->
    - event_rewind


## Generated Story goal:chitchat, id:67a8696eb5894b25a800b6cbd7a695bb -1433687689422449604
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* ask_howdoing
    - action_chitchat   <!-- predicted: chitchat -->
* ask_whoisit
    - action_chitchat   <!-- predicted: chitchat -->
* enter_data
    - action_select_installation_command   <!-- predicted: whatspossible -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: whatspossible -->
* ask_faq_languages
    - action_store_problem_description   <!-- predicted: action_default_fallback -->
    - slot{"problem_description": "what languages do you support?"}
    - action_faqs   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_default_fallback -->
    - utter_ask_ready_to_build   <!-- predicted: action_listen -->
* enter_data
    - action_store_problem_description   <!-- predicted: action_default_fallback -->
    - slot{"problem_description": "ofcouse"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
* mood_confirm
    - utter_anything_else   <!-- predicted: utter_thumbsup -->
* handleinsult
    - action_default_fallback   <!-- predicted: utter_thumbsup -->
    - event_rewind
* deny
    - utter_nohelp
* out_of_scope
    - action_default_fallback   <!-- predicted: oos -->
    - event_rewind
* deny
    - utter_nohelp


## Generated Story goal:1 step, id:cdd14d763a664a5b95e998ce165bd86f -7969799930115274360
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: whatspossible -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: getstarted_1 -->
    - utter_first_bot_with_rasa   <!-- predicted: getstarted_1 -->
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: getstarted_1 -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* enter_data
    - action_greet_user   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037 -1171446944825865182
* get_started_step1
    - action_greet_user   <!-- predicted: utter_greet -->
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: getstarted_1 -->
    - utter_getstarted_new   <!-- predicted: getstarted_1 -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: getstarted_1 -->
    - utter_stack_details   <!-- predicted: getstarted_1 -->
    - utter_explain_nlucore   <!-- predicted: getstarted_1 -->
* mood_confirm
    - utter_explain_nlu   <!-- predicted: getstarted_1 -->
    - utter_explain_core   <!-- predicted: getstarted_1 -->
    - utter_tryout   <!-- predicted: getstarted_1 -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: getstarted_1_success -->
    - event_rewind
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: getstarted_1_success -->
    - utter_anything_else
* enter_data
    - action_default_fallback
    - event_rewind
* enter_data
    - action_default_fallback   <!-- predicted: whatspossible -->
    - event_rewind


