# Sara - the Rasa Demo Bot
[![Build Status](https://travis-ci.com/RasaHQ/rasa-demo.svg?branch=master)](https://travis-ci.com/RasaHQ/rasa-demo)

## :surfer: Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.

Sara is an alpha version and lives in our docs (temporarily she's unavailable on the docs due to maintenance), 
helping developers getting started with our open source tools. It supports the following user goals:

- Understanding the Rasa framework
- Getting started with Rasa
- Answering some FAQs around Rasa
- Subscribing to the Rasa newsletter
- Requesting a call with Rasa's sales team
- Handling basic chitchat

You can find planned enhancements for Sara in the
[Project Board](https://github.com/RasaHQ/rasa-demo/projects/1)

## 👷‍ Installation

To install Sara, please clone the repo and run:

```
cd rasa-demo
pip install -r requirements.txt
pip install -e .
```
This will install the bot and all of its requirements.
Note that this bot should be used with python 3.6 or 3.7.

## 🤖 To run Sara:

Use `rasa train` to train a model (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`).

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions --actions demo.actions
```

There are some custom actions that require connections to external services,
specifically `SubscribeNewsletterForm` and `SalesForm`. For these
to run you would need to have your own MailChimp newsletter and a Google sheet
to connect to.

In another window, run the bot:
```bash
docker run -p 8000:8000 rasa/duckling
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working 
under the hood. To simply talk to the bot, you can remove this flag.

If you would like to run Sara on your website, follow the instructions
[here](https://github.com/mrbot-ai/rasa-webchat) to place the chat widget on
your website.

## 🤖 To run Sara under Docker:

To run Sara locally under docker, do the following:

```
export RASA_VERS=1.5.1
docker run -v $(pwd):/app rasa/rasa:${RASA_VERS}-full train --augmentation 0 --config config_local.yml
docker-compose -f docker-compose-local.yml build
docker-compose -f docker-compose-local.yml up -d
docker run -it --rm --network=$(basename `pwd`)_default -v $(pwd):/app rasa/rasa:${RASA_VERS}-full shell --model /app/models/$(ls models) --endpoints endpoints_local.yml
```

## 👩‍💻 Overview of the files

`data/core/` - contains stories 

`data/nlu` - contains NLU training data

`demo` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

## ⚫️ Code Style

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
