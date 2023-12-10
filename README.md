# llama + langchain

Example code to use langchain library to run queries against an LLama model 


## Setup:

* See install instructions for ollama app: https://ollama.ai/download & from commandline run `ollama pull llama2`
  * Reference: https://python.langchain.com/docs/guides/local_llms#quickstart
* First time you run this it will be slow as the model needs to be downloaded (basic model is ~4GB)
* Models are stored under ~/.ollama/models/blobs/
* Ollama runs a local API : http://localhost:11434/
* Stop ollama - top right of mac toolbar near the clock: https://github.com/jmorganca/ollama/issues/690#issuecomment-1745473655
* Re-start ollama - `ollama serve llama2` or run app again (if you run from command line you can see requests & timing)


Once the setup steps above have been run, you should see a server running on  http://localhost:11434/ 
Next setup a python venv:

* create new venv: `python3 -m venv env`      
* enable venv: `source env/bin/activate`
* install requirements: `pip install -r requirements.txt`
* if you install anymore packages run: `pip freeze > requirements.txt`


Run the UI: `streamlit run src/ui.py`
**or**
Run the command line example: `python src/engine.py`
