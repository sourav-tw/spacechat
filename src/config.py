import os
from dotenv import load_dotenv

load_dotenv()

HTTP_PORT = os.getenv('HTTP_PORT', 5000)

LLM_MODEL = os.getenv('LLM_MODEL', "llama3")

EMBED_MODEL = os.getenv('EMBED_MODEL', "BAAI/bge-small-en-v1.5")

CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))

CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 150))

REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 60))

DOCUMENTS_DIR = os.getenv('DOCUMENTS_DIR', "../docs")

COLLECTION_NAME = os.getenv('COLLECTION_NAME', "space-chat")

PROMPT_TEMPLATE = os.getenv('PROMPT_TEMPLATE', "SPACE_CHAT_PROMPT")

LANGFUSE_PUBLIC_KEY = os.getenv('LANGFUSE_PUBLIC_KEY')

LANGFUSE_SECRET_KEY = os.getenv('LANGFUSE_SECRET_KEY')
