import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
with open("rest.txt", "r") as f:
    lines = f.readlines()[10:]
    data = np.asarray(lines, dtype = int)

measures = data*0.119
pressure = np.linspace(0, 60.01, num = 5823)
fig, ax = plt.subplots()
ax.set_title("Артериальное давление до физической нагрузки")
plt.plot(pressure, 
        measures,
        linewidth = 1,
        color = 'blue',
        ls='-', 
        ms = 10,
        label = 'Давление - 130/80[мм рт. ст.]')
ax.minorticks_on()
ax.scatter(14.2, 130.2, color = 'red')
plt.text(16.2, 130.2,'Systole')
ax.scatter(49.36, 78.2, color = 'red')
plt.text(52, 78.2,'Diastole')
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
fig.savefig('rest-pressure')
