import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
from sqlalchemy import create_engine


st.set_page_config(page_title="🦦 Infrahub 🦦 Agent", page_icon="🦦")
st.title("🦦 Infrahub 🦦 Agent")

INJECTION_WARNING = """
This is an early prototype and is not intended for production use.
"""

st.sidebar.warning(INJECTION_WARNING, icon="⚠️")
# User inputs
infrahub_url = st.sidebar.text_input(
    label="Infrahub URL",
    placeholder="https://localhost:8000",
    key="infrahub_url",
)
infrahub_key = st.sidebar.text_input(
    label="Infrahub API Key",
    type="password",
    key="infrahub_key",
)
openai_api_key = st.sidebar.text_input(
    label="OpenAI API Key",
    type="password",
    key="openai_api_key",
)
radio_opt = ["No", "Yes"]
selected_opt = st.sidebar.radio(
    label="I am aware of the risks.", options=radio_opt, key="accept_risk"
)
if radio_opt.index(selected_opt) == 0:
    st.info("Please accept the risk")
    st.stop()

if not openai_api_key or not infrahub_key:
    st.info("Please add your API keys to continue.")
    st.stop()


# TODO

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask me anything!")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response = "TODO"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
