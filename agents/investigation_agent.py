from loguru import logger

from agents.agent import Agent
from agents.validation_agent import ValidationAgent
from state_tracker.state_tracker import StateTracker


class InvestigationAgent(Agent):
    """
    Agent responsible for investigating the user's problem.
    """

    def __init__(self, questions: list, validation_agent: ValidationAgent):
        """
        Initializes the InvestigationAgent with a list of questions and a validation agent.

        Args:
            questions (list): List of questions to ask during the investigation.
            validation_agent (ValidationAgent): The agent to validate answers.
        """
        try:
            super().__init__()
            self.state_tracker = StateTracker(questions, validation_agent)
            self.chain = self.create_chain(
                {
                    "input_variables": ["identified_problem"],
                    "template": """
                    You have identified the problem as: {identified_problem}
                    Please ask one question at a time to investigate the problem thoroughly.
                """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing InvestigationAgent: {e}")
            raise

    def investigate(self) -> str:
        """
        Retrieves the next question to ask.

        Returns:
            str: The next question.
        """
        try:
            return self.state_tracker.get_next_question()
        except Exception as e:
            logger.error(f"Error in InvestigationAgent investigate: {e}")
            raise

    def record_answer(self, answer: str) -> bool:
        """
        Records the user's answer and validates it.

        Args:
            answer (str): The user's answer.

        Returns:
            bool: True if the answer is valid and recorded, False otherwise.
        """
        try:
            return self.state_tracker.record_answer(answer)
        except Exception as e:
            logger.error(f"Error in InvestigationAgent record_answer: {e}")
            raise

    def is_complete(self) -> bool:
        """
        Checks if the investigation is complete.

        Returns:
            bool: True if the investigation is complete, False otherwise.
        """
        try:
            return self.state_tracker.is_complete()
        except Exception as e:
            logger.error(f"Error in InvestigationAgent is_complete: {e}")
            raise
