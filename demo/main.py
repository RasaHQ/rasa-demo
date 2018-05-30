from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from demo import config

from rasa_core.channels.rest import HttpInputChannel


logger = logging.getLogger()  # get the root logger


def run_remote():
    from rasa_extensions.core.remote import run_with_remote_core

    logging.basicConfig(level="DEBUG")

    from rasa_extensions.core.channels.rasa_chat import RasaChatInput

    rasa_in = RasaChatInput(config.platform_api)
    input_channel = HttpInputChannel(config.self_port, "/",
                                     rasa_in)

    run_with_remote_core(config.core_model_dir,
                         input_channel,
                         config.remote_core_endpoint,
                         config.rasa_core_token
                         )


if __name__ == "__main__":

    run_remote()
