from openai import OpenAI


api = OpenAI()

completion = api.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
      {
        "role": "system",
        "content": "You are a helpful assistant. Print in Json format."
      },
      {
        "role": "user",
        "content": "Once upon a time"
      }
    ],
    max_tokens=15,
    temperature=0,
    logprobs=True,
    top_logprobs=2,
)

print(completion.choices[0].message.content)
if completion.choices[0].logprobs is not None:
    all_logprobs = completion.choices[0].logprobs.content
    for logprob in all_logprobs:
        print(logprob)