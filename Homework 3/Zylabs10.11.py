# Jarandon Adams - 1812590
# Zylabs 10.11

class FoodItem:

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def calc_calories(self, servings_amt):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings_amt
        return calories

    def food_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":

    food_item1 = FoodItem()

    food_name = input()
    fat_content = float(input())
    carb_content = float(input())
    protein_content = float(input())

    food_item2 = FoodItem(food_name, fat_content, carb_content, protein_content)

    num_servings = float(input())

    food_item1.food_info()

print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item1.calc_calories(num_servings)))
print()
food_item2.food_info()
print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item2.calc_calories(num_servings)))
