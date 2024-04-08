import logging
from langfuse.llama_index import LlamaIndexCallbackHandler
from llama_index.core.callbacks import CallbackManager
from llama_index.core import Settings
from config import LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY


def init_langfuse():
    if is_langfuse_enabled() is False:
        logging.warning("LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY is not set in the environment variables")
        return None
    print('Integrating Langfuse...')
    langfuse_callback_handler = LlamaIndexCallbackHandler()
    Settings.callback_manager = CallbackManager([langfuse_callback_handler])
    print('Langfuse integrated successfully!')
    return


def is_langfuse_enabled():
    return LANGFUSE_PUBLIC_KEY is not None and LANGFUSE_SECRET_KEY is not None
