from llama_index.core import PromptTemplate
from langfuse import Langfuse
from config import PROMPT_TEMPLATE

# custom prompt template
langfuse = Langfuse()


def get_template():
    prompt = langfuse.get_prompt(PROMPT_TEMPLATE)
    template = prompt.compile()
    qa_template = PromptTemplate(template)
    return qa_template
