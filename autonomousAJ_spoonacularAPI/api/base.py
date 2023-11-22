# autonomousAJ_spoonacularAPI/api/base.py
from autonomousAJ_spoonacularAPI.auth import spoonacular_client
import requests

class Spoonacular_API_Base:
    def get_spoonacular_client(self):
        return spoonacular_client.get_spoonacular_client()

    def handle_api_call(self, api_function, *args, **kwargs):
        try:
            response = api_function(*args, **kwargs)
            response.raise_for_status()  # Raises an HTTPError for bad requests
            return response

        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")

        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")

        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")

        except requests.exceptions.RequestException as err:
            print(f"Other Error: {err}")

        return None
