# services/langchain_service.py

import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import \
    create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI


class LangChainService:
    def __init__(self, api_key: str, file_path: str):
        self.api_key = api_key
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        self.df["job_date"] = pd.to_datetime(self.df["job_date"])
        self.df["date_of_last_day_off_taken"] = pd.to_datetime(
            self.df["date_of_last_day_off_taken"]
        )
        self.agent = self._create_agent()

    def _create_agent(self):
        return create_pandas_dataframe_agent(
            ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", api_key=self.api_key),
            self.df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )

    def get_response(self, query: str) -> str:

        return self.agent.invoke(query)["output"]
