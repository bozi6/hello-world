# Convert the following JSON into Vehicle Object
import json


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehileDecoder(obj):
    """
    Jármű dekódoló

    :param obj: jsonból kikódolt objektum
    :type obj: json object
    :return: Vehicle tömb
    :rtype: list

    """
    return Vehicle(obj["name"], obj["engine"], obj["price"])


if __name__ == "__main__":
    vehicleObj = json.loads(
        '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}',
        object_hook=vehileDecoder,
    )
    print("Type of decoed object from JSON data")
    print(type(vehicleObj))
    print("Vehicle Details:")
    print(
        " Name: {}\n Engine: {}\n Price: {}".format(
            vehicleObj.name, vehicleObj.engine, vehicleObj.price
        )
    )
