import streamlit as st
from langchain.callbacks.streamlit import StreamlitCallbackHandler
from dotenv import load_dotenv
load_dotenv()
import os
from config import configure_db, LOCALDB, MYSQL, LOCALDB, MYSQL
from sql_agent import create_agent

st.set_page_config(page_title="Langchain: Chat with SQL DB")
st.title("LangChain: Chat with SQL DB")


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

## initiating chat message
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state['messages']=[
        {"role": "assistant","content": "How may I help you?"}
    ]

# display every message in chat bubble message format
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query= st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):

        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = create_agent(db).run(user_query,
                                        callbacks=[st_cb])

        st.session_state.messages.append({"role":"assistant", "content": response})

        st.write(response)
