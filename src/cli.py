from langchain.llms import Ollama
import analysis_prompts as prompts
import os

if __name__ == "__main__":
    # Loads model into RAM
    # This is using Facebook's llama model (7B params - i.e. the smallest model available)
    # It takes about 4GB of RAM to run.
    # Larger models will perform better.
    # When using this model, calls will be made to localhost:11434/ but will not be sent to any remote endpoints
    # https://python.langchain.com/docs/integrations/llms/ollama
    # Might also be worth looking at https://python.langchain.com/docs/integrations/chat/ollama
    llm = Ollama(model="mistral")

    # Loads an example API yaml file
    # You'd probably want to split this up into chunks before sending it to the model
    # as the model will have a limit on how much context it can handle
    dir_path = os.path.dirname(os.path.realpath(__file__))
    yaml = open(os.path.join(dir_path, 'example_api.yaml'), 'r').read()

    message = prompts.important_message(llm)
    # Use the model generate a summary of the yaml...can be slow
    summary = prompts.summarize_api(llm, yaml)
    # Use the summary to generate a set of test cases
    # You could pass the yaml in here to see if you get better results
    test_cases = prompts.describe_test_cases(llm, summary)
    # use the yaml again here
    example_curl = prompts.provide_example_curl_data(llm, yaml)
    # Use yaml to generate example kotlin batch upload request
    example_kotlin = prompts.batch_create_example(llm, yaml)

    print("\n\n*** Important message ****")
    print(message)
    print("\n\n*** API overview ****")
    print(summary)
    print("\n\n*** Example test cases ****")
    print(test_cases)
    print("\n\n*** Example curl ****")
    print(example_curl)
    print("\n\n*** Example kotlin ****")
    print(example_kotlin)

