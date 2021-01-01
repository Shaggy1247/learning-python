# -----------------------------------------------------------
# Lesson twentyone
# Learning about creating classes
#
# Done 12/31/20, Shaggy1247
# -----------------------------------------------------------

class Dog(object):
    def __init__(self, name, age):
        self.name = name        # Attribute
        self.age = age
        self.li = [1, 2, 3, 4]
        # print("Nice you made a Dog")

    def speak(self):    # Method

        print("Hi I am", self.name, "and I am", self.age, "years old")

    def change_age(self, age):
        self.age = age


traven = Dog("Traven", 5)
traven.speak()
traven.change_age(2)
traven.speak()

print(traven.age)
print(traven.li)
