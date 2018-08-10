import logging

from demo import config
import os


logger = logging.getLogger()  # get the root logger


def run_remote():
    from rasa_core.remote import RemoteAgent
    from rasa_core.utils import EndpointConfig

    logging.basicConfig(level="DEBUG")

    from rasa_core.channels.rasa_chat import RasaChatInput
    from rasa_addons.webchat import WebChatInput, SocketInputChannel

    # definte the input channels for the platform and the chat widget
    rasa_in = RasaChatInput(config.platform_api)
    widget_in = WebChatInput(static_assets_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'static'))
    input_channel = SocketInputChannel(config.self_port, "/",
                                       rasa_in, widget_in)

    # define the core endpoint
    core_endpoint_config = EndpointConfig(
        url=config.remote_core_endpoint,
        token=config.rasa_core_token
    )

    # define the nlg endpoint
    nlg_endpoint_config = EndpointConfig(
        url=config.rasa_nlg_endpoint,
        token=config.rasa_platform_token
    )

    # start the remote agent
    agent = RemoteAgent.load(config.core_model_dir,
                             core_endpoint=core_endpoint_config,
                             nlg_endpoint=nlg_endpoint_config
                             )

    agent.handle_channel(input_channel)


if __name__ == "__main__":

    run_remote()
