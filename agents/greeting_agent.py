from loguru import logger

from agents.agent import Agent


class GreetingAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["user_input"],
                    "template": """
                    The user said: {user_input}
                    Please identify if the user is asking for general information or reporting a problem. Respond with "general information" or "problem".
                """,
                }
            )

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def greet(self, user_input):
        try:
            return self.run(self.chain, user_input=user_input)
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
