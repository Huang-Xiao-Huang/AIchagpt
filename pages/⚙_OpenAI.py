import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


import os,time
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

chat = None
#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
elif st.session_state["OPENAI_API_KEY"] != '':
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ''

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ''

st.set_page_config(
    page_title="Wecome to Openai",
    layout= "wide",
    page_icon="机器人👀"
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
        prompt = st.chat_input("输入信息")
        if prompt:
            st.session_state["messages"].append(
                HumanMessage(content=prompt)
            )
            with st.chat_message("user"):
                st.markdown(prompt)
                # st.write(f'{prompt}')
            with st.spinner("AI正在思考中，请稍等..."):
                ai_answer = chat([HumanMessage(content=prompt ) ])
                st.session_state["messages"].append(ai_answer)
                with st.chat_message("assistant"):
                    # st.markdown(
                    #     ai_answer.content
                    # )
                        out = st.empty()
                        str_= ""
                        for i in ai_answer.content:
                            str_ += str(i)
                            out.markdown(str_)
                            time.sleep(0.03)
else:
    with st.container():
        st.warning(
            "请在OPENAI页面输入你的apikey"
        )

# import streamlit as st

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")

