from openai import OpenAI


api = OpenAI()

next = api.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Once upon a time"
      }
    ],
    max_tokens=7,
    temperature=0,
)

print(next)