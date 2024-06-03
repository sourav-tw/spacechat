from llama_index.core import PromptTemplate
from langfuse import Langfuse
from src.config import PROMPT_TEMPLATE
from src.observability import is_observability_enabled


def get_template():
    if is_observability_enabled() is True:
        observability = Langfuse()
        try:
            prompt = observability.get_prompt(PROMPT_TEMPLATE)
        except Exception as e:
            print("Error in getting prompt template - ", e)
            return None
        template = prompt.compile()
        qa_template = PromptTemplate(template)
        return qa_template
    return None
