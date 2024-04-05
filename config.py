import os

# define init index
INIT_INDEX = os.getenv('INIT_INDEX', 'false').lower() == 'true'

# vector index persist directory
INDEX_PERSIST_DIRECTORY = os.getenv('INDEX_PERSIST_DIRECTORY', "./data/chromadb")

# http api port
HTTP_PORT = os.getenv('HTTP_PORT', 5000)

LLM_MODEL = os.getenv('LLM_MODEL', "mistral")

EMBED_MODEL = os.getenv('EMBED_MODEL', "BAAI/bge-small-en-v1.5")

CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))

CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 150))

REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 60))

DOCUMENTS_DIR = os.getenv('DOCUMENTS_DIR', "./docs")

COLLECTION_NAME = os.getenv('COLLECTION_NAME', "space-chat")

PROMPT_TEMPLATE = os.getenv('PROMPT_TEMPLATE', "SPACE_CHAT_PROMPT")