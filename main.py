import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The cat says "
)

print(response)
