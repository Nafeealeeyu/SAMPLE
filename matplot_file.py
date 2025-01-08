import matplotlib.pyplot as plt
import numpy as np
x_axis = np.array([1, 15, 40, 20, 5])
y_axis = np.array([10, 180, 15, 50, 40])
plt.plot(y_axis, marker='o', linestyle="dashed", color="black")
plt.title('REAL TIME ANALYSIS')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
