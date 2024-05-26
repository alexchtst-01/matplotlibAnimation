import numpy as np
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.axis('off')

imageStore = []
for i in range(10):
    imageStore.append(np.random.rand(512, 512))

animated_frame = ax.imshow(imageStore[0])

def update(frame):
    animated_frame.set_data(imageStore[frame])
    return animated_frame

animation = FuncAnimation(fig=fig, func=update, frames=10, interval=25)

plt.show()