import os
from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="ft:davinci-002:personal::8XcRkM3U",
  #messages=[
    #{"role": "system", "content": "You are a helpful assistant."},
    #{"role": "user", "content": "Hello! When is the library open on weekends?"}
  #]
  prompt="When do I have to start the heater?",
)
print(response.choices[0].text)