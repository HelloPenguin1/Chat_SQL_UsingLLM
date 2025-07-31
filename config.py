import streamlit as st
from pathlib import Path
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
import sqlite3

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

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