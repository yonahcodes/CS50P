def main():
    fruit = input("Item: ").strip().lower()
    result = calories(fruit)

    if result != None:
        print(f"Calories: {calories(fruit)}")

def calories(fruit):
    # Create a dictionary with key-value pairs
    fruit_dict = {
        "apple": "130", "avocado": "50", "banana": "110",
        "cantaloupe": "50", "grapefruit": "60", "grapes": "90",
        "honeydew melon": "50", "kiwifruit": "90", "lemon": "15",
        "lime": "20", "nectarine": "60", "orange": "80",
        "peach": "60", "pear": "100", "pineapple": "50",
        "plums": "70", "strawberries": "50", "sweet cherries": "100",
        "tangerine": "50", "watermelon": "80",
    }

    # Check if fruit input is in the dictionary
    # If it is return associated value
    if fruit in fruit_dict:
        return fruit_dict[fruit]


main()
