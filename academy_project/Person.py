from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Person:
    __first_name = "no name"
    __last_name = "no name"
    __age = 0
    __gender = Gender.MALE

    def __init__(self, first_name, last_name, age, gender):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, f_name):
        if 1 < len(f_name) < 20:
            self.__first_name = f_name
        else:
            print("Incorrect first name length!")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, l_name):
        if 1 < len(l_name) < 20:
            self.__last_name = l_name
        else:
            print("Incorrect last name length!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 16 < age < 120:
            self.__age = age
        else:
            print("Incorrect age!")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gen):
        if gen == Gender.MALE or gen == Gender.FEMALE:
            self.__gender = gen
        else:
            print("Incorrect gender!")

    def walk(self):
        print(f"{self.first_name} is walking")

    def say(self, phrase_to_say):
        print(f"{self.first_name} says: {phrase_to_say}")


# person = Person("Vasya", "Pupkin", 25, Gender.MALE)
# person.walk()
# person.say("hello world!")


class Academy:
    pass


class Teacher:
    pass


class Student:
    pass


class Subject:
    pass
