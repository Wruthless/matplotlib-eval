from random import Random
import matplotlib.pyplot as plt

from random_walks import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(16,9))
    ax.scatter(rw.x_values, rw.y_values, s=15)
    
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Show first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)

    # Axes are not needed
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()    
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break