## Step 4 prompt
* get_started_step4
    - greet_success: action_greet_user

## Happy path: Prompt -> Get event locations -> get next event
* get_started_step4
    - greet_success: action_greet_user
* ask_which_events
    - getstarted_4_success: action_get_community_events
* ask_when_next_event
    - getstarted_4: action_get_community_events
    - getstarted_4_success: utter_recommend_forum

## Happy path: Prompt -> Get event locations -> get next event for location
* get_started_step4
    - greet_success: action_greet_user
* ask_which_events
    - getstarted_4_success: action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - getstarted_4: action_get_community_events
    - getstarted_4_success: utter_recommend_forum

## Happy path: Get event locations -> get next event
* ask_which_events
    - getstarted_4_success: action_get_community_events
* ask_when_next_event
    - getstarted_4_success: action_get_community_events
    - chitchat: utter_anything_else

## Happy path: Get event locations -> get next event for location
* ask_which_events
    - getstarted_4_success: action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - getstarted_4_success: action_get_community_events
    - chitchat: utter_anything_else

## Prompt -> Get next event
* get_started_step4
    - greet_success: action_greet_user
* ask_when_next_event
    - getstarted_4: action_get_community_events
    - getstarted_4_success: utter_recommend_forum

## Prompt -> Get next event for location
* get_started_step4
    - greet_success: action_greet_user
* ask_when_next_event{"location": "Berlin"}
    - getstarted_4: action_get_community_events
    - getstarted_4_success: utter_recommend_forum

## Get next event
* ask_when_next_event
    - getstarted_4_success: action_get_community_events
    - chitchat: utter_anything_else

## Get next event for location
* ask_when_next_event{"location": "Berlin"}
    - getstarted_4_success: action_get_community_events
    - chitchat: utter_anything_else

## Prompt -> Contribute
* get_started_step4
    - greet_success: action_greet_user
* ask_why_contribute
    - getstarted_4: utter_reasons_to_contribute
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute

## Contribute
* ask_why_contribute
    - getstarted_4: utter_reasons_to_contribute
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute

## Prompt -> How can I contribute
* get_started_step4
    - greet_success: action_greet_user
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute

## How can I contribute
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute

## Prompt -> Get help in forum
* get_started_step4
    - greet_success: action_greet_user
* ask_question_in_forum
    - getstarted_4_success: utter_link_to_forum

## Get help in the forum
* ask_question_in_forum
    - getstarted_4_success: utter_link_to_forum
