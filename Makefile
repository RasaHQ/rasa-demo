.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    train"
	@echo "        Train a Rasa model."
	@echo "    run-cmdline"
	@echo "        Starts the bot on the command line"
	@echo "    visualize"
	@echo "        Saves the story graphs into a file"

run-actions:
	rasa run actions --actions demo.actions

train:
	rasa train

train-memo:
	rasa train core --domain domain.yml --stories data/core --config augmentedmemo-only.yml --out models/dialogue --augmentation 0 --quiet

run-cmdline:
	make run-actions&
	rasa shell --debug --endpoints endpoints.yml

visualize:
	rasa visualize --stories data/core/ --domain domain.yml --out story_graph.png

evaluate-core:
	rasa test core --model models/dialogue --stories data/core/ --fail-on-prediction-errors --quiet