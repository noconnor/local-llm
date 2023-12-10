from langchain.llms import Ollama
import analysis_prompts as prompts
import os

if __name__ == "__main__":
    # Loads model into RAM
    # This is using Facebook's llama model (7B params - i.e. the smallest model available)
    # It takes about 4GB of RAM to run.
    # Larger models will perform better.
    llm = Ollama(model="llama2")

    # Loads an example API yaml file
    # You'd probably want to split this up into chunks before sending it to the model
    # as the model will have a limit on how much context it can handle
    dir_path = os.path.dirname(os.path.realpath(__file__))
    yaml = open(os.path.join(dir_path, 'example_api.yaml'), 'r').read()

    # Use the model generate a summary of the yaml
    summary = prompts.summarize_api(llm, yaml)
    # Use the summary to generate a set of test cases - you could probably go directly from yama to test cases
    # without the summary, but might be useful to see how to chain outputs.
    # There's probably a better way of doing this.
    test_cases = prompts.describe_test_cases(llm, summary)

    print("\n\n*** API overview ****")
    print(summary)
    print("\n\n*** Example test cases ****")
    print(test_cases)


