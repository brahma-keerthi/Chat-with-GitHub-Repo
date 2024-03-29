import streamlit as st
import utils
import os
local = True
if local:
    from dotenv import load_dotenv
    load_dotenv()

st.title("Chat with GitHub Repository")

## Get some user inputs
# user_key = st.text_input("Enter your OpenAI Key", "")
# if user_key:
#     os.environ['OPENAI_API_KEY'] = user_key
# else:
#     user_key = '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'
#     os.environ['OPENAI_API_KEY'] = user_key

user_repo = st.text_input("Enter GitHub public repo link")
if user_repo:
    st.write("You entered:", user_repo)

    ## Load the Github Repo
    embedder = utils.Embedder(user_repo)
    embedder.clone_repo()
    st.write("Your repo has been cloned")

    ## Chunk and Create DB
    st.write("Parsing the content and embedding it. This may take some time")
    embedder.load_db()
    st.write("Done Loading. Ready to take your questions")

    # # Initialize chat history
    # if "messages" not in st.session_state:
    #     st.session_state.messages = []

    # # Display chat messages from history on app rerun
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

    # Accept user input and display the results
    prompt = st.text_input("Type your question here.")
    if prompt:
        response = embedder.retrieve_results(prompt)
        st.write(response)
        