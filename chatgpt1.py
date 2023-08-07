import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="text-curie-001",  # Correct engine name for GPT-3.5 Turbo
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message['content'])  # Accessing the content of the message
