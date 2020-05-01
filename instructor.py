# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

class Instructor:

    def __init__(self, firstName, lastName, slack):
        self.firstName = firstName
        self.lastName = lastName
        self.slack = slack
        self.cohort = ""
        self.specialty = ""

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)