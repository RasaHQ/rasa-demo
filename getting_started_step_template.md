<!-- Replace "X" with the step number and "X-1" with the previous step number -->

## Step X prompt
* get_started_stepX
    - action_greet_user

## transition from step X-1
* get_started_stepX-1
    - action_greet_user
    - slot{"step":"X-1"}
    - utter_direct_to_stepX
* get_started_stepX
    - action_greet_user
    - slot{"step":"X"}

