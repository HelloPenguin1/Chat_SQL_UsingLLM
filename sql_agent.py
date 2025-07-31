from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

from config import llm_model

def create_agent(db):
    # Defining a toolkit
    toolkit = SQLDatabaseToolkit(db=db, llm=llm_model)
    
    # Defining an agent
    agent = create_sql_agent(
        llm=llm_model,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
    )
    return agent
