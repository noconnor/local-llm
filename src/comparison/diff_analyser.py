import os
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.llms import Ollama

# Find what directory this file is located in
dir_path = os.path.dirname(os.path.realpath(__file__))


def load_pdfs():
    # TODO: Look into better ways to combine these documents, you ultimately want to end up with a big blob of text
    #  with some markers that the model can compare.

    v1 = PyPDFLoader(os.path.join(dir_path, 'v1.pdf'))
    v1_docs = v1.load_and_split()

    v2 = PyPDFLoader(os.path.join(dir_path, 'v2.pdf'))
    v2_docs = v2.load_and_split()

    # TODO: Add logic to figure out which is the larger docs before combining - this will only currently work if v2
    #  docs list is bigger than v1
    changes = []
    for i, j in enumerate(v2_docs):
        if i < len(v1_docs):
            before = v1_docs[i]
            after = j.page_content
            diff = f"Version1: {before} \n\n Version2: {after} \n\n"
            changes.append(Document(page_content=diff))
        else:
            before = ""
            after = j.page_content
            diff = f"Version1: {before} \n\n Version2: {after} \n\n"
            changes.append(Document(page_content=diff))

    return changes


def summarise_changes():

    llm = Ollama(model='mistral')  # could try llama2 model

    docs = load_pdfs()

    prompt_template = """Write a concise bullet point summary of changes between the two texts provided.
    Specifically compare the text labelled Version1 with the text labelled Version2 and provide summary of the changes 
    made in the Version2 text.
    If there are no changes between the texts, dont produce any result.
    {text}
    CONCISE SUMMARY OF CHANGES:"""
    prompt = PromptTemplate(input_variables=["text"], template=prompt_template)

    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    summary = chain.run(docs)

    return summary


if __name__ == "__main__":
    print(summarise_changes())
