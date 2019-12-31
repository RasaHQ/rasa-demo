## prompt for getting started + confirm
* get_started_step1
    - action_greet_user
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa

## tech question, deny
* technical_question
  - action_docs_search
  - utter_ask_docs_help
* deny
  - action_forum_search

## tech question, affirm
* technical_question
  - action_docs_search
  - utter_ask_docs_help
* affirm
  - utter_great
