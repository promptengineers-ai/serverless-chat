"""Configuration files for the project."""
import os

# Path to the vector store
APP_VERSION = os.getenv("APP_VERSION", '')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", '')