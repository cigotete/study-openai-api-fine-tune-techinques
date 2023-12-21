import os
from openai import OpenAI
client = OpenAI()

job = client.fine_tuning.jobs.create(
  training_file="file-XYZ",
  validation_file="file-ABC",
  model="davinci-002"
)

print("Fine-tuning job started:", job.id)