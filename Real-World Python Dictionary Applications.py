#Task 1: 
# Restaurant Menu Update 
# You are given an initial structure of a restaurant menu stored in a nested dictionary.
#  Your task is to update this menu based on given instructions


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Pepsi" : 2.50, "Sprite" : 2.00}
restaurant_menu["Main Course"]["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)