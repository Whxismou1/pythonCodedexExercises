import random

num = random.randint(0, 1)   # RNGesus will give us a random number that is either 0 or 1

if num > 0.5:
  print(num)
  print('Heads')
else:
  print(num)
  print('Tails')