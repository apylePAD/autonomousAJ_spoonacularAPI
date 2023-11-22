import os
from dotenv import load_dotenv

load_dotenv()

class Get_Spoonacular_Client:
    def __init__(self):
        self.api_key = os.getenv('SPOONACULAR_API_KEY')

    def get_spoonacular_client(self):
        api_key = self.api_key
        return api_key

spoonacular_client = Get_Spoonacular_Client()