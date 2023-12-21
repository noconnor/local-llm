# ollama + langchain

Example code to use [langchain](https://python.langchain.com/docs/get_started/introduction) library to run queries against an [ollama](https://ollama.ai/) models.

See [Ollama examples](https://github.com/jmorganca/ollama/tree/main/examples) for reference code.


## Setup Local models:

* See install instructions for ollama app: https://ollama.ai/download
  * Reference: https://python.langchain.com/docs/guides/local_llms#quickstart
* From commandline run:
  * `ollama pull mistral` (4GB on disk, ~8GB in RAM)
  * `ollama pull llama2`  (4GB on disk, ~8GB in RAM)
* First time you run this it will be slow as the models needs to be downloaded.
* Models are stored under ~/.ollama/models/blobs/
* Ollama runs a local API : you can browse to `http://localhost:11434/`
* To stop ollama - see top right of mac toolbar near the clock: https://github.com/jmorganca/ollama/issues/690#issuecomment-1745473655
* Re-start ollama - `ollama serve mistral` or `ollama serve llama2`

Once the setup steps above have been run, you should see a server running on  http://localhost:11434/ 


## Setup a python venv:

* create new venv: `python3 -m venv env`      
* enable venv: `source env/bin/activate`
* install requirements: `pip install -r requirements.txt`
* if you install anymore packages run: `pip freeze > requirements.txt`


## Run Examples:

* Instruction processing: 
  * Run the UI, from the commandline run: `streamlit run src/instruct/ui.py`
  * Or Run the same prompts via the command line: `python src/instruct/cli.py`
* Document Summaries:
  * Run the UI, from the commandline run: `streamlit run src/summarise/ui.py`
* Document Comparison:
  * Run the UI, from the commandline run: `streamlit run src/comparison/ui.py`
