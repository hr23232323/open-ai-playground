from openai import OpenAI
from decouple import config

api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# TODO - anything more complex