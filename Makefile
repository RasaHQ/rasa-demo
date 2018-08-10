.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run-cmdline"
	@echo "        Starts the bot on the command line"
	@echo "    visualize"
	@echo "        Saves the story graphs into a file"

train-nlu:
	python3 -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name current --data data/nlu/ -o models --project nlu --verbose

train-core:
	python3 demo/train_core.py

run-cmdline:
	python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug

visualize:
	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png
