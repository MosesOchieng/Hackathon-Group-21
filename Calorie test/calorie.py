def main():

    # Ask for the number of fat grams.
    fat_grams = int(input('Enter the number of fat grams consumed: '))
    fat_calories(fat_grams)

    # Ask for the number of carb grams.
    carb_grams = int(input('Enter the number of carbohydrate grams consumed: '))
    carb_calories(carb_grams)

def fat_calories(fat_grams):
    # Calculate the calories from fat.
    # calories_from_fat = fat_grams*9
    calories_from_fat = fat_grams * 9
    print ('The calories from fat are', calories_from_fat)

def carb_calories(carb_grams):
    # Calculate the calories from carbs.
    # calories_from_carbs = carb_grams * 4
    calories_from_carbs = carb_grams * 4
    print( 'The calories from carbohydrates are', calories_from_carbs)

# Call the main function.
main()
