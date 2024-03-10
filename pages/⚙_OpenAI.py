import  streamlit as st
# import os


#如果openai没有在会话中(会话的作用是存储一些历史信息),则设置为空
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''

#页面设置
st.set_page_config(page_title="OpenAI Settings",layout= "wide")

#标题
st.title("Openai Settings")
#输入APi密钥
openai_api_key = st.text_input("API Key",
              value=st.session_state["OPENAI_API_KEY"],
              max_chars=None,key=None,type="password")

#提交保存按钮
saved= st.button(
    "Save😀"
)
if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key
    st.write(openai_api_key)

