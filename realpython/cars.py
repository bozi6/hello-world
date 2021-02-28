class Car:
    # attributes
    year = 2016
    mpg = 20
    speed = 100

    # methods
    def accelerate(self):
        return self.speed + 20

    def brake(self):
        return self.speed - 50


car1 = Car()

print(car1.accelerate())
print(car1.brake())
print(car1.year)
print(car1.mpg)
print(car1.speed)


class MyCompany:
    # Class variable - osztály változó
    growth = 0.1

    def __init__(self, compname, revenue, employesize):
        # instance variable - példány változók
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employesize


print(MyCompany.growth)

Bank = MyCompany('DBA Bank', 50000, 1000)
print(Bank.revenue)


class Cab:
    # Initialize variables for first iteration
    numberofcabs = 0
    numberofpassengers = 0

    def __init__(self, driver, kms, places, pay, passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs += 1
        Cab.numberofpassengers += 1

    # Returns price of cab fare per km
    def rateperkm(self):
        return self.bill / self.running

    # Returns number of cabs running
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs

    # Returns average number of passengers travelling in a cab
    @classmethod
    def avgnoofpassengers(cls):
        return int(cls.numberofpassengers / cls.numberofcabs)


firstcab = Cab("Ranesh", 80, ['Delhi', 'Noida'], 2200, 3)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thridcab = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)

print(firstcab.driver)
print(secondcab.driver)
print(thridcab.driver)
print(firstcab.rateperkm())
print(secondcab.rateperkm())
print(thridcab.rateperkm())
print(Cab.noofcabs())
print(Cab.avgnoofpassengers())
print(Cab.numberofpassengers)