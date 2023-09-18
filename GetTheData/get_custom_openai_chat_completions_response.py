import openai
import os
from dotenv import load_dotenv
from nova_prompt import return_nova_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_custom_openai_chat_completions_response(config=[{"role": "system", "content": "You are a helpful assistant. Please respond to the following conversation."}]):
  messages = []

  if config:
    if type(config) is not str:
      # print("Using config: " + str(config) + "\n")
      for item in config:
        if item["role"] in ["system", "user", "assistant"]:
          messages.append(item)
        else:
          print("Error: Invalid role")
    else:
      messages.append({"role": "system", "content": config})
      print(f"Using config: {config}" + " as system message\n")
  else:
    print("Error: No config provided")
    print("Using default config")
    messages.append({"role": "system", "content": "You are a helpful assistant."})

  return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

if __name__ == "__main__":
  print("Would you like to use a custom config? (y/n)")
  if input() == "y":
    print("Please enter your config:")
    user_input = input()
    print("Getting response from OpenAI...")
    response = get_custom_openai_chat_completions_response(user_input)
  else:
    print("Getting response from OpenAI...")
    response = get_custom_openai_chat_completions_response()
  response_text = response.choices[0].message.content
  print("Full response from OpenAI:\n\n\n")
  print(response)
  print('\n\n\n')
  print("Response Text:\n\n\n")
  print(response_text)
  print('\n\n\n')
  print('|~ End ~|')