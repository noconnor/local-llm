import streamlit as st
import base64
import os
import diff_analyser


def open_pdf(file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, file)
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        return f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'


st.write("Example demo app on how to summarise changes between different versions of a pdf")

with st.expander("Show Document v1"):
    st.markdown(open_pdf("v1.pdf"), unsafe_allow_html=True)

with st.expander("Show Document v2"):
    st.markdown(open_pdf("v2.pdf"), unsafe_allow_html=True)

with st.spinner(text=f"Generating Summary Of Changes...",  cache=True):
    # Use the model to generate a summary
    text = diff_analyser.summarise_changes()
    st.markdown(text)
