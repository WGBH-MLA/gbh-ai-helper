
# imports from standard library
import os

# imports from Python venv
from openai import AzureOpenAI
from dotenv import dotenv_values

# imports from within this package
from . import __version__

DEFAULT_SYSTEM_PROMPT = """
You are sharp and analytical. 
You provide a short, precise answer to each request. 
Do not restate the question or use full sentences. 
Do not add any phrases or punctuation unless they are part of the answer.
Your response must be the answer ONLY.  
If you cannot definitively determine a single answer, then you must respond by saying 'NO ANSWER'
"""

def get_client():
    """
    Client is initialized using the values of environment varaibles.
    """
    client = AzureOpenAI()
    return client

_default_client = None

def analyze_sample( instruction:str,
                    sample:str,
                    system_prompt:str=DEFAULT_SYSTEM_PROMPT,
                    max_tokens:int=150,
                    client=None,
                    deployment_key="DEPLOY_GPT41MINI" ) -> str:
    """Given an instruction and some text for analysis, it performs the analysis 
    and returns the result."""

    # lazy client initialization
    global _default_client
    if client is None:
        if _default_client is None:
            _default_client = get_client()
        client = _default_client

    full_instruction  = "TASK: I have some text. " + instruction
    wrapped_sample = 'TEXT: """\n' + sample + '\n"""'
    full_user_prompt = full_instruction + "\n\n" + wrapped_sample

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": full_user_prompt} ]

    deployment_name = os.getenv(deployment_key)

    # Use the chat.completions API
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        max_completion_tokens=max_tokens,
        temperature=0.5 )
    response_content = response.choices[0].message.content

    return response_content


def run_test():
    client = get_client()

    instruction = "Give me a comma-separated list of the proper names."
    sample = "I was talking to Owen the other day, and he told me he living in Boston."
    system_prompt = DEFAULT_SYSTEM_PROMPT

    response = analyze_sample(instruction, sample, system_prompt)

    print("TEST INSTRUCTION: " + instruction)
    print("TEST SAMPLE:      " + sample)
    print("TEST OUTPUT:      " + response)


def main():
    """
    For now, the main method just runs the test 
    """
    print(f"GBH AI Helper (version {__version__})\n")

    run_test()


if __name__ == "__main__":
    main()
