from openai import OpenAI


api = OpenAI()

next = api.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages = [
      {
        "role": "system",
        "content": "You are a helpful assistant. Return in json format."
      },
      {
        "role": "user",
        "content": "Give me a list of presidents of the United States."
      }
    ],
    max_tokens=50,
    temperature=0,
    response_format={ "type": "json_object" },
)

print(next.choices[0].message.content)