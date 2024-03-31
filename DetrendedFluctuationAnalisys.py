import numpy as np
import matplotlib.pyplot as plt
from MFDFA import MFDFA
# import pandas as pd


# Считываем данные из файла
dates = np.loadtxt('dates/rr2.txt')
n=dates[0]
h = dates[1]
data = dates[2:]
lag = np.arange(1, n, h)

# Шум
# np.random.seed(0)
# n = 1000
# data = np.random.randn(n)
# lag = np.arange(1, n, 1)

# Вычисляем зависимость lg(F_DFA) от lg(n)
lag, dfa = MFDFA(data, lag, q=2, order = 2)

# Рассчитываем показатель скейлинга α
alpha = np.polyfit(np.log10(lag), np.log10(dfa), 1)[0]

# Выводим результаты
print(f'Показатель скейлинга α: {alpha}')

# Строим график
plt.subplot(2, 1, 1)
plt.plot(data)
plt.subplot(2, 1, 2)
plt.loglog(lag, dfa, marker='o')
plt.xlabel('lg(n)')
plt.ylabel('lg(DFA)')
# plt.title('Dependence of lg(DFA) on lg(n)')
plt.show()
