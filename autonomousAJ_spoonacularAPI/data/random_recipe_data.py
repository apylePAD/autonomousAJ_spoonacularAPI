# autonomousAJ_spoonacularAPI/data/random_recipe_data.py
from datetime import datetime
import pandas as pd
from autonomousAJ_spoonacularAPI.api.random_recipe import Random_Recipe
from autonomousAJ_spoonacularAPI.config import global_config

class Random_Recipe_Data:
    def __init__(self):
        self.spoonacular_random_recipe = Random_Recipe()

    def get_and_process_random_recipe_data(self):
        random_recipe_data = self.spoonacular_random_recipe.search_random_recipes()
        
        df_random_recipe = pd.json_normalize(random_recipe_data['recipes']['items'])
        self.save_random_recipe_data(df_random_recipe)

    def save_random_recipe_data(self, df_random_recipe):
        now = datetime.now()
        df_random_recipe.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/random_recipes/random_recipe_{now}.csv", index=False)
        print(df_random_recipe)

