## feedback2
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## akela test
* enter_data@0.7{"name":"Akela"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "SpacyEntityExtractor"}
    - utter_spacy
    - utter_anything_else