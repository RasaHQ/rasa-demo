## prompt for getting started + confirm
* get_started_step1
    - action_greet_user
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa

## technical_question - docs_found - deny
* technical_question
    - action_docs_search
    - slot{"docs_found": true}
    - utter_ask_docs_help
* deny
    - action_tag_docs_search
    - action_forum_search

## technical_question - docs_found - affirm
* technical_question
    - action_docs_search
    - slot{"docs_found": true}
    - utter_ask_docs_help
* affirm
    - action_tag_docs_search
    - utter_great

## technical_question - no docs_found
* technical_question
    - action_docs_search
    - slot{"docs_found": false}
    - action_forum_search