from math import sin, cos, radians
from matplotlib import pyplot as plt


class Cannon:
    """
    Ágyú osztály
    """
    GRAVITY = -9.8  # Gravity constant (m/s^2)

    def __init__(self, x0, y0, v, angle):
        """
        Initializes the cannon.
        :param x0: initial x-coordinate
        :param y0: initial y-coordinate
        :param v: initial velocity
        :param angle: shooting angle (degrees)
        """
        self.x, self.y = x0, y0
        self.vx = v * cos(radians(angle))  # Horizontal velocity
        self.vy = v * sin(radians(angle))  # Vertical velocity
        self.ax, self.ay = 0, self.GRAVITY  # Accelerations
        self.time = 0  # Elapsed time
        self.xarr = [self.x]  # List of x-coordinates
        self.yarr = [self.y]  # List of y-coordinates

    def update_velocity(self, dt, axis):
        """
        Updates velocity for the given axis.
        :param dt: time step (s)
        :param axis: 'x' or 'y' for the respective axis
        """
        if axis == 'x':
            self.vx += self.ax * dt
            return self.vx
        elif axis == 'y':
            self.vy += self.ay * dt
            return self.vy

    def update_position(self, dt, axis):
        """
        Updates position for the given axis based on velocity and acceleration.
        :param dt: time step (s)
        :param axis: 'x' or 'y' for the respective axis
        """
        if axis == 'x':
            self.x += 0.5 * (self.vx + self.update_velocity(dt, 'x')) * dt
            return self.x
        elif axis == 'y':
            self.y += 0.5 * (self.vy + self.update_velocity(dt, 'y')) * dt
            return self.y

    def step(self, dt):
        """
        Advances simulation by one time step.
        :param dt: time step (s)
        """
        self.xarr.append(self.update_position(dt, 'x'))
        self.yarr.append(self.update_position(dt, 'y'))
        self.time += dt


def make_shoot(x0, y0, velocity, angle):
    """
    Simulates a cannon shot.
    :param x0: initial x-coordinate
    :param y0: initial y-coordinate
    :param velocity: initial velocity
    :param angle: shooting angle (degrees)
    :return: tuple of lists (x-coordinates, y-coordinates)
    """
    cannon = Cannon(x0, y0, velocity, angle)
    dt = 0.05

    while cannon.y >= 0:
        cannon.step(dt)

    return cannon.xarr, cannon.yarr


def main():
    """
    Main program for simulating cannon shots at different angles.
    """
    x0, y0, velocity = 0, 0, 10

    # Simulate shots at different angles
    angles = [45, 46, 47]
    results = [make_shoot(x0, y0, velocity, angle) for angle in angles]

    # Find the longest shot
    max_distance = 0
    max_angle = 0
    max_xarr = []
    max_yarr = []
    for (x, y), angle in zip(results, angles):
        if max(x) > max_distance:
            max_distance = max(x)
            max_angle = angle
            max_xarr = x
            max_yarr = y

    # Plot results
    for (x, y), angle in zip(results, angles):
        plt.plot(x, y, label=f"{angle} deg shoot")

    # Annotate the longest shot
    plt.plot(max_xarr, max_yarr, "mo-", label=f"Longest shot ({max_angle} deg)")
    plt.text(max_distance, 0, f"Longest: {max_distance:.2f} m",
             horizontalalignment='center', color='purple', fontsize=10)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend()
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.show()


if __name__ == "__main__":
    main()
