from loguru import logger

from agents.agent import Agent


class RecommendationAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["summary", "recommendation"],
                    "template": """
                    Based on the following summary, provide recommendations to solve the problem:
                    {summary}

                    Here you can find relevant information to use for the recomendations:
                    {recommendation}
                """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing RecommendationAgent: {e}")
            raise

    def recommend(self, summary, recommendation):
        try:
            return self.run(self.chain, summary=summary, recommendation=recommendation)
        except Exception as e:
            logger.error(f"Error in RecommendationAgent recommend: {e}")
            raise
