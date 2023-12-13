# ollama + langchain

Example code to use langchain library to run queries against an ollama models 


## Setup:

* See install instructions for ollama app: https://ollama.ai/download
  * Reference: https://python.langchain.com/docs/guides/local_llms#quickstart
* From commandline run  
  * `ollama pull mistral`
  * `ollama pull llama2`
* First time you run this it will be slow as the models needs to be downloaded (each model is ~4GB)
* Models are stored under ~/.ollama/models/blobs/
* Ollama runs a local API : you can browse to `http://localhost:11434/`
* To stop ollama - see top right of mac toolbar near the clock: https://github.com/jmorganca/ollama/issues/690#issuecomment-1745473655
* Re-start ollama - `ollama serve mistral` or `ollama serve llama2`


Once the setup steps above have been run, you should see a server running on  http://localhost:11434/ 


Next setup a python venv:

* create new venv: `python3 -m venv env`      
* enable venv: `source env/bin/activate`
* install requirements: `pip install -r requirements.txt`
* if you install anymore packages run: `pip freeze > requirements.txt`


Run the UI: `streamlit run src/ui.py`
**or**
Run the command line example: `python src/cli.py`
