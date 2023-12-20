import os
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("data_prepared.jsonl", "rb"),
  purpose="fine-tune"
)