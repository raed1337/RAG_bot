from loguru import logger

from agents.agent import Agent


class IdentificationAgent(Agent):
    """
    Agent responsible for identifying the user's request or problem.
    """

    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["user_input"],
                    "template": """
                    The user said: {user_input}
                    Please identify if the user is asking for general information or reporting a problem. Respond with "absence" or "haressement".
                """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing IdentificationAgent: {e}")
            raise

    def identify(self, user_input):

        try:
            return self.run(self.chain, user_input=user_input)
        except Exception as e:
            logger.error(f"Error in IdentificationAgent identify: {e}")
            raise
