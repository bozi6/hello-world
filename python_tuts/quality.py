def average(values):
    """Computes the arithmetic mean of a lst of numbers.

    >>> print(average([20 ,30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
     'yellow'], 'blue']]]

pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
