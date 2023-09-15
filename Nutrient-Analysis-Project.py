# Program: Nutrition Assistant
# Author: TUAN LUC LU
# Date: 10 May 2020
# The source of the data: USDA FoodData Central

import requests


class Food:
    def __init__(self, name):
        self.name = name
        self.calories = 0
        self.fat = 0
        self.sodium = 0
        self.potassium = 0
        self.carb = 0
        self.fiber = 0
        self.protein = 0
        self.sugars = 0
        self.vitamin_a = 0
        self.vitamin_c = 0
        self.calcium = 0
        self.iron = 0

    def fetch_data_from_api(self):
        api_url = f'https://api.nal.usda.gov/fdc/v1/foods/list?api_key=fruit'
        response = requests.get(api_url)
        data = response.json()

        self.calories = data.get('calories', 0)
        self.fat = data.get('fat', 0)
        self.sodium = data.get('sodium', 0)
        self.potassium = data.get('potassium', 0)
        self.carb = data.get('carb', 0)
        self.fiber = data.get('fiber', 0)
        self.protein = data.get('protein', 0)
        self.sugars = data.get('sugars', 0)
        self.vitamin_a = data.get('vitamin_a', 0)
        self.vitamin_c = data.get('vitamin_c', 0)
        self.calcium = data.get('calcium', 0)
        self.iron = data.get('iron', 0)


def main():
    food_items = [
        'apple', 'avocado', 'banana', 'cantaloupe', 'grapefruit',
        'grapes', 'honeydew', 'kiwi', 'lemon', 'lime',
        'nectarine', 'orange', 'peach', 'pear', 'pineapple',
        'plums', 'strawberries', 'cherries', 'tangerine', 'watermelon'
    ]

    foods = {}  # Dictionary to store Food objects

    print("Welcome to the Nutritional Checking program!")

    # Fetch data for each food item and create Food objects
    for item in food_items:
        food = Food(item)
        food.fetch_data_from_api()
        foods[item] = food


if __name__ == "__main__":
    main()
