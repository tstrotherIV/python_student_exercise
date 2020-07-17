class Instructor:

    def __init__(self, name, slack, cohort, specialty):
        self.name = name
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def add_exercises(self, student, exercises):
        student.exercises.extend(exercises)
