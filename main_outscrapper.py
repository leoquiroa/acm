from outscraper import ApiClient
from utils import Utils

keys = Utils.read_json("keys.json")
client = ApiClient(api_key=keys["OUTSCRAPER_API_KEY"])
restaurants = Utils.read_json(f"Configs\\restaurants.json")
RESTAURANT_NAME = restaurants["NAME"]
URL = "https://www.yelp.com/biz/"

response = client.yelp_reviews(
    query=f"{URL}{RESTAURANT_NAME}",
    limit=restaurants["LIMIT"],
    fields=["review_id","review_rating","review_text","date"],
    sort="date_desc"
)
print(response)
file_name = f"Response\\{RESTAURANT_NAME}.{Utils.get_today_date()}-scrapper"
Utils.save_response_as_json(file_name,response[0])
print('--')
