from openai.types.chat import ChatCompletion

def parse_chat_response(completion: ChatCompletion):
    message = completion.choices[0].message.content
    tokens_used = completion.usage.total_tokens
    
    return message, tokens_used