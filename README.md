# Sara - the Rasa Demo Bot

## :surfer: Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.

Sara is an alpha version and lives in our docs, 
helping developers getting started with our open source tools. It supports the following user goals:

- Understanding the Rasa framework
- Getting started with Rasa
- Answering some FAQs around Rasa
- Directing technical questions to specific documentation
- Subscribing to the Rasa newsletter
- Requesting a call with Rasa's sales team
- Handling basic chitchat

You can find planned enhancements for Sara in the
[Project Board](https://github.com/RasaHQ/rasa-demo/projects/1)

## 👷‍ Installation

To install Sara, please clone the repo and run:

```sh
cd rasa-demo
make install
```

This will install the bot and all of its requirements.
Note that this bot should be used with python 3.6 or 3.7.


## 🤖 To run Sara:

Use `rasa train` to train a model (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`).

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions --actions actions.actions
```

There are some custom actions that require connections to external services,
specifically `SubscribeNewsletterForm` and `SalesForm`. For these
to run you would need to have your own MailChimp newsletter and a Google sheet
to connect to. See the [development](#development) section for instructions on providing
credentials for external services.

In another window, run the bot:
```bash
docker run -p 8000:8000 rasa/duckling
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working 
under the hood. To simply talk to the bot, you can remove this flag.

If you would like to run Sara on your website, follow the instructions
[here](https://github.com/botfront/rasa-webchat) to place the chat widget on
your website.

## To test Sara:

After doing a `rasa train`, run the command:

```bash
rasa test nlu -u test/test_data.json --model models
rasa test core --stories test/test_stories.md
```

## 👩‍💻 Overview of the files

`data/core/` - contains stories 

`data/nlu` - contains NLU training data

`actions` - contains custom action code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble


## Development

To install requirements for development, run:

```sh
make install-dev
```

To run custom actions locally, put a file called .env in the root of your local directory with values
for the following environment variables. Most actions will work without them, but if you are working on actions
connecting to external APIs you will need credentials.


```
GDRIVE_CREDENTIALS=#json access key for Google Drive API for action_submit_sales_form
MAILCHIMP_LIST=#id of mailchimp list for action_submit_subscribe_newsletter_form
MAILCHIMP_API_KEY=#api key for mailchimp
ALGOLIA_APP_ID=#algolia app ID for action_docs_search 
ALGOLIA_SEARCH_KEY=#algolia search key
ALGOLIA_DOCS_INDEX=#algolia search index
RASA_X_HOST=#Rasa X domain e.g. localhost:5002
RASA_X_PASSWORD=#password for authenticating into Rasa X
RASA_X_USERNAME=#username for authenticating into Rasa X
RASA_X_HOST_SCHEMA=#Rasa X address schema (http/https)
```

To run unit tests for custom actions:

```
make test-actions
```

To ensure proper database cleanup during testing, you will need to include a connection URL for your tracker store database in your .env file e.g.
```
TRACKER_DB_URL=postgresql:///tracker
```
This is not necessary for running the actions.

## ⚫️ Code Style

To ensure a standardized code style we use the formatter [black](https://github.com/ambv/black).

If you want to automatically format your code on every commit, you can use [pre-commit](https://pre-commit.com/).
Just install it via `pip install pre-commit` and execute `pre-commit install` in the root folder.
This will add a hook to the repository, which reformats files on every commit.

To reformat files manuallly execute
```
make formatter
```

## :gift: License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/main/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.
