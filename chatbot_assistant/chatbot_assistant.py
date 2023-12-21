import os
from openai import OpenAI

openai = OpenAI()

def regular_discussion(prompt):
  """
params: prompt - a string
Returns a response from the API using Davinci.
If the user asks about a drug, the function will call get_malady_name().
  """
  prompt = [
      {"role": "system", "content": """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, very friendly and careful with Human's health topics
If Human writes the name of a drug the assistant will reply with "######".
Human: Hi
AI: Hello Human. How are you? I'll be glad to help. Give me the name of a drug and I'll tell you what it's used for.
Human: What is the use of following drug: 'Ebal 20mg Tablet 10'SEbal 10mg Tablet 10'S'?
AI: ######
Human: I'm fine. How are you?
AI: I am fine. Thank you for asking. I'll be glad to help. Give me the name of adrug and I'll tell you what it's used for.
Human: What is Chaos Engineering?
AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer questions about drugs. Give me the name of a drug and I'll tell you what it's used for.
Human: Where is Carthage?
AI: I'm sorry, I am not qualified to do that. I'm only programmed to answer questions about drugs. Give me the name of a drug and I'll tell you what it's used for.
Human: What is the use of following drug: 'Admenta 5mg Tablet 10'SAdmenta 10mg Tablet 10'S.?
AI: ######
Human: What is the use of following drug: 'Modapro 100mg Tablet 10'SModapro 200mg Tablet 10'S.?
AI: ######
"""}, {"role": "user", "content": """
{}
""".format(prompt)}]
  # Get the response from the API.
  response = openai.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=prompt,
  max_tokens=100,
  stop=["\n", " Human:", " AI:"],
  )
  if response.choices[0].message.content.strip() == "######":
    get_malady_name(prompt[1]['content'].strip())
  else:
    final_response = response.choices[0].message.content.strip() + "\n"
    print("AI: {}".format(final_response))


def get_malady_name(drug_name):
  """
params: drug_name - a string
Returns a malady name that corresponds to a drug name from the fine-tuned model.
The function will call get_malady_description() to get a description of the malady.
"""
  # Configure the model ID. Change this to your model ID.
  model = "ft:gpt-3.5-turbo-1106:personal::8Y67cEkf"
  class_map = {
    0: "Acne",
    1: "Adhd",
    2: "Allergies",
    3: "Alzheimer",
    4: "Amoebiasis",
    5: "Anemia",
    6: "Angina",
    7: "Anxiety",
  }
  # Returns a drug class for each drug
  prompt = [
      {"role": "system", "content": "You are a helpful medical prescription chatbot."},
      {"role": "user", "content": "{}\n".format(drug_name)}]
  response = openai.chat.completions.create(
  model=model,
  messages=prompt,
  temperature=0,
  max_tokens=100,
  )
  response = response.choices[0].message.content
  try:
    malady = class_map[int(response)]
    print("AI: This drug used for {}.".format(malady))
    print(get_malady_description(malady))
  except:
    print("AI: I don't know what '" + drug_name + "' is used for.")


def get_malady_description(malady):
  """
params: malady - a string
Get a description of a malady from the API using Davinci.
"""
  prompt = [
      {"role": "system", "content": "You are a helpful medical prescription chatbot."},
      {"role": "user", "content": """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
The assistant does not provide medical advice. It only defines a malady, a disease, or a condition.
If the assistant does not know the answer to a question, it will ask to rephrase it.
Q: What is {}?
A:
""".format(malady)}]
  # Get the response from the API.
  response = openai.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=prompt,
  max_tokens=100,
  stop=["\n", " Q:", " A:"],
  )
  return response.choices[0].message.content.strip()


if __name__ == "__main__":
  while True:
    regular_discussion(input("Human:"))