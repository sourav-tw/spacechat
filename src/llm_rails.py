from nemoguardrails import LLMRails, RailsConfig


def init_llm_rails():
    config = RailsConfig.from_path("./rails_config")
    rails = LLMRails(config=config)
    return rails
