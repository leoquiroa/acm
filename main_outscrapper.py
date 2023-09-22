from outscraper import ApiClient
from utils import Utils

keys = Utils.read_keys()
client = ApiClient(api_key=keys["OUTSCRAPER_API_KEY"])

curl 
-X 
GET 
"https://api.app.outscraper.com/yelp/reviews?query=eggcellent-waffles-san-francisco&limit=3&async=false" 
-H  
"X-API-KEY: YOUR-API-KEY"