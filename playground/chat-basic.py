from chat.chat_basic import create_basic_completion

message, tokens_used = create_basic_completion()

print(message)
print(f"Tokens Used: {tokens_used}")