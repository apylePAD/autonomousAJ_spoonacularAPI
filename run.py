# autonomousAJ_spoonacularAPI/run.py
import inquirer
from autonomousAJ_spoonacularAPI.data.random_recipe_data import Random_Recipe_Data


def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Random Recipe', 'Recipe By Ingredients', 'Recipe By Nutrients', 'Search Recipe', 'Similar Recipe', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_randomRecipe_input():
    random_recipe_processor = Random_Recipe_Data()
    random_recipe_processor.get_and_process_random_recipe_data()

def get_recipeByIngredients_input():
    pass

def get_recipeByNutrients_input():
    pass

def get_searchRecipe_input():
    pass

def get_similarRecipe_input():
    pass

    
def run():
    while True:
        choice = main_menu()
        if choice == 'Random Recipe':
            get_randomRecipe_input()
        elif choice == 'Recipe By Ingredients':
            get_recipeByIngredients_input()
        elif choice == 'Recipe By Nutrients':
            get_recipeByNutrients_input()
        elif choice == 'Search Recipe':
            get_searchRecipe_input()
        elif choice == 'Similar Recipe':
            get_similarRecipe_input()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()