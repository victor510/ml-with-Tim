import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw =RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
# plt.savefig('squares_plot.png', bbox_inches='tight')

# Emphasize on first and last points

plt.scatter(0,0, c='green', edgecolors='none', s=25)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
# cleaning up the axis
#
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

# Set the figsize
# plt.figure(figsize=(10, 6))


plt.show()
