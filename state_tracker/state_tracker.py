from loguru import logger


class StateTracker:
    def __init__(self, questions, validation_agent):
        self.questions = questions
        self.current_question_index = 0
        self.answers = []
        self.validation_agent = validation_agent

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None

    def validate_answer(self, question, answer):
        try:
            return self.validation_agent.validate(question, answer)
        except Exception as e:
            logger.error(f"Error in StateTracker validate_answer: {e}")
            raise

    def record_answer(self, answer):
        try:
            question = self.get_next_question()
            print(question)
            print(answer)
            if self.validate_answer(question, answer):
                self.answers.append(answer)
                self.current_question_index += 1
                return True
            return False
        except Exception as e:
            logger.error(f"Error in StateTracker record_answer: {e}")
            raise

    def is_complete(self):
        try:
            return self.current_question_index >= len(self.questions)
        except Exception as e:
            logger.error(f"Error in StateTracker is_complete: {e}")
            raise
