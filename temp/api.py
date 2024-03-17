import json
import requests
import os 

api_key = os.environ.get('API_KEY')


url = f"https://api.openweathermap.org/data/2.5/weather?q=london&appid={api_key}"


r = requests.get(url)

data = json.loads(r.text)

print(data)

# print(data['weather'] [0] ['description'])
# city = 'new york'
# G_api_key = 'AIzaSyDTaGNseARJbi3EOOXoF5noneGuythKpiQ'
# page = 1
# search_engine_ID = '7594d42e2b52844b7'
# query = city + "1920x1080"
# start = (page - 1) *10 +1
# search_type = 'image'
# url =f"https://customsearch.googleapis.com/customsearch/v1?key={G_api_key}&cx={search_engine_ID}&q={query}&start={start}&searchType={search_type}&imgSize=xlarge"
# data = requests.get(url).json()
# search_items = data.get("items")
# image_url = search_items[1] ['link']
# image_url =str(image_url)

# print (image_url)