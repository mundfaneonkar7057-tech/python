def calculate_calories(carbs, fats, proteins):
    calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return calories


carbs = float(input("Enter grams of carbs: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

total = calculate_calories(carbs, fats, proteins)

print("Total caloric intake:", total, "calories")