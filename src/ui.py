import streamlit as st
import analysis_prompts as prompts
import os
from langchain.llms import Ollama

st.write("Example demo app on how to use use local Ollama models.")

st.write("Note on [\"Hallucinations\"](https://x.com/karpathy/status/1733299213503787018?s=46)")

# Loads model into RAM
# This is using Facebook's llama model (7B params - i.e. the smallest model available)
# It takes about 4GB of RAM to run.
# Larger models will perform better.
# When using this model, calls will be made to localhost:11434/ but will not be sent to any remote endpoints
llm = Ollama(model="llama2")

# Loads an example API yaml file
# You'd probably want to split this up into chunks before sending it to the model
# as the model will have a limit on how much context it can handle
dir_path = os.path.dirname(os.path.realpath(__file__))
yaml = open(os.path.join(dir_path, 'example_api.yaml'), 'r').read()


with st.spinner(text="Generating Message...",  cache=True):
    # Use the model to generate a very important message
    message = prompts.important_message()

with st.expander("Show Important message"):
    st.markdown(message)

with st.expander("Show API yaml"):
    st.markdown("```" + yaml + "```")

with st.spinner(text="Generating Summary...",  cache=True):
    # Use the model to generate a summary of the yaml.
    summary = prompts.summarize_api(llm, yaml)

with st.expander("Show Summary"):
    st.markdown(summary)

with st.spinner(text="Generating Test cases...",  cache=True):
    # Use the summary from previous stage to generate a set of test cases
    # You could pass the yaml in here to see if you get better results
    test_cases = prompts.describe_test_cases(llm, summary)

with st.expander("Show Test Cases"):
    st.markdown(test_cases)

with st.spinner(text="Generating curl example...",  cache=True):
    # Use yaml to generate example curl & expected response
    example_curl = prompts.provide_example_curl_data(llm, yaml)

with st.expander("Show curl data"):
    st.markdown(example_curl)

with st.spinner(text="Generating code example...",  cache=True):
    # Use yaml to generate example kotlin batch upload request
    example_kotlin = prompts.batch_create_example(llm, yaml)

with st.expander("Show kotlin code"):
    st.markdown(example_kotlin)




