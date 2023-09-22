from utils import Utils
import openai

keys = Utils.read_json("keys.json")
openai.api_key = keys["OPENAI_API_KEY"]
restaurants = Utils.read_json("Configs\\restaurants.json")
reviews = Utils.read_json(f"Response\\{restaurants['NAME']}.{Utils.get_today_date()}-scrapper.json")
reviews = [x['review_text'] for x in reviews]


prompt_to_chatgpt = [
  {
    "role": "system",
    "content": Utils.read_prompt_file()
  }
]
for review in reviews:
  prompt_to_chatgpt.append(
    {      
      "role": "user",
      "content": review
    }
  )

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=prompt_to_chatgpt,
  temperature=0.02,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
file_name = f"Response\\{restaurants['NAME']}.{Utils.get_today_date()}-chatgpt-full"
Utils.save_response_as_json(file_name,response)
print('--')
file_name = f"Response\\{restaurants['NAME']}.{Utils.get_today_date()}-chatgpt-compact"
Utils.save_response_as_json(file_name,response["choices"][0]["message"]["content"])
print(response["choices"][0]["message"]["content"])
print('--')
