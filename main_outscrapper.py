from outscraper import ApiClient
from utils import Utils

keys = Utils.read_keys()
client = ApiClient(api_key=keys["OUTSCRAPER_API_KEY"])
RESTAURANT_NAME = "https://www.yelp.com/biz/aba-austin-austin"
response = client.yelp_reviews(
    query=RESTAURANT_NAME,
    limit=25,
    fields=["review_id","review_rating","review_text","date"],
    sort="date_desc"
)
print(response)
file_name = RESTAURANT_NAME.split("/")[-1]
Utils.save_response(f"Response/{file_name}",response[0])
print('--')
