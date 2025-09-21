import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there!, Myself Shailesh Thorat"

tokens = enc.encode(text)

print("Tokens",tokens)

# Tokens [25216, 1354, 27942, 197617, 1955, 663, 8382, 49813, 266]

decoded = enc.decode([25216, 1354, 27942, 197617, 1955, 663, 8382, 49813, 266])
print("decoded",decoded)