# Rasa Demo bot 
[![Build Status](https://travis-ci.com/RasaHQ/rasa-demo.svg?branch=master)](https://travis-ci.com/RasaHQ/rasa-demo)

## :surfer: Introduction
The purpose of this repo is to help you build a cool bot with Rasa.

It's the alpha version of the bot that supports two user goals:
- Subscribing to the Rasa newsletter
- Placing a request for a call with Rasa's sales team

If you want to read more about why we made it and try chatting to it, you can
find it [here](http://rasa.com/docs/getting-started/demobot/)

You can find planned enhancements for the demo in the
[Project Board](https://github.com/RasaHQ/rasa-demo/projects/1)

## 🤖 Installation + Running of the bot

To install the bot, please clone the repo and run:

```
cd website-demo
pip install -e .
```
This will install the bot and all of its requirements.
Note that it was written in Python 3 so might not work with PY2.

To train the core model: `make train-core`

To train the NLU model: `make train-nlu`

To run the bot with both these models:
```
docker run -p 8000:8000 rasa/duckling
make run-cmdline
```

There are some custom actions that require connections to external services,
specifically `ActionSubscribeNewsletter` and `ActionStoreSalesInfo`. For these
to run you would need to have your own MailChimp newsletter and a Google sheet
to connect to.

If you would like to run the bot on the website, you need to install the great
[Rasa Addons](https://github.com/mrbot-ai/rasa-addons) repo:
```
pip install git+https://github.com/mrbot-ai/rasa-addons@0.3.3
```
Then follow the instructions [here](https://github.com/mrbot-ai/rasa-webchat)
to place the chat widget on your website.

## 👩‍💻 Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu` - contains example NLU training data

`demo` - contains custom action/api code

`domain.yml` - the domain file for Core

`nlu_tensorflow.yml` - the NLU config file


## :gift: License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/master/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.
