from academy_project.Academy import Academy
from academy_project.Person import Person, Gender


class Teacher(Person):
    def work(self, academy_name, subject_name):
        print(f"{self.first_name} works in {academy_name.name} academy as a teacher of {subject_name}")


teacher = Teacher("Sara", "Wood", 35, Gender.FEMALE)
academy = Academy("IT", ["Python", "PHP", "JavaScript", "QA"])
teacher.work(academy, academy.subjects[0])