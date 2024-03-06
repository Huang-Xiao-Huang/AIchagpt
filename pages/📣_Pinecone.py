import  streamlit as st

#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ''

st.set_page_config(
    page_title="Pinecone Settings",layout="wide"
)
#标题
st.title("Pinecone Settings")

#获取apikey
pinecone_api_key = st.text_input(
    "API Key" ,value=st.session_state["OPENAI_API_KEY"],max_chars=None,key=None,type="default"
)
enviroment = st.text_input(
    "Enviroment",value=st.session_state["PINECONE_ENVIRONMENT"],max_chars=None,key=None,type="default"
)

saved = st.button(
    "Save"
)

if saved:
    st.session_state["OPENAI_API_KEY"]  = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"]  = enviroment