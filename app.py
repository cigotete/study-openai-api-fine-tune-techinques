from openai import OpenAI


api = OpenAI()
models = api.models.list()

for model in models:
    print(model.id)