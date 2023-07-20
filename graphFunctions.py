import numpy as np
from database import *

def graph_random_data(x, ax, canvas, minValue=-40, maxValue=40):
    ax.clear()
    if len(x)>20:
        x.pop(0)
    x.append(np.random.uniform(-40, 40))
    ax.plot(x, "-o", color='blue')
    ax.set_ylim(-40, 40)
    ax.set_xlim(0, 20)
    ax.set_xticks(np.arange(1, 20))
    ax.grid()
    canvas.draw()

def graph_openweathermap(x, ax, canvas):
    dataJSON=getAPIData()['list'][-21:]
    x.clear()
    ax.clear()
    [x.append(it['main']['temp']) for it in dataJSON]
    ax.plot(x, "-o", color='blue')
    ax.set_ylim(-40, 40)
    ax.set_xlim(0, 20)
    ax.set_xticks(np.arange(1, 20))
    ax.grid()
    canvas.draw()

