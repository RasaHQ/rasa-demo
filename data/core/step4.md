## Step 4 prompt
* get_started_step4
    - action_greet_user
    - utter_describe_step4
    
## Happy path: Prompt -> Get event locations -> get date for location 
* get_started_step4
    - action_greet_user
    - utter_describe_step4
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Happy path: Get event locations -> get date for location  
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Prompt -> Get date for location
* get_started_step4
    - action_greet_user
    - utter_describe_step4
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum
    
## Get date for location
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Prompt -> Contribute
* get_started_step4
    - action_greet_user
    - utter_describe_step4
* ask_why_contribute
    - utter_reasons_to_contribute
* ask_how_contribute
    - utter_possibilities_to_contribute

## Contribute
* ask_why_contribute
    - utter_reasons_to_contribute
* ask_how_contribute
    - utter_possibilities_to_contribute

## Prompt -> How can I contribute
* get_started_step4
    - action_greet_user
    - utter_describe_step4
* ask_how_contribute
    - utter_possibilities_to_contribute
    
## How can I contribute
* ask_how_contribute
    - utter_possibilities_to_contribute
