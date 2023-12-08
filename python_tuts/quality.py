import doctest
import pprint
import textwrap


def average(values):
    """Kiszámolja a számtani közepét a megadott számoknak

    >>> print(average([20 ,30, 70]))
    40.0

    :return: Sum the values
    :rtype: float

    """
    return sum(values) / len(values)


if __name__ == "__main__":
    doctest.testmod()
    t = [
        [
            [["black", "cyan"], "white", ["green", "red"]],
            [["magenta", "yellow"], "blue"],
        ]
    ]

    pprint.pprint(t, width=30)
    doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""
    print(textwrap.fill(doc, width=40))
