DELETE FROM cohort;
DELETE FROM instructors;
DELETE FROM students;
DELETE FROM exercise;
DELETE FROM student_exercise;

DROP TABLE IF EXISTS cohort;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS student_exercise;

CREATE TABLE "cohort"
(
    "Id" INTEGER NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE
);

CREATE TABLE "instructors" (
    "Id" INTEGER NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "slack_handle" TEXT NOT NULL,
    "cohort_id" INTEGER NOT NULL,
    "specialty" TEXT NOT NULL,
    FOREIGN KEY
(`cohort_id`) REFERENCES "cohort"
(`Id`)
);


CREATE TABLE "students" (
    "Id" INTEGER NOT NULL PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "slack_handle" TEXT NOT NULL,
    "cohort_id" INTEGER NOT NULL,
    FOREIGN KEY
(`cohort_id`) REFERENCES "cohort"
(`Id`)
);


CREATE TABLE "exercise"
(
    "Id" INTEGER NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "language" TEXT NOT NULL
);

CREATE TABLE "student_exercise" (
	"Id" INTEGER NOT NULL PRIMARY KEY,
    "exercise_id" INTEGER NOT NULL,
    "student_id" INTEGER NOT NULL,
    FOREIGN KEY
(`exercise_id`) REFERENCES "exercise"
(`Id`),
    FOREIGN KEY
(`student_id`) REFERENCES "students"
(`Id`)
);

-- 3 cohorts
INSERT INTO cohort
    (Name)
VALUES
    ('40');

INSERT INTO cohort
    (Name)
VALUES
    ('41');

INSERT INTO cohort
    (Name)
VALUES
    ('42');


-- 5 exercises

INSERT INTO exercise
    (Name, Language)
VALUES
    ('Kandy Korner', 'React');

INSERT INTO exercise
    (Name, Language)
VALUES
    ('Nutshell', 'JavaScript');

INSERT INTO exercise
    (Name, Language)
VALUES
    ('Arberoteum', 'Python');

INSERT INTO exercise
    (Name, Language)
VALUES
    ('MyListing360', 'React');

INSERT INTO exercise
    (Name, Language)
VALUES
    ('Daily Journal', 'JavaScript');


-- 3 instructors
INSERT INTO instructors
    (name, Slack_handle, Cohort_id, specialty)
VALUES
    ('Joe', '@instructor1', 1, "Voices");

INSERT INTO instructors
    (name, Slack_handle, Cohort_id, specialty)
VALUES
    ('Bryan', '@instructor2', 2, "Dad Jokes");

INSERT INTO instructors
    (name, Slack_handle, Cohort_id, specialty)
VALUES
    ('Sage', '@instructor3', 3, "getting banned");



-- 7 students
INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Jimmy', 'Johnson', "@awesome1", 1);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Ashley', 'Riker', "@awesome2", 2);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Brian', 'Knoles', "@awesome3", 3);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Jared', 'Right', "@awesome4", 2);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Ryan', 'Hint', "@awesome5", 1);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Ritta', 'Hines', "@awesome6", 2);

INSERT INTO students
    (first_name, last_name, slack_handle, cohort_id )
VALUES
    ('Austin', 'Anderson', "@awesome7", 3);



INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (1, 1);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (1, 2);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (2, 2);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (2, 3);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (3, 3);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (3, 5);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (4, 1);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (4, 5);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (5, 2);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (5, 4);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (6, 4);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (6, 5);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (7, 1);

INSERT INTO student_exercise
    (student_id, exercise_id)
VALUES
    (7, 3);


select i.name as 'Instructor Name', c.name as 'Cohort'
from instructors i
    join cohort c on i.cohort_id = c.Id
order by i.cohort_id
