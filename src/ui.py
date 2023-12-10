import streamlit as st
import analysis_prompts as prompts
import os
from langchain.llms import Ollama

# See engine.py for annotated code

st.write("Example LLama usage for swagger API analysis")

llm = Ollama(model="llama2")

dir_path = os.path.dirname(os.path.realpath(__file__))
yaml = open(os.path.join(dir_path, 'example_api.yaml'), 'r').read()

with st.expander("Show API yaml"):
    st.markdown("```" + yaml + "```")

with st.spinner(text="Generating Summary...",  cache=True):
    summary = prompts.summarize_api(llm, yaml)

with st.expander("Show Summary"):
    st.markdown(summary)

with st.spinner(text="Generating Test cases...",  cache=True):
    test_cases = prompts.describe_test_cases(llm, yaml)

with st.expander("Show Test Cases"):
    st.markdown(test_cases)




