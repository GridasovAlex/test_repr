"""Game predict number V2"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing a number

    Args:
        number (int, optional): mystery number. Defaults to 1.

    Returns:
        int: number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def score_game(random_predict) -> int:
    """is the number of times our algorithm guesses the number.
    1,000 passes

    Args:
        random_predict ([type]): guessing function

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

if __name__ == '__main__':
    # RUN
    score_game(random_predict)
