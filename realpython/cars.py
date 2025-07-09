"""Autok osztálya."""


def main():
    """Legfőbb funkció function."""
    class Car:
        """
        A class representing a car with basic attributes and methods to accelerate and brake.

        Attributes:
            year (int): The manufacturing year of the car. Default is 2016.
            mpg (int): Miles per gallon fuel efficiency. Default is 20.
            speed (int): The current speed of the car in mph. Default is 100.

        Methods:
            accelerate():
                Increases the car's speed by 20 mph.
                Returns the new speed.

            brake():
                Decreases the car's speed by 50 mph.
                Returns the new speed.
        """
        # attributes
        year = 2016
        mpg = 20
        speed = 100

        # methods
        def accelerate(self):
            """
            Increases the current speed of the car by 20 units.

            Returns:
                int: The new speed after acceleration.
            """
            return self.speed + 20

        def brake(self):
            """
            Reduces the current speed of the car by 50 units.

            Returns:
                int: The new speed after braking.
            """
            return self.speed - 50

    car1 = Car()
    print('car1 accelerate:', car1.accelerate())
    print('car1 brake:', car1.brake())
    print('car1 year:', car1.year)
    print('car1 mpg: ', car1.mpg)
    print('car1 speed:', car1.speed)

    class MyCompany:
        """
        MyCompany represents a company with basic financial and employee information.

        Attributes:
            growth (float): Class variable representing the company's growth rate.

        Args:
            compname (str): The name of the company.
            revenue (float): The revenue of the company.
            employesize (int): The number of employees in the company.

        Instance Attributes:
            name (str): The name of the company.
            revenue (float): The revenue of the company.
            no_of_employees (int): The number of employees in the company.
        """
        # Class variable - osztály változó
        growth = 0.1

        def __init__(self, compname, revenue, employesize):
            # instance variable - példány változók
            self.name = compname
            self.revenue = revenue
            self.no_of_employees = employesize

    print('mycompany growth: ', MyCompany.growth)

    bank = MyCompany('DBA Bank', 50000, 1000)
    print('Bank revenue:', bank.revenue)

    class Cab:
        """
        Cab class represents a taxi cab with details about its driver, distance run, places visited, fare, and passengers.

        Class Attributes:
            numberofcabs (int): Total number of Cab instances created.
            numberofpassengers (int): Total number of passengers across all Cab instances.

        Instance Attributes:
            driver (str): Name of the cab driver.
            running (float): Distance run by the cab in kilometers.
            places (list): List of places visited by the cab.
            bill (float): Total fare for the cab ride.

        Methods:
            __init__(self, driver, kms, places, pay, passengers):
                Initializes a Cab instance and updates class counters.

            rateperkm(self):
                Returns the fare per kilometer for the cab ride.

            noofcabs(cls):
                Class method. Returns the total number of cabs.

            avgnoofpassengers(cls):
                Class method. Returns the average number of passengers per cab (rounded down to nearest integer).
        """
        # Initialize variables for first iteration
        numberofcabs = 0
        numberofpassengers = 0

        def __init__(self, driver, kms, places, pay, passengers):
            self.driver = driver
            self.running = kms
            self.places = places
            self.bill = pay
            Cab.numberofcabs += 1
            Cab.numberofpassengers += 1 + passengers

        # Returns price of cab fare per km
        def rateperkm(self):
            """
            Calculates the rate per kilometer by dividing the total bill by the total running distance.

            Returns:
                float: The cost per kilometer.
            """
            return self.bill / self.running

        # Returns number of cabs running
        @classmethod
        def noofcabs(cls):
            """
            Returns the total number of cabs.

            Returns:
                int: The current value of the class attribute 'numberofcabs'.
            """
            return cls.numberofcabs

        # Returns average number of passengers travelling in a cab
        @classmethod
        def avgnoofpassengers(cls):
            """
            Calculates the average number of passengers per cab.

            Returns:
                int: The average number of passengers per cab, computed as the total number of passengers divided by the total number of cabs.
            """
            return int(cls.numberofpassengers / cls.numberofcabs)

    firstcab = Cab("Ranesh", 80, ['Delhi', 'Noida'], 2200, 3)
    secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
    thridcab = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)

    print('Firstcab driver:', firstcab.driver)
    print('Secondcab driver:', secondcab.driver)
    print('Thirdcab driver:', thridcab.driver)
    print('Firstcab rateperkm:', firstcab.rateperkm())
    print('Secondcab rateperkm:', secondcab.rateperkm())
    print('Thirdcab rateperkm:', thridcab.rateperkm())
    print('Cab number of cabs:', Cab.noofcabs())
    print('Cab average number of passengers:', Cab.avgnoofpassengers())
    print('Cab number of passengers:', Cab.numberofpassengers)


if __name__ == '__main__':
    main()
