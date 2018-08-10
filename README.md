# Rasa Demo bot

## :surfer: Introduction
The purpose of this repo is to help you build a cool bot with Rasa.

It's the alpha version of the bot that supports two user goals:
- Subscribing to the newsletter
- Placing a request for a call with the sales team

You can find planned enhancement for the demo in the [Project Board](https://github.com/RasaHQ/killer-demo/projects/1)

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

## 👩‍💻 Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu` - contains example NLU training data

`demo` - contains custom action/api code

`domain.yml` - the domain file for Core

`nlu_tensorflow.yml` - the NLU config file


## :gift: License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies GmbH. [Copy of the license](https://github.com/RasaHQ/killer-demo/blob/master/LICENSE). Licensees may convey the work under this license. There is no warranty for the work.
