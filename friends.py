class Friend:
    """
    Haverok osztálya
    """
    def __init__(self, name):
        self.name = name
        self.job = "None"
        self.age = "None"

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job


x = Friend('ALice')
y = Friend('Bob')
z = Friend('Jim')

nepek = (x, y, z)

x.setJob("Carpenter")
y.setJob("Stagehand")
z.setAge(42)
z.setJob('Electrician')
x.setAge(27)
y.setAge(35)

for nep in nepek:
    print("{} is: {}, age: {}".format(nep.name, nep.job, nep.age))
