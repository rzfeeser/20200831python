#!/usr/bin/python

class Dog:
    def __init__(self, name, age, breed, trained):
        self.name = name
        self.age = age
        self.breed = breed
        self.trained = trained

    def __str__(self):
        return self.name

    def rename(self, newname):
        self.name = newname

    def older(self, years):
        self.age += years

    def dnacheck(self, realbreed):
        self.breed = realbreed

    def school(self, isTrained):
        self.trained = isTrained


def main():
    woof = Dog("Fido", 77, "goldendog", True)

    print(woof)

    print(woof.age)
    print(woof.breed)
    print(woof.trained)

    woof.rename("Larry The Dog")

    print(woof)

    woof.older(-70)

    print(woof.age)

main()
