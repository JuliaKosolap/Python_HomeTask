from academy_project.Academy import Academy
from academy_project.Person import Person, Gender


class Student(Person):
    def study(self, academy_name, course_number):
        print(f"{self.first_name} studies in {academy_name.name} academy on the {course_number} course")

    def walk(self):
        print(f"{self.first_name} is walking to the academy")


student = Student('John', 'Dow', 19, Gender.MALE)
academy = Academy("IT", ["Java", "Python", "PHP", "JavaScript", "QA", "UI/UX Design"])
student.study(academy, 2)
student.walk()
student.say("My name is John. I'm a student")

