import matplotlib.pyplot as plt
from constants import RPI_0_COORDINATES, RPI_1_COORDINATES, RPI_2_COORDINATES, PHONE_COORDINATES

def plot_circles(radius_0, radius_1, radius_2):
    figure, axes = plt.subplots()
    rectangle = plt.Rectangle((0,0), 29, 34)
    axes.add_artist(rectangle)
    rectangle.set_facecolor('none')
    rectangle.set_edgecolor('black')

    phone = plt.Rectangle(PHONE_COORDINATES, 1, 1)
    axes.add_artist(phone)
    phone.set_facecolor('cyan')
    phone.set_edgecolor('cyan')

    circle_0 = plt.Circle(RPI_0_COORDINATES, radius_0)
    axes.add_artist( circle_0 )
    circle_0.set_facecolor('none')
    circle_0.set_edgecolor('blue')
    plt.plot(0, 0, 'o', color='blue')

    circle_1 = plt.Circle(RPI_1_COORDINATES, radius_1)
    axes.add_artist( circle_1 )
    circle_1.set_facecolor('none')
    circle_1.set_edgecolor('green')
    plt.plot(29, 22, 'o', color='green')

    circle_2 = plt.Circle(RPI_2_COORDINATES, radius_2)
    axes.add_artist( circle_2 )
    circle_2.set_facecolor('none')
    circle_2.set_edgecolor('red')
    plt.plot(0, 34, 'o', color='red')

    axes.set_aspect(1)
    plt.xlim(-20, 50)
    plt.ylim(-10, 50)

    axes.legend([circle_0, circle_1, circle_2, phone, rectangle], ["rpi_node_0", "rpi_node_1", "rpi_node_2", "phone position", "apartment outline"])

    plt.title('Phone Trilateration')
    plt.show()

plot_circles(7.943282347242816, 26.6072505979881, 22.3872113856834)