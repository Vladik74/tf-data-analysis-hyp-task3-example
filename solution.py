import pandas as pd
import numpy as np

import statsmodels.stats.weightstats as w

chat_id = 496613075 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, res = w.ztest(x, value=500, alternative='larger')
    return res <= 0.1 # Ваш ответ, True или False
