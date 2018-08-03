.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Spin up a server that serves as an endpoint to receive facebook user messages."

train-nlu:
	python3 -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data data/nlu/nlu.json -o models --project nlu --verbose

train-core:
	python3 demo/train_core.py

run:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/default/current -p 5002 -c facebook --credentials credentials.yml

run-cmdline:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug

visualize:
	python3 -m rasa_core.visualize -s stories.md -d domain.yml -o story_graph.png
