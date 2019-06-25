# Plan to update Sara's Getting Started flow to include Rasa X


## FAQ (created for my own purpose)

- ### What does `action_greet_user` handle?
	If intent is `greet`, simply greets back (with a bunch of bells and whistles, of course).
	If the intent is `get_started_stepX`, it utters the `utter_get_started_stepX` utterance.
- ### How is `chitchat.md` structured?
	- All chitchat intents can be handled with a single response independent of state.
	- If the user chitchats after triggering an intent but before completing it, reply with `action_chitchat`, but also nudge the user to get back to finishing the flow of the incomplete intent.

## Questions to ask Akela
- I now plan to make Step 2 all about `rasa init` (as in the docs). I will have to scrap the existing "Ask any questions" step to make room for that. Is that okay?


## What baggage does a step in the "Getting Started" flow come with?

### In the domain file
- #### Direct intents to jump to that step (`get_started_stepX`)
	These are triggered only from UI buttons and not from user text input.
- #### Utterances to get started with the step (`utter_get_started_with_stepX`)
	The first message uttered by Sara as soon as that step is entered.
- #### `utter_continue_stepX`
	This is only in response to an `next_step` intent.
- #### `utter_direct_to_stepX`
	This is to both take the user to the next step in the normal "Getting Started" flow, but also to nudge the user back into the flow after a lull in the conversation after chitchat, disappointment, or a failure case.

### In story files related to the "Get Started" flow
- #### Previous-step story file
	Include stories to transition to the current step.

- #### Separate story file for the step
	The first step, for instance, is in `get_started.md`, but apart from an edge case like that one, it's good to keep each step in a separate story file.

### In story files not directly related to the "Get Started" flow
- #### Add stories in `faq.md` including scenarios where the standard flow is disturbed by a FAQ by the user, but then Sara nudges them back after answering it.
- #### Find points within the step where the user might chitchat and add a couple of stories in `chitchat.md` where the bot nudges the user back into resuming the standard flow.

## Moving old step 3 to step 4 + Moving old step 4 to step 5 + Introducing new step 3

### Moving old step 4 to step 5
1. Find & Replace `step4` with `step5` in `domain.yml`.
2. Find & Replace `step4` with `step5` in all story files.
3. Rename `step4.md` to `step5_community.md`.
4. Update `ActionNextSteps` to include step 5.

### Moving old step 3 to step 4
1. Find & Replace `step3` with `step4` in `domain.yml`.
2. Find & Replace `step3` with `step4` and occurrences of `slot{"step":"3"}` with `slot{"step":"4"}` in all story files.
3. Rename `step3_install_rasa.md` to `step4_install_rasa.md`.
4. The Find & Replace step (bullet point 2 above) would have resulted in some stories skipping from step 2 to step 4. Remove these transitions from step 2 to step  and create transitions from step 3.

### Replacing existing dummy step 2 with the `rasa init` step from the updated docs

#### In the domain file
1. Replace template text of `utter_get_started_step2` with something else instead of "Ask me any questions".

#### In the story files


### Introducing new step 3 for Rasa X
#### In the domain file
1. Create intent `get_started_step3`.
2. Create utterance `utter_get_started_step3`.
3. Create utterance `utter_continue_step3`.
4. Create utterance `utter_direct_to_step3`.
5. Include transitions from step 2.

#### In the story files
1. Create stories mentioned in the "baggage" section above.


## Renaming templates and changing template text

### Step 1

Explain components

#### Changes from corresponding step in legacy docs
This step is mostly the same as the old docs, just that information on Rasa X has been added.

#### Template needing text changes only
- `utter_get_started_step1`
- `utter_ask_which_product`
 
#### Template needing both name and text changes
- `utter_explain_nlucore` to `utter_explain_nlucorerasax`

#### New templates
- `utter_explain_rasax`
- `utter_faq_rasax_more`?

#### New intents
- `ask_faq_tutorialrasax`


### Step 2

rasa init step

#### Changes from corresponding step in legacy docs
The legacy docs end up writing the same example code that `rasa init` generates by hand instead.
Bonus point: The single command now means Sara can include that in her conversation!

#### Templates needing text changes only
- `utter_get_started_step2` (need input on this)

#### Templates needing both name and text changes
N/A

#### New templates
N/A

#### Intents to change
N/A

#### Intents to add
N/A


### Step 3

Start Rasa X

#### Changes from corresponding step in legacy docs
No equivalent in legacy docs.

#### Templates needing text changes only
N/A

#### Templates needing both name and text changes
N/A

#### New templates
N/A

#### Intents to change
N/A

#### Intents to add
N/A


### Step 4

Install with pip

#### Changes from corresponding step in legacy docs
Installation command for `pip` has changed (a single one that covers Rasa X as well). No more having to install starter pack either.

#### Templates needing text changes only
- `utter_installation_with_pip`
- `utter_installation_with_conda` (What's the new conda command?)

#### Templates needing both name and text changes
N/A

#### New templates
N/A

#### Intents to change
N/A

#### Intents to add
N/A


### Step 5

Join the community

#### Changes from corresponding step in legacy docs
N/A

#### Templates to change
N/A

#### Templates to add
N/A

#### Intents to change
N/A

#### Intents to add
N/A
