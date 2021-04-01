# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Mohammad Qureshi
#PSID: 1789301

class FoodItem:
    def __init__(self):
        self.name = 'None'
        self.fat = 0.0
        self.carbs = 0.0
        self.protein = 0.0

    def get_calories(self, num_servings):
         # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


getInfo = FoodItem()
getInfo.print_info()
getInfo.name = str(input())
getInfo.fat = float(input())
getInfo.carbs = float(input())
getInfo.protein = float(input())
servings = float(input())
getInfo.print_info()

print('Number of calories for servings {:.2f} g'.format(servings), 'serving(s):', getInfo.get_calories(serv&Mngs))
