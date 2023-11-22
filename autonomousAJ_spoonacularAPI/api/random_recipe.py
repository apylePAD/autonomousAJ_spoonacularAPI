# autonomousAJ_spoonacularAPI/api/albums.py
import requests
from .base import Spoonacular_API_Base

class Random_Recipe(Spoonacular_API_Base):
    def search_random_recipes(self):
        api_key = self.get_spoonacular_client()
        print(api_key)

        # Endpoint for getting a random recipe
        url = 'https://api.spoonacular.com/recipes/random'

        # Parameters for the API call
        params = {
            'apiKey': api_key,
            'number': 1  # Number of recipes to return
        }

        # Making the GET request
        response = requests.get(url, params=params)

        # Checking if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)  # or process the data as you need
        else:
            print("Failed to retrieve data:", response.status_code)

        return data
