from math import sin, radians, degrees, asin


def calculate_angle_for_distance(velocity, distance, gravity):
    """
    Calculates the angle(s) needed to achieve the given horizontal distance
    for a projectile launched with a given velocity and gravity.

    :param velocity: Initial velocity of the projectile (m/s)
    :param distance: Target horizontal distance (m)
    :param gravity: Gravitational acceleration (m/s^2)
    :return: Tuple of two possible angles (degrees) or None if no solution exists
    """
    max_distance = (velocity ** 2) / gravity
    if distance > max_distance:
        return None  # The requested distance is not achievable
    
    # Calculate the angles using the inverse sine function
    angle_radians_1 = 0.5 * asin((distance * gravity) / (velocity ** 2))
    angle_radians_2 = radians(90) - angle_radians_1  # The complementary angle

    # Convert to degrees
    angle_1 = degrees(angle_radians_1)
    angle_2 = degrees(angle_radians_2)

    return angle_1, angle_2


def main():
    """
    Main function to calculate and display the shooting angles for a given distance.
    """
    try:
        # Take inputs for distance, velocity, and gravity
        velocity = float(input("Enter the initial velocity of the projectile (m/s): "))
        distance = float(input("Enter the target horizontal distance (m): "))
        gravity = 9.81

        # Validate inputs
        if velocity <= 0 or distance <= 0 or gravity <= 0:
            print("Error: All input values must be positive!")
            return

        angles = calculate_angle_for_distance(velocity, distance, gravity)

        if angles is None:
            print("The given distance is not achievable with the provided velocity and gravity.")
        else:
            print(f"\nThe projectile can reach the distance of {distance} meters at:")
            print(f" - {angles[0]:.1f} degrees")
            print(f" - {angles[1]:.1f} degrees (complementary angle)")
    except ValueError:
        print("Error: Please enter valid numeric values for velocity, distance, and gravity.")


if __name__ == "__main__":
    main()