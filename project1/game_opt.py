"""Game predict number optimized"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing a number

    Args:
        number (int, optional): mystery number. Defaults to 1.

    Returns:
        int: number of attempts
    """

    count = 0
    minimum_boundary = 0 # заносим в перемнные границы для поиска
    maximum_boundary = 101

    while True:
        count += 1
        predict_number = np.random.randint(minimum_boundary, maximum_boundary) # предполагаемое число

        if predict_number < number:
            minimum_boundary = predict_number # укорачиваем диопазон поиска по нижней границе

        elif predict_number > number:
            maximum_boundary = predict_number # укорачиваем диопазон поиска по верхней границе

        elif count > 50: break

        else: break # выход из цикла, если угадали

    return(count)


def score_game(random_predict) -> int:
    """is the number of times our algorithm guesses the number. 1000 passes

    Args:
        random_predict (function): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'the algorithm guesses the number on average in {score} tries')
    return(score)


score_game(random_predict)
