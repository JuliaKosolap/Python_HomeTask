class Academy:
    __name = "no name"
    __subjects = []

    def __init__(self, name, subjects):
        self.__name = name
        self.__subjects = subjects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 <= len(name) < 50:
            self.__name = name
        else:
            print("Incorrect academy name length!")

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, subjects):
        for subject in subjects:
            self.__subjects.append(subject)

