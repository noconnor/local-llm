# llama + langchain

Example code to use langchain library to run queries against an LLama model 


## Setup:

* See install instructions for ollama: https://python.langchain.com/docs/guides/local_llms
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

Run the script: `python src/engine.py`


### Example CLI output:

```
*** API overview ****
The API described in the YAML file has the following features:

* The `info` section provides metadata about the API, including its title, description, version, and server locations.
* The `servers` section specifies two servers for the API: `http://api.example.com/v1` (the main production server) and `http://staging-api.example.com` (an internal staging server for testing).
* The `paths` section defines the available endpoints for the API. For each endpoint, it provides a summary of what the endpoint does, as well as a description of the response.
* The `/users` endpoint retrieves a list of users and returns them in a JSON array.

Step-by-step analysis of inputs and outputs:

1. `GET /users`:
   Inputs: None
   Outputs: A JSON array of user names (type: string)
2. Response codes:
   * `200`: Successful response with a JSON array of user names
3. `application/json` content type:
   * Schema: An array of strings representing the list of users
4. Other content types:
   * Type: array
   * Items: String (representing each user name in the array)


*** Example test cases ****

Of course! Based on the provided API summary, here are five test cases that should be covered when writing automated tests for this API:

1. Test case: Verify successful response with a JSON array of user names
   * Inputs: None
   * Outputs: A JSON array of user names (type: string)
   * Expected response code: 200 (Successful response)
   * Expected content type: application/json
   * Schema: An array of strings representing the list of users
2. Test case: Verify response with a valid user ID
   * Inputs: Valid user ID (type: integer)
   * Outputs: A JSON object containing the user details (type: object)
   * Expected response code: 200 (Successful response)
   * Expected content type: application/json
   * Schema: An object with fields for user ID, name, email, and other relevant details
3. Test case: Verify response with an invalid user ID
   * Inputs: Invalid user ID (type: integer)
   * Outputs: A JSON error message indicating the user ID is invalid (type: string)
   * Expected response code: 404 (User not found) or 500 (Internal server error)
   * Expected content type: application/json
   * Schema: A string representing the error message
4. Test case: Verify response with a valid user name
   * Inputs: Valid user name (type: string)
   * Outputs: A JSON object containing the user details (type: object)
   * Expected response code: 200 (Successful response)
   * Expected content type: application/json
   * Schema: An object with fields for user ID, name, email, and other relevant details
5. Test case: Verify response with an invalid user name
   * Inputs: Invalid user name (type: string)
   * Outputs: A JSON error message indicating the user name is invalid (type: string)
   * Expected response code: 404 (User not found) or 500 (Internal server error)
   * Expected content type: application/json
   * Schema: A string representing the error message
```