"""Game predict number"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100: "))

    if predict_number > number:
        print("The number must be smaller than")

    elif predict_number < number:
        print("The number should be higher than")

    else:
        print(f"Great! That number {predict_number} you guessed in {count} tries")
        break # конец игры, выход из цикла
