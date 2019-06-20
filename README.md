# Sara - the Rasa Demo Bot
[![Build Status](https://travis-ci.com/RasaHQ/rasa-demo.svg?branch=master)](https://travis-ci.com/RasaHQ/rasa-demo)

## :surfer: Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.

Sara is an alpha version and lives in our docs (temporarily she's unavailable on the docs due to maintenance), helping developers getting started with our open source tools. It supports the following user goals:

- Understanding the Rasa framework
- Installing the Rasa framework
- Answering some FAQs around Rasa
- Subscribing to the Rasa newsletter
- Requesting a call with Rasa's sales team
- Handling basic chitchat

You can talk to Sara [here](https://rasa.com/docs/get_started_step1/) (temporarily unavailable) and find planned enhancements for Sara in the
[Project Board](https://github.com/RasaHQ/rasa-demo/projects/1)

## 🤖 How to install and run Sara

To install Sara, please clone the repo and run:

```
cd rasa-demo
pip install -e .
```
This will install the bot and all of its requirements.
Note that it was written in Python 3 so might not work with PY2.

To train the model: `make train` (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`)

To run Sara with both these models:
```
docker run -p 8000:8000 rasa/duckling
make run-cmdline
```

There are some custom actions that require connections to external services,
specifically `ActionSubscribeNewsletter` and `ActionStoreSalesInfo`. For these
to run you would need to have your own MailChimp newsletter and a Google sheet
to connect to.

If you would like to run Sara on your website, follow the instructions
[here](https://github.com/mrbot-ai/rasa-webchat) to place the chat widget on
your website.

## 👩‍💻 Overview of the files

`data/core/` - contains stories 

`data/nlu` - contains example NLU training data

`demo` - contains custom action/api code

`domain.yml` - the domain file 

`config.yml` - the Rasa config file

### Code Style

To ensure a standardized code style we use the formatter [black](https://github.com/ambv/black).

If you want to automatically format your code on every commit, you can use [pre-commit](https://pre-commit.com/).
Just install it via `pip install pre-commit` and execute `pre-commit install` in the root folder.
This will add a hook to the repository, which reformats files on every commit.

If you want to set it up manually, install black via `pip install black`.
To reformat files execute
```
black .
```

## :gift: License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/master/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.
