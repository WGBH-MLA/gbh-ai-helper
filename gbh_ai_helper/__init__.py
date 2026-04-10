# gbh_ai_helper/__init__.py

from importlib import metadata
import os
from dotenv import load_dotenv

try:
    __version__ = metadata.version("gbh-ai-helper")
except ModuleNotFoundError:
    __version__ = "local"

from .single_round import analyze_sample, one_completion, get_client, DEFAULT_DEPLOYMENT_ALIAS

# minimal package-level API
__all__ = [ analyze_sample, one_completion, get_client, DEFAULT_DEPLOYMENT_ALIAS ]

# load creds into the env as soon as package is imported
creds_path = os.path.expanduser("~/.gbh_ai")
if os.path.exists(creds_path):
    load_dotenv(creds_path, override=True)
else:
    raise RuntimeError(f"Required credentials file not found at `~/.gbh_ai`.")
