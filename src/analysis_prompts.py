from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def summarize_api(llm, yaml):
    template = """Can you summarize what the API described in the yaml does.
    Provide a step by step analysis of its inputs and outputs.
    Keep the summary concise.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)


def describe_test_cases(llm, api_summary):
    template = """Using the API summary, can you describe 5 test cases that should be covered when writing automated 
    tests for this API. Provide your answer in bullet point format.

    ```{summary}```
    """

    prompt = PromptTemplate(template=template, input_variables=["summary"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(summary=api_summary)


def provide_example_curl_data(llm, yaml):
    template = """Using the API definition from the provided yaml, can you provide an example curl request and 
    an expected response for the specified endpoint.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)


def batch_create_example(llm, yaml):
    template = """Using the API definition from the provided yaml, can you provide example python code that will
    create 100 pets with different names and tags.

    ```{yaml}```
    """

    prompt = PromptTemplate(template=template, input_variables=["yaml"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain.run(yaml=yaml)
