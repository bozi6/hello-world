from turtle import *

"""
Nagy piros szív rajzolása.
"""


def main():
    """Főprogram"""
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()


if __name__ == "__main__":
    main()
