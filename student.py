from nssperson import NSSPerson


class Student(NSSPerson):

    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(slack, cohort)
        self.first_name = first_name
        self.last_name = last_name
        self.exercises = list()
