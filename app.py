import os
from openai import OpenAI


api = OpenAI()

response = api.embeddings.create(
  model="text-embedding-ada-002",
  input="I am a programmer",
  )

print(response)