import random

some_exceptions = [ValueError, TypeError, IndexError, None,
                   EOFError, AttributeError, AssertionError,
                   FileExistsError, FileNotFoundError]

try:
    choice = random.choice(some_exceptions)
    print("Létrejön a {} hiba".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Elkaptunk egy ValueError")
except TypeError:
    print("Elkaptunk egy TypeError")
except Exception as e:
    print("Másmilyen hibát kaptunk el: {}".format(e.__class__.__name__))

else:
    print("Ez a kód akkor fut le ha nincs semmilyen hiba")
finally:
    print("Ez a 'takarító kód mindíg meghyívódik.")
