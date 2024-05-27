from loguru import logger

from agents.agent import Agent


class ValidationAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["question", "answer"],
                    "template": """
                    Question Q: {question}
                    Answer A : {answer}
                    Please evaluate if the answer A is relevant and represnet a potentialanswer to the question Q. Respond with "valid" or "invalid".
                """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing ValidationAgent: {e}")
            raise

    def validate(self, question, answer):
        try:
            validation_result = self.run(self.chain, question=question, answer=answer)
            print(validation_result)
            return False if "invalid" in validation_result.lower() else True
        except Exception as e:
            logger.error(f"Error in ValidationAgent validate: {e}")
            raise
