import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os
from config import configure_db

st.set_page_config(page_title="Langchain: Chat with SQL DB")
st.title("LangChain: Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

#user selects an option

radio_opt = ["Use SQLite 3 Database- Student.db", "Connect to your own SQL Database"]

selected_opt = st.sidebar.radio(label="Choose the DB which you want to chat", options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide MySQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("Enter your MySQL password", type="password")
    mysql_db = st.sidebar.text_input("MySQL database")
else:
    db_uri = LOCALDB


api_key = os.getenv("GROQ_API_KEY")



if not db_uri:
    st.info("Please enter the database information and uri")


## LLM Model
llm = ChatGroq(api_key=api_key,
               model_name = 'Llama3-8b-8192',
               streaming = True)



if db_uri==MYSQL:
    db=configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)


    