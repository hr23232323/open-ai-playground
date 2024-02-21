from util.client import client
from util.response import parse_chat_response

def create_basic_completion():
    completion = client.chat.completions.create(
        messages = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ],
        model = "gpt-3.5-turbo",
    )

    message, tokens_used = parse_chat_response(completion)
    
    return message, tokens_used
