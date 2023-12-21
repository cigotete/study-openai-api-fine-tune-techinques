import os
from openai import OpenAI

client = OpenAI()

# Upload training file
with open("drug_malady_data_prepared_train.jsonl", "rb") as training_file:
    training_file_response = client.files.create(
        file=training_file,
        purpose="fine-tune"
    )

# Upload test file
with open("drug_malady_data_prepared_valid.jsonl", "rb") as test_file:
    test_file_response = client.files.create(
        file=test_file,
        purpose="fine-tune"
    )

print("Training file ID:", training_file_response.id)
print("Test file ID:", test_file_response.id)