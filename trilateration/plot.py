import matplotlib.pyplot as plt
from constants import RPI_0_COORDINATES, RPI_1_COORDINATES, RPI_2_COORDINATES

def plot_circles(radius_0, radius_1, radius_2):
    figure, axes = plt.subplots()
    rectangle = plt.Rectangle((0,0), 29, 34)
    axes.add_artist(rectangle)
    rectangle.set_facecolor('none')
    rectangle.set_edgecolor('black')

    circle_0 = plt.Circle(RPI_0_COORDINATES, radius_0)
    axes.add_artist( circle_0 )
    circle_0.set_facecolor('none')
    circle_0.set_edgecolor('blue')

    circle_1 = plt.Circle(RPI_1_COORDINATES, radius_1)
    axes.add_artist( circle_1 )
    circle_1.set_facecolor('none')
    circle_1.set_edgecolor('green')

    circle_2 = plt.Circle(RPI_2_COORDINATES, radius_2)
    axes.add_artist( circle_2 )
    circle_2.set_facecolor('none')
    circle_2.set_edgecolor('red')

    axes.set_aspect(1)
    plt.xlim(-20, 50)
    plt.ylim(-20, 50)

    plt.title('Phone Trilateration')
    plt.show()

plot_circles(15, 25, 20)