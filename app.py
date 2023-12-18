from openai import OpenAI


api = OpenAI()

completion = api.chat.completions.create(
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
    max_tokens=15,
    temperature=0.7,
    n=2
)

response = completion.choices
for i in response:
    print(i.message.content)