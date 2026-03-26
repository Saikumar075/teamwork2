import random

dice_roll=random.randint(1,6)
print(dice_roll)

luck =(1,2,3,43,65,7,0,6,80,100)
new=random.choices(luck,k=1)
print(new)
print("Both addition",new[0]+dice_roll,"multiplicate",new[0]*dice_roll)