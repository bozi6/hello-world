"""Friend osztály és használata."""


class Friend:
    """Haverok osztálya."""

    def __init__(self, name):
        """név,munka,kor beállítása."""
        self.name = name
        self.job = "None"
        self.age = "None"

    def getAge(self):
        """
        Return age.

        :return: self.age
        :rtype: str

        """
        return self.age

    def setAge(self, age):
        """
        Set age.

        :return: self.age
        :rtype: str

        """
        self.age = age

    def getJob(self):
        """Munka lekérdezése."""
        return self.job

    def setJob(self, job):
        """Munka beállítása."""
        self.job = job


def main():
    """
    Főprogrm.

    :return: emberkék nevét és életkorát írja ki
    :rtype: object

    """
    x = Friend("ALice")
    y = Friend("Bob")
    z = Friend("Jim")

    nepek = (x, y, z)

    x.setJob("Carpenter")
    y.setJob("Stagehand")
    z.setAge(42)
    z.setJob("Electrician")
    x.setAge(27)
    y.setAge(35)

    for nep in nepek:
        print("{} is: {}, age: {}".format(nep.name, nep.job, nep.age))


if __name__ == "__main__":
    main()
