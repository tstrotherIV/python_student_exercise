from exercise import Exercise
from cohort import Cohort
from student import Student
from instructor import Instructor

# Problem: Create 4, or more, exercises
exercise1 = Exercise("Exercise1", "Python")
exercise2 = Exercise("Exercise2", "Javascript")
exercise3 = Exercise("Exercise3", "Node")
exercise4 = Exercise("Exercise4", "Django")

exercises = [exercise1, exercise2, exercise3, exercise4]
exercises = list(exercises)

# Problem: Create 3, or more, cohorts
cohort1 = Cohort("Cohort 40")
cohort2 = Cohort("Cohort 41")
cohort3 = Cohort("Cohort 42")

# Problem: Create 4, or more, students and assign them to one of the cohorts
Jimmy = Student("Jimmy", "Johnson", "@awesome1", "Cohort 40")
Ashley = Student("Ashley", "Riker", "@awesome2", "Cohort 41")
Brian = Student("Brian", "Knoles", "@awesome3", "Cohort 42")
Eve = Student("Eve", "Nelson", "@awesome4", "Cohort 40")

# Problem: Eve.add_exercises()
students = [Jimmy, Ashley, Brian, Eve]
students = list(students)

# Problem: Create 3, or more, instructors and assign them to one of the cohorts.
Joe = Instructor("Joe", "@instructor1", "Cohort 40", "Voices")
Bryan = Instructor("Bryan", "@instructor2", "Cohort 41", "Dad Jokes")
Sage = Instructor("Sage", "@instructor3", "Cohort 42", "getting banned")

# Problem: Have each instructor assign 2 exercises to each of the students
Joe.add_exercises(Eve, [exercise1, exercise2])
Bryan.add_exercises(Jimmy, [exercise2, exercise3])
Sage.add_exercises(Ashley, [exercise3, exercise4])
Joe.add_exercises(Brian, [exercise1, exercise2])

# Chapt 14 challenge


def newStr(student):
    for exercise in Ashley.exercises:
        print(f"{student.first_name} is working on {exercise.name} ")


newStr(Eve)
