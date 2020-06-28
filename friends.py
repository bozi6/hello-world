class Friend:
    def __init__(self):
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


Alice = Friend()
Bob = Friend()

Alice.setJob("Carpenter")
Bob.setJob("Stagehand")
Alice.setAge(27)
Bob.setAge(35)

print("Bob is: {}, age: {}".format(Bob.job, Bob.age))
print("Alice is: {}, age: {}".format(Alice.job, Alice.age))
