# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on


class Student:

    def __init__(self, firstName, lastName, slack):
        self.firstName = firstName
        self.lastName = lastName
        self.slack = slack
        self.cohort = ""
        self.exercises = list()

    def student_summary(self):
        print(f"----Student Summary----")
        print(f"{self.firstName} {self.lastName}")
        print(f"Slack: {self.slack}")
        print(f"Assigned Exercises:")
        for exercise in self.exercises:
            print(f"{exercise.name} {exercise.language}")