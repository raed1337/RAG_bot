from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger

from setting import settings

api_key = settings.api_key


class Agent:
    """
    Base class for all agents.

    Attributes:
        llm (OpenAI): The OpenAI language model.
    """

    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """
        Initializes the Agent with a specified OpenAI model.

        Args:
            model_name (str): The name of the OpenAI model to use.

        Raises:
            ValueError: If the OpenAI API key is not set in the environment variables.
            Exception: If there is an error initializing the OpenAI model.
        """

        try:
            self.llm = ChatOpenAI(model=model_name, api_key=api_key)
        except Exception as e:
            logger.error(f"Error initializing OpenAI model: {e}")
            raise

    def create_chain(self, template: dict) -> LLMChain:
        """
        Creates an LLMChain using a specified prompt template.

        Args:
            template (dict): The prompt template configuration.

        Returns:
            LLMChain: The created LLMChain.
        """

        try:
            prompt_template = PromptTemplate(
                input_variables=template["input_variables"],
                template=template["template"],
            )
            return LLMChain(llm=self.llm, prompt=prompt_template)
        except Exception as e:
            logger.error(f"Error creating LLMChain: {e}")
            raise

    def run(self, chain, **kwargs) -> str:
        """
        Runs the LLMChain with provided arguments.

        Args:
            chain (LLMChain): The LLMChain to run.
            **kwargs: Additional arguments for the LLMChain.

        Returns:
            str: The result of running the LLMChain.
        """
        try:
            return chain.run(**kwargs)
        except Exception as e:
            logger.error(f"Error running LLMChain: {e}")
            raise
