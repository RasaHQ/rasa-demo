## Get started from website
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* affirm
    - utter_run_rasa_init
    - utter_direct_to_step3

## Get starter from website + deny
* get_started_step2
    - action_greet_user
    - slot{"step": "2"}
* deny
    - utter_anything_else
