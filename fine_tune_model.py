import os
from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-M11YWj8Ln9fA3FBojHVpkFDN",
  model="davinci-002"
)