from nssperson import NSSPerson


class Instructor(NSSPerson):

    def __init__(self, name, slack, cohort, specialty):
        super().__init__(slack, cohort)
        self.name = name
        self.specialty = specialty

    def add_exercises(self, student, exercises):
        student.exercises.extend(exercises)
