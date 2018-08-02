from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.featurizers import \
    MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy


agent = Agent('domain.yml', policies=[
        MemoizationPolicy(max_history=6),
        KerasPolicy(MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(),
                                                max_history=6)),
        FallbackPolicy(nlu_threshold=0.8, core_threshold=0.3)])

training_data = agent.load_data('data/core/')

agent.train(training_data, epochs=200)
agent.persist('models/dialogue')
