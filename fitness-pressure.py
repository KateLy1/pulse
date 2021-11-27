import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
with open("fitness.txt", "r") as f:
    lines = f.readlines()[10:]
    data = np.asarray(lines, dtype = int)

measures = data*0.119
pressure = np.linspace(0, 60.00, num = 5826)
fig, ax = plt.subplots()
ax.set_title("Артериальное давление после физической нагрузки")
ax.scatter(2.22, 157, color = 'red')
plt.text(3.2, 157.2,'Systole')
ax.scatter(32.36, 92.2, color = 'red')
plt.text(34, 92.2,'Diastole')
plt.plot(pressure, 
        measures,
        linewidth = 1,
        color = 'blue',
        ls='-', 
        ms = 10,
        label = 'Давление - 157/92[мм рт. ст.]')
ax.minorticks_on()
ax.grid(axis = 'both')
ax.grid(which = 'major',
        color ='gray')
ax.grid(which = 'minor',
        color ='gray',
        linestyle = '--')
ax.set_xlabel('Время [с]')
i = 0
location = ['upper right']
ax.legend(loc = location[i])
ax.set_ylabel('Давление [мм рт. ст.]')
plt.show()
fig.savefig('fitness-pressure')
