class Subject:
    __name = "no name"

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 <= len(name) < 10:
            self.__name = name
        else:
            print("Incorrect subject name length!")
