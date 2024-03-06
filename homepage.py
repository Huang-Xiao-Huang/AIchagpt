import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os
# os.environ["http_proxy"] = "http://localhost:7890"
# os.environ["https_proxy"] = "http://localhost:7890"
# os.environ["http_proxy"] = 'http://127.0.0.1:7890'
# os.environ["https_proxy"] = 'https://127.0.0.1:7890'

chat = None

#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
else:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ''

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ''

st.set_page_config(
    page_title="Wecome to Openai",
    layout= "wide"
)
#目录
st.title("😀  欢迎来到 OpenAI 😀 ")
st.subheader("大语言模型")

with st.container():
    st.header("Openai Settings")
    st.markdown(
        f'''
        | Openai api key |
        |-----------------------|
        |{st.session_state["OPENAI_API_KEY"]}|
        '''
    )


#维护会话状态
if "messages" not in st.session_state:
    st.session_state["messages"] = []



#主页逻辑的信息
if chat:
    with st.container():
        st.header("Chat with GPT")
       # 对话历史记录
        for message in st.session_state["messages"]:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
        #聊天输入框
        Prompt = st.chat_input("Type something...")
        if Prompt:
            st.session_state["messages"].append(
                HumanMessage(content=Prompt)
            )
            with st.chat_message("user"):
                st.markdown(Prompt)
            with st.spinner("AI正在思考中，请稍等..."):
                ai_answer = chat([HumanMessage(content=Prompt ) ])
                st.session_state["messages"].append(ai_answer)
                with st.chat_message("assistant"):
                    st.markdown(
                        ai_answer.content
                    )
else:
    with st.container():
        st.warning(
            "请在页面设置你的apikey"
        )



