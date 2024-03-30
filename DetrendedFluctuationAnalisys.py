import numpy as np
import matplotlib.pyplot as plt
from MFDFA import MFDFA
# import pandas as pd


# Считываем данные из файла
dates = np.loadtxt('dates/isi.txt')
n=dates[0]
data = dates[2:]
lag = np.unique(np.logspace(0.5, 3, 100).astype(int))

# Шум
# np.random.seed(0)
# signal_length = 1000
# data = np.random.randn(signal_length)

# Define scale range
lag = np.arange(10, 200, 10)


# Вычисляем зависимость lg(F_DFA) от lg(n)
lag, dfa = MFDFA(data, lag, q=2, order = 2)

# Рассчитываем показатель скейлинга α
alpha = np.polyfit(np.log10(lag), np.log10(dfa), 1)[0]

# Выводим результаты
print(f'Показатель скейлинга α: {alpha}')

# Строим график
plt.plot(np.log10(lag), np.log10(dfa), marker='o')
plt.xlabel('lg(n)')
plt.ylabel('lg(DFA)')
plt.title('Dependence of lg(DFA) on lg(n)')
plt.show()
