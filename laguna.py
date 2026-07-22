import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("POOLSIDE_API_KEY"),
  base_url="https://inference.poolside.ai/v1"
)

response = client.chat.completions.create(
  model="poolside/laguna-s-2.1",
  messages=[
    {
      "role": "user",
      "content": "What are channels in Go?"
    }
  ],
  stream=True
)

for chunk in response:
  if chunk.choices and chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="", flush=True)