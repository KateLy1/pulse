import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def summ(filename, a):
    with open(filename) as f:
        lines = f.readlines()[11:]
        sum = 0
        data = np.asarray(lines, dtype=int)
        for i in range (a):
            sum = data[i] + sum
        delsum = round(sum / a)
    return delsum

a = summ("40 mmHg.txt", 973)
b = summ("80 mmHg.txt", 971)
c = summ("120 mmHg.txt", 969)
d = summ("160 mmHg.txt", 973)
measures = [a, b, c, d]
pressure = [40, 80, 120, 160]
fig, ax = plt.subplots()
ax.set_title("Калибровочный график зависимости показаний АЦП от давления")
plt.plot(pressure, measures,
        linewidth = 3,
        color = 'orange',
        ls='-', 
        ms = 10,
        label = 'Измерения')
plt.plot(pressure, measures,
        linewidth = 3,
        color = 'blue',
        ls='None', 
        ms = 10,
        marker = '*',
        markeredgecolor = 'blue',
        label = 'P = 0.102*N-10.27[Па]')
ax.minorticks_on()
ax.grid(axis = 'both')
ax.grid(which = 'major',
        color ='gray')
ax.grid(which = 'minor',
        color ='gray',
        linestyle = '--')
ax.set_xlabel('Давление [Па]')
i = 0
location = ['upper left']
ax.legend(loc = location[i])
ax.set_ylabel('Отсчёты АЦП')
plt.show()
fig.savefig('калибровка')