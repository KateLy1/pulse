import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
with open("fitness.txt", "r") as f:
    lines = f.readlines()[10:5835]
    data1 = np.asarray(lines, dtype = int)
with open("fitness.txt", "r") as f:
    lines = f.readlines()[11:]
    data2 = np.asarray(lines, dtype = int)
data = data1-data2
measures = data*0.119

pressure = np.linspace(0, 60.00, num = 5825)
fig, ax = plt.subplots(figsize =(100, 10))
ax.set_title("Пульс после физической нагрузки")
plt.plot(pressure, 
        measures,
        linewidth = 1,
        color = 'orange',
        ls='-', 
        ms = 1,
        label = 'Пульс 113[уд./мин.]')
ax.minorticks_on()
ax.grid(axis = 'both')
ax.grid(which = 'major',
        color ='gray')
ax.grid(which = 'minor',
        color ='gray',
        linestyle = '--')
ax.set_xlabel('Время [с]')
ax.set_ylabel('Изменение давления в артерии [мм рт. ст.]')
i = 0
location = ['upper right']
ax.legend(loc = location[i])

plt.show()
fig.savefig('fitness-pulse')