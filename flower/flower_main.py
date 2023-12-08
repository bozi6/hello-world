import turtle


def main():
    """
    Draw a flower with turtle

    :return: Nice flower
    :rtype: turtle object

    """
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("white")
    t.speed(0)
    col = ("yellow", "red", "green", "lime", "light green", "blue")

    for i in range(150):
        t.pencolor(col[i % 6])
        t.circle(190 - i / 2, 90)
        t.lt(90)
        t.circle(190 - i / 3, 90)
        t.lt(60)
    s.exitonclick()


if __name__ == "__main__":
    main()
