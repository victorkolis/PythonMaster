# step2_reproduce_the_bug.py

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Reproduce the Bug - This is the error 
# from random import randint
# dice_imgs = 6
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Solution
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, len(dice_imgs) - 1)
print(dice_imgs[dice_num])
