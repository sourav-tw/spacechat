from llama_index.core import PromptTemplate
from langfuse import Langfuse
from src.config import PROMPT_TEMPLATE
from src.langfuse_integration import is_langfuse_enabled


def get_template():
    if is_langfuse_enabled() is True:
        langfuse = Langfuse()
        try:
            prompt = langfuse.get_prompt(PROMPT_TEMPLATE)
        except Exception as e:
            print("Error in getting prompt template - ", e)
            return None
        template = prompt.compile()
        qa_template = PromptTemplate(template)
        return qa_template
    return None
