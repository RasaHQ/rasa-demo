from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from demo import config

from rasa_core.channels.rest import HttpInputChannel


logger = logging.getLogger()  # get the root logger


def run_remote():
    from rasa_core.remote import RemoteAgent

    logging.basicConfig(level="DEBUG")

    from rasa_extensions.core.channels.rasa_chat import RasaChatInput

    rasa_in = RasaChatInput(config.platform_api)
    input_channel = HttpInputChannel(config.self_port, "/",
                                     rasa_in)

    agent = RemoteAgent.load(config.core_model_dir,
                             config.remote_core_endpoint,
                             config.rasa_core_token
                             )

    agent.handle_channel(input_channel)


if __name__ == "__main__":

    run_remote()
