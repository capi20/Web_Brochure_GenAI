import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv(override=True)

# Retrieve API key from environment
API_KEY = os.getenv('OPENAI_API_KEY')

# Validate API key
if API_KEY and API_KEY.startswith('sk-proj-') and len(API_KEY) > 10:
    print('API key looks good so far')
else:
    print('API key invalid')

# OpenAI model configuration
MODEL = 'gpt-4o-mini'
openai = OpenAI()
