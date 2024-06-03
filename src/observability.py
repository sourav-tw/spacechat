import logging
from langfuse.llama_index import LlamaIndexCallbackHandler
from llama_index.core.callbacks import CallbackManager
from llama_index.core import Settings
from src.config import LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY


def init_observability():
    if is_observability_enabled() is False:
        logging.warning("LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY is not set in the environment variables")
        return None
    print('Integrating Langfuse...')
    observability_callback_handler = LlamaIndexCallbackHandler()
    Settings.callback_manager = CallbackManager([observability_callback_handler])
    print('Langfuse integrated successfully!')
    return


def is_observability_enabled():
    return LANGFUSE_PUBLIC_KEY is not None and LANGFUSE_SECRET_KEY is not None
