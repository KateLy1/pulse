import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
with open("rest.txt", "r") as f:
    lines = f.readlines()[10:5832]
    data1 = np.asarray(lines, dtype = int)
with open("rest.txt", "r") as f:
    lines = f.readlines()[11:]
    data2 = np.asarray(lines, dtype = int)
data = data1-data2

measures = data*0.119
pressure = np.linspace(0, 60.01, num = 5822)
fig, ax = plt.subplots(figsize =(100, 10))
ax.set_title("Пульс до физической нагрузки")
plt.plot(pressure, 
        measures,
        linewidth = 1,
        color = 'blue',
        ls='-', 
        ms = 1,
        label = 'Пульс 57 [уд./мин.]')
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
fig.savefig('rest-pulse')