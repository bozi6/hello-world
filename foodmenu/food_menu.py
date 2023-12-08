# Definig a class food,
# which contain name and price of the food item


class Food(object):
    """
    Food class

    :return: Food price
    :rtype: str

    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getprice(self):
        """
        Set food price

        :return: self.price
        :rtype: int

        """
        return self.price

    def __str__(self):
        return self.name + " : " + str(self.getprice()) + " - Money"


# Definig a function for building a Menu
# which generates list of Food
def buildmenu(names, costs):
    """
    Menu builder

    :param names: get food names in list
    :param costs: get prices in list
    :return: menu list

    """
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu


def hanoi(disks_number):
    if disks_number == 1:
        return 1
    else:
        return 2 * hanoi(disks_number - 1) + 1


def main():
    """
    Főprogram

    :return: kiírja a kjákat és az árakat

    """
    # items
    names = ["Coffee", "Tea", "Pizza", "Burger", "Fries", "Apple", "Donut", "Cake"]

    # prices
    costs = [250, 150, 180, 70, 65, 55, 120, 350]

    # building food menu
    Foods = buildmenu(names, costs)

    n = 1
    for el in Foods:
        print("{}; {}".format(n, el))
        n = n + 1

    x = int(input("ENTER THE NUMBER OF DISKS: "))

    print("NUMBER OF STEPS: ", hanoi(x))
