import streamlit as st
from langchain.callbacks import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
load_dotenv()
import os
from config import configure_db
from agent import agent

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


if not db_uri:
    st.info("Please enter the database information and uri")



# Defining the type of database

if db_uri==MYSQL:
    db=configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

