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

from observability import init_observability
from prompts import get_template
from config import *

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

global query_engine
query_engine = None


def init_llm():
    llm = Ollama(model=LLM_MODEL, request_timeout=REQUEST_TIMEOUT)
    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)

    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = CHUNK_SIZE
    Settings.chunk_overlap = CHUNK_OVERLAP
    init_observability()


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


def init_query_engine(index):
    global query_engine
    memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

    # custom prompt template
    qa_template = get_template()

    # build query engine with custom template
    # text_qa_template specifies custom template
    # similarity_top_k configure the retriever to return the top 3 most similar documents,
    # the default value of similarity_top_k is 2
    query_engine = index.as_chat_engine(
        streaming=True,
        text_qa_template=qa_template,
        similarity_top_k=3,
        chat_mode="context",
        memory=memory
    )

    return query_engine


def chat(input_question):
    global query_engine
    response = query_engine.query(input_question)
    return response


# It's a simple chat command line interface
def chat_cmd():
    global query_engine
    while (input_question := input("Enter your question (or 'exit' to quit): ")) != 'exit':
        response = query_engine.stream_chat(input_question)
        response.print_response_stream()


if __name__ == '__main__':
    init_llm()
    index = init_index()
    init_query_engine(index)
    chat_cmd()
