from openai import OpenAI
from openai.types.chat import ChatCompletion
from decouple import config

api_key = config("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def parse_chat_response(completion: ChatCompletion):
    message = completion.choices[0].message.content
    tokens_used = completion.usage.total_tokens
    
    return message, tokens_used

completion = client.chat.completions.create(
    messages = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ],
    model = "gpt-3.5-turbo",
)

message, tokens_used = parse_chat_response(completion)

print(message)
print(f"Tokens Used: {tokens_used}")
