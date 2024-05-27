from loguru import logger

from agents.agent import Agent


class SummarizationAgent(Agent):
    """
    Agent responsible for summarizing the conversation.
    """

    def __init__(self):
        """
        Initializes the SummarizationAgent.
        """
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["conversation_history"],
                    "template": """
                    Summarize the following conversation:
                    {conversation_history}
                """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing SummarizationAgent: {e}")
            raise

    def summarize(self, conversation_history: str) -> str:
        """
        Summarizes the given conversation history.

        Args:
            conversation_history (str): The conversation history.

        Returns:
            str: The summary of the conversation.
        """
        try:
            return self.run(self.chain, conversation_history=conversation_history)
        except Exception as e:
            logger.error(f"Error in SummarizationAgent summarize: {e}")
            raise
