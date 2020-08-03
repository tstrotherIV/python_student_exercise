import sqlite3


class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in Cohort {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from students s
            join cohort c on s.cohort_id = c.Id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def assigned_exercises(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.name,
                s.Id,
                s.first_name,
                s.last_name
            from exercise e
            join student_exercise se on se.exercise_id = e.Id
            join students s on s.Id = se.student_id
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)

            # print(exercises)

        for exercise_name, students in exercises.items():
            print(f'{exercise_name}')
            for student in students:
                print(f'\t* {student}')

    def student_assigned_exercises(self):

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.name,
                s.Id,
                s.first_name,
                s.last_name
            from exercise e
            join student_exercise se on se.exercise_id = e.Id
            join students s on s.Id = se.student_id
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if student_name not in students:
                students[student_name] = [exercise_name]
            else:
                students[student_name].append(exercise_name)

            # print(exercises)

        for student_name, exercises in students.items():
            print(f'{student_name} is working on')
            for exercise in exercises:
                print(f'\t* {exercise}')

    def instructor_assigned_exercises(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.name ExerciseName,
                i.Id,
                i.name
            from exercise e
            join instructors i on instructor_assigned = i.Id;
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            instructor_id = row[2]
            instructor_name = f'{row[3]}'

            if instructor_name not in instructors:
                instructors[instructor_name] = [exercise_name]
            else:
                instructors[instructor_name].append(exercise_name)

            # print(exercises)

        for instructor_name, exercises in instructors.items():
            print(f'{instructor_name} has assigned')
            for exercise in exercises:
                print(f'\t* {exercise}')

    def assigned_exercises(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.name,
                s.Id,
                s.first_name,
                s.last_name
            from exercise e
            join student_exercise se on se.exercise_id = e.Id
            join students s on s.Id = se.student_id
            """)

        dataset = db_cursor.fetchall()

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)

            # print(exercises)

        for exercise_name, students in exercises.items():
            print(exercise_name)
            for student in students:
                print(f'\t* {student}')


reports = StudentExerciseReports()
# reports.all_students()
reports.assigned_exercises()
reports.student_assigned_exercises()
reports.instructor_assigned_exercises()


class Cohorts():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class CohortReports():

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_cohorts(self):
        """Retrieve cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohorts(
                row[0]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT cohort.name as 'Cohort Name'
            FROM cohort
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)


reports = CohortReports()
reports.all_cohorts()


class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} with {self.language}'


class ExerciseReports():

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_exercises(self):
        """Retrieve exercise name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise.name as "Exercise Name", exercise.language as 'language'
            FROM exercise
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


reports = ExerciseReports()
reports.all_exercises()


class JavaScriptExercises():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} with {self.language}'


class JavaScriptExerciseseports():

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_javascript_exercises(self):
        """Retrieve all JavaScript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: JavaScriptExercises(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise.name as "Exercise Name", exercise.language as 'language'
            FROM exercise
            WHERE exercise.language = "JavaScript"
            """)

            all_javascript_exercises = db_cursor.fetchall()

            for exercise in all_javascript_exercises:
                print(exercise)


reports = JavaScriptExerciseseports()
reports.all_javascript_exercises()


class PythonExercises():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} with {self.language}'


class PythonExerciseseports():

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_python_exercises(self):
        """Retrieve all Python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: PythonExercises(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise.name as "Exercise Name", exercise.language as 'language'
            FROM exercise
            WHERE exercise.language = "Python"
            """)

            all_python_exercises = db_cursor.fetchall()

            for exercise in all_python_exercises:
                print(exercise)


reports = JavaScriptExerciseseports()
reports.all_javascript_exercises()


class Instructor():

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def __repr__(self):
        return f'Instructor {self.name} is in Cohort {self.cohort}'


class InstructorReports():

    """Methods for reports on the Instructors"""

    def __init__(self):
        self.db_path = "/Users/tomstrother/workspace/C40/backend/python/StudentExercises/studentexercises.db"

    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[0], row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.name as 'Instructor Name', c.name as 'Cohort'
            from instructors i
                join cohort c on i.cohort_id = c.Id
            order by i.cohort_id
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)


reports = InstructorReports()
reports.all_instructors()
