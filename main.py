import warnings

from loguru import logger

from agents.greeting_agent import GreetingAgent
from agents.identification_agent import IdentificationAgent
from agents.investigation_agent import InvestigationAgent
from agents.recomendation_agent import RecommendationAgent
from agents.summarization_agent import SummarizationAgent
from agents.validation_agent import ValidationAgent
from utilities.utility import read_json_and_extract_keys

warnings.filterwarnings("ignore")


class ChatBot:
    def __init__(self):
        self.greeting_agent = GreetingAgent()
        self.identification_agent = IdentificationAgent()
        self.validation_agent = ValidationAgent()
        self.investigation_agent = InvestigationAgent(
            questions=[
                "What is the nature of the problem?",
                "When did the problem start?",
                "Who is involved in the problem?",
                "What steps have you taken to resolve the problem?",
            ],
            validation_agent=self.validation_agent,
        )
        self.summarization_agent = SummarizationAgent()
        self.recommendation_agent = RecommendationAgent()

    def start_conversation(self):
        try:
            # Step 1: Greet the user
            greeting = "Hello! How can I help you today? I am your assistant human resource manager."
            print(greeting)

            # Step 2: Identify the user's request or problem
            user_input = input("You: ")
            identification = self.greeting_agent.greet(user_input=user_input)
            print(f"Bot: {identification}")

            if "problem" in identification.lower():
                # Step 2: Identify the problem nature
                identification = self.identification_agent.identify(
                    user_input=user_input
                )
                print(f"Bot: {identification}")

                if "absence" in identification.lower():

                    questions_and_recomendation = read_json_and_extract_keys(
                        "data/absence.json", "questions", "recommendation"
                    )
                elif "haressement":
                    questions_and_recomendation = read_json_and_extract_keys(
                        "data/hrassement.json", "questions", "recommendation"
                    )

                self.investigation_agent = InvestigationAgent(
                    questions=questions_and_recomendation["questions"],
                    validation_agent=self.validation_agent,
                )
                # Step 3: Investigate the problem
                conversation_history = user_input
                while not self.investigation_agent.is_complete():
                    question = self.investigation_agent.investigate()
                    if question:
                        print(f"Bot: {question}")
                        conversation_history += f"\nAgent: {question}"
                        user_response = input("You: ")
                        conversation_history += f"\nUser: {user_response}"
                        if not self.investigation_agent.record_answer(user_response):
                            print("Bot: Please provide a relevant and valid answer.")

                # Step 4: Summarize the conversation
                summary = self.summarization_agent.summarize(
                    conversation_history=conversation_history
                )
                print(f"Bot: {summary}")

                # Step 5: Provide recommendations
                recommendations = self.recommendation_agent.recommend(
                    summary=summary,
                    recommendation=questions_and_recomendation["recommendation"],
                )
                print(f"Bot: {recommendations}")
            else:
                # Handle general information requests
                print("Bot: How can I assist you with general information?")
        except Exception as e:
            logger.error(f"Error in ChatBot conversation: {e}")
            raise


if __name__ == "__main__":
    logger.add("chatbot.log", rotation="1 MB")
    chatbot = ChatBot()
    chatbot.start_conversation()
