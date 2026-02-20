# GBH AI Helper

This is a Python package to facilitate use of GBH-provided AI resources, like OpenAI models provided through Microsoft Azure.

## Setup

### Installation

Clone the repository.  Change to the repository directory and do a `pip install .` to install the package and its dependencies.

(For developers, do `pip install -e .` to install in editable mode.)

### Credentials

For the package to be useful, you need info and secrets stored in a file in your home directory.  Call your file `~/.gbh_ai`.  It defines environment variables `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `OPENAI_API_VERSION`, `DEPLOY_GPT41MINI`.

An example template can be found in the `.gbh_ai.example` file in this repo.

### Verifying setup

To verify the setup works, try running `gbh_ai_helper_test` from the command line.

## Usage

This package is intended to be used by other Python modules.

The main function to use is `analyze_sample` which supports using an LLM to perform some kind of analysis on a sample of user-provided text.

