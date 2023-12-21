import os
import pprint
from openai import OpenAI

client = OpenAI()

pp = pprint.PrettyPrinter(indent=2)

drugs = [
  "What is 'A CN Gel(Topical) 20gmA CN Soap 75gm' used for?", # Class 0
  "What is 'Addnok Tablet 20'S' used for?", # Class 1
  "What is 'ABICET M Tablet 10's' used for?", # Class 2
]

for drug_name in drugs:
  prompt = "Drug: {}\nMalady:".format(drug_name)
  response = client.completions.create(
    model="ft:davinci-002:personal::qwerty",
    #messages=[
      #{"role": "system", "content": "You are a helpful assistant."},
      #{"role": "user", "content": "Hello! When is the library open on weekends?"}
    #]
    prompt=prompt,
    temperature=1,
    max_tokens=1,
  )
  result = vars(response.choices[0])
  pp.pprint(result)
  print('#'*50)