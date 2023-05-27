name = "My name"
age = 23
city = "Moscow"
favorite_food = "fruits"

def food(meal):
    if meal == favorite_food:
        return meal
    else:
        return "Not found"
    
meal_list = food(favorite_food)
print(meal_list)