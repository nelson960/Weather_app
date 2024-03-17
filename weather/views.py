from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
import re
import os 


api_key = os.environ.get('API_KEY')	
G_api_key = os.environ.get('G_API_KEY')
# paste the api keys as plain text if not working 



def index(request):
	
	if 'city' in request.POST:
		city = request.POST.get('city', '')
		city = re.sub(r"[^\w\s]", "", city)
	else:
		city = 'London' 

	
	weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

	PARAMS = {'units':'metric'}
	
	
	page = 1
	search_engine_ID = '7594d42e2b52844b7'
	query = city + "1920x1080"
	start = (page - 1) *10 +1
	search_type = 'image'
	url =f"https://customsearch.googleapis.com/customsearch/v1?key={G_api_key}&cx={search_engine_ID}&q={query}&start={start}&searchType={search_type}&imgSize=xlarge"
	data = requests.get(url).json()
	search_items = data.get("items")
	image_url = search_items[1]['link']

	try:
		data = requests.get(weather_url, PARAMS).json()
		description = data['weather'] [0] ['description']
		icon = data['weather'] [0] ['icon']
		temp = data['main'] ['temp']
		day = datetime.date.today()
		return render(request, 'weather/index.html', {'description':description, 'icon':icon, 'temp':temp, 'city': city, 'day':day, 'image_url':image_url, 'exception_occurred':False})
   
	except KeyError:
		exception_occurred = True
		messages.error(request, 'Entered data is not avilable to API ')
		day = datetime.date.today()
		return render(request, 'weather/index.html', {'description':'Entered location is not avaliable','icon':'01d', 'city': 'london', 'day':day, 'exception_occurred':exception_occurred})


