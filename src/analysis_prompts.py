from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama


def important_message():
    # Temp model
    # https://python.langchain.com/docs/integrations/llms/ollama
    llm_tmp = Ollama(model="llama2")
    prompt = """Sing Happy Birthday to Paula. And mention shes from Mayo which is not as good as Dublin."""
    return llm_tmp(prompt)


def summarize_api(llm, yaml):
    template = """Summarize the API described in the provided yaml.
    Generate a step by step analysis of its inputs and outputs.
    Include all http methods, including POST endpoints.
    Keep the summary concise.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)


def describe_test_cases(llm, api_summary):
    template = """Using the API summary, describe 5 test cases that should be covered when writing automated 
    tests for this API. Provide your answer in bullet point format.

    ```{summary}```
    """

    prompt = PromptTemplate(template=template, input_variables=["summary"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(summary=api_summary)


def provide_example_curl_data(llm, yaml):
    template = """Using the API definition from the provided yaml, generate example curl GET, POST and DELETE requests.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)


def batch_create_example(llm, yaml):
    template = """Using the API definition from the provided yaml, step by step generate example kotlin code that will
    use the API to create 100 pets with different names and tags.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)
