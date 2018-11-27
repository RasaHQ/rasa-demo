## Generated Story goal:getstarted, id:804addd312184e3384716589128ae5ad 7225286321375551559
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* enter_data
    - utter_direct_install
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:e6fa071ff0e94499b4a7bac0edd18227 -1135811984055669407
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whoisit
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
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:1140ececf0ec473180799dd4d598672d -6391045995910006908
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* None
    - action_default_fallback
    - rewind
* ask_howdoing
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
* enter_data{"number": 1}
    - utter_direct_install
    - utter_anything_else
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* ask_whoisit
    - action_chitchat
* out_of_scope
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* ask_isbot
    - action_chitchat
* enter_data
    - utter_possibilities
* technical_question
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* out_of_scope{"language": "french"}
    - slot{"language": "french"}
    - utter_out_of_scope
    - utter_possibilities
* enter_data
    - utter_possibilities
* thank
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "vincediegane@gmail.com"}
    - slot{"email": "vincediegane@gmail.com"}
    - action_store_email
    - slot{"email": "vincediegane@gmail.com"}
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
    - success

## Generated Story goal:getstarted, id:6422344c4803405494dc6c17e07b58d6 -8952212793634298420
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* signup_newsletter
    - utter_great
    - utter_ask_email
* enter_data{"email": "filippo.minutella@youtilitycenter.it"}
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
    - action_store_email
    - slot{"email": "filippo.minutella@youtilitycenter.it"}
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
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:ad5fb80204444eaa8a2bca3ac0c4183b 5787120610023818368
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whatspossible
    - action_chitchat
* technical_question
    - utter_nohelp
* technical_question
    - utter_possibilities
* technical_question
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
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
    - success

## Generated Story goal:getstarted, id:ef1eafd9a1b04caa8782be82351ce33f -8550015207896305719
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* ask_whatspossible
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* thank
    - utter_noworries
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
    - rewind
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* thank
    - utter_noworries
    - success

## Generated Story goal:getstarted, id:0f8813a190904078aa2cff1b7faa1e69 2483633972736899851
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
    - utter_ask_goal
* ask_builder
    - action_chitchat
    - utter_ask_goal
* ask_whatisrasa
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
* switch
    - action_store_unknown_product
    - slot{"unknown_product": "wit"}
    - utter_no_guide_for_switch
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* mood_confirm
    - utter_what_language
* enter_data
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:b38efbb91d3745fea37234277008fbd8 -8826923805113198293
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
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
* enter_data{"jobfunction": "developer"}
    - action_store_job
    - slot{"job_function": "developer"}
    - utter_ask_usecase
* enter_data
    - action_store_usecase
    - slot{"use_case": "virtual assistant"}
    - utter_thank_usecase
    - utter_ask_budget
* enter_data{"amount-of-money": 2}
    - action_store_budget
    - slot{"budget": 2}
    - utter_sales_contact
    - utter_ask_name
* enter_data
    - action_store_name
    - slot{"person_name": "Thorin"}
    - utter_ask_company
* enter_data
    - action_store_company
    - slot{"company_name": "Gandalfs company"}
    - utter_ask_businessmail
* enter_data{"email": "thorin@thorin.thorin.com"}
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_email
    - slot{"email": "thorin@thorin.thorin.com"}
    - action_store_sales_info
    - slot{"data_stored": true}
    - utter_confirm_salesrequest
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:182ec26caec44bc1a5599afc4b899ba3 9195754664139970630
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
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_ask_which_tool
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "IBM watson"}
    - utter_no_guide_for_switch
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:3056d16b1ef34735b867f0eb00da5a9e 3333718755217779700
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
* mood_confirm
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:03aec288fb8344dd9a6aa47d37af2e6d -9063334716126405558
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
* enter_data
    - utter_possibilities
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:01b872dd65de4a86870be245dae0984c -4008979391761926606
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* greet
    - utter_greet
* ask_whatisrasa
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:1fbc61697e0f4a149b6ff4a0fac4b64e 7076594325776430566
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
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
    - success

## Generated Story goal:getstarted, id:2ac693732f3b4df492bf2ad72fea841d 7282290640424792666
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_chitchat
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
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:87619e690d10457c932eba08f9ebf602 -588461147343309013
* enter_data
    - utter_thumbsup
    - utter_anything_else
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
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:5f458669c6e04aa8b2f4e52cf81cffa1 -1510198585533270087
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:7830abb04e1c49809d89b0d420443928 8103804079007693517
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
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
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
* mood_confirm
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:49bbf948433247c784fe2ed199f7c931 -6822057689937111858
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
* enter_data
    - utter_direct_install
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:5b72515d7e584a17aac1ca10eb53214b 2164085748464922413
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
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_explain_nlu
    - utter_also_explain_core
* mood_confirm
    - utter_explain_core
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* deny
    - utter_nohelp
    - success

## Generated Story goal:getstarted, id:c28fd8cf8e3c4bb89fd79922e74ddc6d 4726379811329892019
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
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started
    - action_set_onboarding
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* enter_data
    - action_subscribe_newsletter
    - action_subscribe_newsletter
    - utter_already_subscribed
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* deny
    - utter_nohelp
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:a3c62ec26bd84b46adf61078d9b7e01f 606750322048733708
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
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
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - success

## Generated Story goal:getstarted, id:b33184c82c4b49e8bc52e5b141654865 -2426218508657778534
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - utter_out_of_scope
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_direct_install
    - utter_anything_else
* deny
    - utter_nohelp
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:bffb69a4cadf4a869cce7f5dc6697c18 7088543905590691654
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
* enter_data
    - action_store_unknown_product
    - slot{"unknown_product": "watson"}
    - utter_no_guide_for_switch
    - utter_anything_else
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:dd97568cca7047a8bb99be9f041b82bd 8922594620458208000
* suggestions
    - action_chitchat
* greet
    - utter_greet
    - utter_inform_privacypolicy
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
    - success

## Generated Story goal:getstarted, id:50ad2b993b10423d9ddd29c8be88ab29 -8163866633515756993
* greet{"name": "Hi Sara"}
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
    - action_default_fallback
    - rewind
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:bf26e70697f04378920c63969626983b -950120035011271909
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
    - success

## Generated Story goal:getstarted, id:3f91ca8a9a19474896f4adab215b57cb 3002101841828049418
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* enter_data
    - action_default_fallback
    - rewind
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
    - success

## Generated Story goal:getstarted, id:4dfd10b7c4de4b7285af501e70713d81 6032599555972573384
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* deny
    - utter_thumbsup
    - success

## Generated Story goal:getstarted, id:d0895ef800074d4789bd068717e10e9c -3632685140551545497
* ask_whoisit
    - action_chitchat
* mood_confirm
    - utter_moreinformation
    - utter_ask_jobfunction
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
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:6afa2fd339334781bc97175ee2b05193 6748218506133865554
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* bye
    - action_default_fallback
    - rewind
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
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:8350a9684ee14756a5ad58eb04c7b689 3964150509455257122
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet{"name": "Hello Sara"}
    - utter_greet
* bye
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_default_fallback
    - rewind
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
    - success

## Generated Story goal:getstarted, id:2bf3e50bb96d48c3a6ff8b35e6a40ab4 809757456182353991
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* enter_data{"name": "Iam Jorge"}
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
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* how_to_get_started{"product": "NLU"}
    - slot{"product": "NLU"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:9028a7bef4174c948ecb8de636be45af -9066548740019796988
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
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started
    - utter_explain_core
    - utter_also_explain_nlu
* mood_confirm
    - utter_explain_nlu
    - utter_tryout
* mood_confirm
    - utter_quickstart
    - utter_anything_else
* thank
    - utter_noworries
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* bye
    - utter_bye
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:41972a8ea1c4401e8a765d481763157d -7368167987920860439
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* signup_newsletter
    - utter_great
    - utter_ask_email
* deny
    - utter_cantsignup
* mood_confirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
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
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
    - success

## Generated Story goal:getstarted, id:7a1c1b5c0cb444c29f73b01d0b8c06a4 9091758904003219508
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_howdoing
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data{"number": 0}
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
* thank
    - utter_noworries
    - success

## Generated Story goal:getstarted, id:ab03e7289b9a44d099bce53798de9fe5 441847645207684396
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_default_fallback
    - rewind
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
    - success

## Generated Story goal:getstarted, id:a6b68460fd2e486ca17afdfb7356cd2f -6974982680890971993
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_default_fallback
    - rewind
* greet
    - action_default_fallback
    - rewind
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
* deny
    - utter_tryout
* enter_data
    - action_default_fallback
    - rewind
* enter_data
    - utter_direct_install
    - utter_anything_else
* greet
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:2a688257f572484eaf03df69d53fd9ef 2885280474659434668
* ask_isbot
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
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
    - success

## Generated Story goal:getstarted, id:94c1d05a42fa432fb71326bbffe8c50b 8049130048445434917
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
* switch{"current_api": "Dialogflow"}
    - slot{"current_api": "Dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else
* ask_howdoing
    - action_chitchat
* enter_data
    - utter_possibilities
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:4ead4fe5fce941f49803825fe87cd922 6128142241568278816
* out_of_scope
    - action_default_fallback
    - rewind
* ask_whoisit{"jobfunction": "development"}
    - action_default_fallback
    - rewind
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_possibilities
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
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* ask_howdoing
    - action_default_fallback
    - rewind
    - success

## Generated Story goal:getstarted, id:61a82be0dab04e118e2ed042eb4e3d62 5060731619518034784
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - action_default_fallback
    - rewind
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
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* mood_confirm
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
    - success

## Generated Story goal:getstarted, id:d4be1b5442844bdfa3fdba00aced5503 -8792732129308822623
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
* ask_weather
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - success

## Generated Story goal:getstarted, id:f905fe9c8bc2472286d888a3d2bc2e99 4115093303662244698
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* ask_whatspossible
    - action_default_fallback
    - rewind
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
    - fail

## Generated Story goal:getstarted, id:02094ca453f647e686d26181b4d03f4f 285835436521501832
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_ask_which_product
* technical_question
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:bdda478467ce482190d6703d27ea2d53 8810074103022150505
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
    - fail

## Generated Story goal:getstarted, id:131b0646a27e4cf6aab2a86c5619b023 1957186685348396238
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* technical_question
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
* ask_howdoing
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:1246edc0c1384ad59b1554da3bbcf56d -3079800542573812286
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:6b5d9883a3cf4f8ba1817bf884e2e108 6460683172762636038
* enter_data
    - utter_thumbsup
    - utter_anything_else
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
    - fail

## Generated Story goal:getstarted, id:9320945deed5459090e9971640365359 7225300078731012991
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
    - action_set_onboarding
    - utter_ask_which_product
* mood_confirm
    - utter_thumbsup
* enter_data
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:216f35cf3e894c0bb13172f51b50dad4 6339986528410007685
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* technical_question
    - utter_moreinformation
    - utter_ask_jobfunction
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
    - utter_ask_jobfunction
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "both"}
    - slot{"product": "both"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_core_tutorial
    - utter_anything_else
* deny
    - utter_nohelp
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:4986d88ccb784dc19dc5a553a8e07890 -7138330429390946500
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
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
* out_of_scope
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
    - utter_tryout
* deny
    - utter_direct_install
    - utter_anything_else
* deny
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:ec346070b4734e00af295571f55837f7 3937001759518359192
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
    - fail

## Generated Story goal:getstarted, id:892498320d384a78aed6696f6e67a538 2758406977396380019
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
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
* enter_data
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* mood_confirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_tryout
    - fail

## Generated Story goal:getstarted, id:fd0058985c3e45c4bf4aa94c997407ca -5959243819871802887
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
* enter_data
    - utter_possibilities
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* ask_whatisrasa
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* human_handoff
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"number": 1}
    - utter_possibilities
* enter_data
    - utter_possibilities
* ask_whatspossible
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* bye
    - utter_bye
* enter_data
    - utter_possibilities
    - fail

## Generated Story goal:getstarted, id:e900e06d633e47c3b831f23425cd7d83 8536078750217323562
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* greet{"name": "Hi Sara"}
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* mood_confirm
    - utter_thumbsup
* ask_whatspossible
    - action_default_fallback
    - rewind
* out_of_scope
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
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
* contact_sales
    - utter_moreinformation
    - utter_ask_jobfunction
    - fail

## Generated Story goal:getstarted, id:ad53b51192aa4bef8954393678d413a2 -5436498510117694639
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:d2b672f04dca45fdbed1ad627b5b3f49 7460061025584704171
* suggestions
    - action_chitchat
* ask_whatspossible
    - action_default_fallback
    - rewind
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:0f885021e48448f0a467b3addf5f6e78 428447117903737460
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_whoisit
    - action_chitchat
    - utter_ask_goal
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* canthelp
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:21eb481b1e5742839fcd14967856e7d4 -6585149076198522394
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
    - fail

## Generated Story goal:getstarted, id:1d3f0ed42700470c92551c307a4bee3a 3322080963775725146
* ask_whoisit
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
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
* enter_data
    - utter_direct_install
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:ac171abfe26347819d63e32761822f28 1003567858497349197
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
* how_to_get_started
    - utter_quickstart_nlu_only
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data{"number": 1}
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:04f11e5aef73408191a373cc370e6654 6997791890647313420
* suggestions
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_isbot
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:dcf5fd070ce44d8dad16adef14991aaf -1174805203229697062
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_nohelp
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
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* enter_data
    - utter_explain_nlu
    - utter_tryout
* greet
    - utter_quickstart
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:3af5aad1b1dd487fbba6bf84499c157c 1082174467868192642
* out_of_scope
    - action_default_fallback
    - rewind
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
* enter_data
    - utter_direct_install
    - utter_anything_else
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* enter_data
    - utter_possibilities
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
* mood_confirm
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:485b1dc8843140eb9ac7de845410dd3c -5237910970854027829
* enter_data
    - utter_thumbsup
    - utter_anything_else
* enter_data
    - utter_possibilities
* signup_newsletter
    - utter_great
    - utter_ask_email
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
    - fail

## Generated Story goal:getstarted, id:b294305abf414f43bf95c259376bc20e -5106287164487535265
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* enter_data
    - action_default_fallback
    - rewind
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
* how_to_get_started{"product": "Core"}
    - slot{"product": "Core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
* mood_confirm
    - utter_thumbsup
    - utter_anything_else
* mood_confirm
    - utter_great
    - utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:4114e7e201264ebdbb8e2587aedc88b9 7985448692066050345
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* out_of_scope
    - action_default_fallback
    - rewind
* enter_data
    - action_default_fallback
    - rewind
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* mood_confirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_whatspossible
    - action_chitchat
* mood_confirm
    - utter_ask_which_tool
* switch{"current_api": "LUIS"}
    - slot{"current_api": "LUIS"}
    - utter_switch_luis
    - utter_anything_else
* technical_question{"number": 2}
    - action_default_fallback
    - rewind
* greet
    - utter_greet
    - utter_anything_else
    - fail

## Generated Story goal:getstarted, id:11ff91e7d8ad4958b776947f5ef028e1 -6877918746206397770
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* rasa_cost
    - action_default_fallback
    - rewind
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
* how_to_get_started
    - action_default_fallback
    - rewind
    - fail

## Generated Story goal:getstarted, id:09b0f4cb27e34984b1113c1bb0000be8 4656655880231031012
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_weather
    - action_default_fallback
    - rewind
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
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart
    - utter_anything_else
* nlu_generation_tool_recommendation
    - action_default_fallback
    - rewind
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:628e0b1d3ab447f2a71822f6e415fc27 -1287693679338030456
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* greet
    - utter_greet
* how_to_get_started
    - action_default_fallback
    - rewind
* nlu_generation_tool_recommendation
    - action_chitchat
* how_to_get_started
    - action_default_fallback
    - rewind
* enter_data
    - utter_possibilities
* ask_howdoing
    - action_default_fallback
    - rewind
* bye
    - utter_bye
* enter_data
    - utter_thumbsup
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
    - fail

## Generated Story goal:getstarted, id:2461296c8be74fdaa611510ae37c815e -3953933487207395692
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
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart_nlu_only
    - utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding
    - utter_built_bot_before
* enter_data
    - action_store_budget
    - slot{"budget": "stp"}
    - utter_sales_contact
    - utter_ask_name
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
    - fail

## Generated Story goal:getstarted, id:228c4db18f41427ea1cd5846cd39a4a6 9099491353635173180
* greet
    - utter_greet
    - utter_inform_privacypolicy
    - utter_ask_goal
* ask_howdoing
    - action_default_fallback
    - rewind
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
    - fail

