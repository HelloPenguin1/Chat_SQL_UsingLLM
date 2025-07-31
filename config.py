import streamlit as st
from pathlib import Path
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"
api_key = os.getenv("GROQ_API_KEY")

# LLM Model
llm_model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name='Llama3-8b-8192',
    temperature=0.7,
    max_tokens=500,
    streaming=True
)


@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri==LOCALDB:
        # set up the file paht to the db file
        db_filepath = (Path(__file__).parent/"student.db").absolute()
        print(db_filepath)
        creator= lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", uri = True)
        return SQLDatabase(create_engine("sqlite:///", creator = creator))
    
    elif db_uri == MYSQL:
        if not (mysql_db and mysql_host and mysql_user and mysql_password):
            st.error("Please provide all SQL connection details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
    
