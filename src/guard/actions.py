import logging
import sys

import chromadb
from llama_index.core import (
    Settings,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext
)
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.base.response.schema import StreamingResponse

from nemoguardrails.actions import action
from nemoguardrails import LLMRails, RailsConfig

from src.observability import init_observability
from src.prompts import get_template
from src.config import *

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

query_engine_cache = None
global rails


def chat(input_question):
    global rails
    res = rails.generate(prompt=input_question)
    return res


def init_llm():
    global rails
    llm = Ollama(model=LLM_MODEL, request_timeout=REQUEST_TIMEOUT, temperature=0.2)
    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)

    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = CHUNK_SIZE
    Settings.chunk_overlap = CHUNK_OVERLAP
    init_observability()

    guard = RailsConfig.from_path("./guard")
    rails = LLMRails(guard)


def init_index():
    reader = SimpleDirectoryReader(input_dir=DOCUMENTS_DIR, recursive=True)
    documents = reader.load_data()

    logging.info("index creating with `%d` documents", len(documents))

    chroma_client = chromadb.EphemeralClient()
    chroma_collection = chroma_client.create_collection(COLLECTION_NAME)

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # use this to set custom chunk size and splitting
    # https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/

    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

    return index


def init_query_engine():
    global query_engine_cache
    if query_engine_cache is not None:
        print('Using cached query engine')
        return query_engine_cache
    # memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

    index = init_index()
    # custom prompt template
    qa_template = get_template()

    # build query engine with custom template
    # text_qa_template specifies custom template
    # similarity_top_k configure the retriever to return the top 3 most similar documents,
    # the default value of similarity_top_k is 2
    query_engine_cache = index.as_query_engine(
        streaming=True,
        text_qa_template=qa_template,
        similarity_top_k=3
    )
    return query_engine_cache


def get_query_response(response) -> str:
    """
    Function to query based on the query_engine and query string passed in.
    """
    if isinstance(response, StreamingResponse):
        typed_response = response.get_response()
    else:
        typed_response = response
    response_str = typed_response.response
    if response_str is None:
        return ""
    return response_str


@action(is_system_action=True)
def user_query(context):
    query_engine = init_query_engine()

    user_message = context.get("user_message")
    print('user_message is ', user_message)
    response = query_engine.query(user_message)
    return get_query_response(response)
