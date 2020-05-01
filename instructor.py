from nssperson import NSSPerson
# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

class Instructor(NSSPerson):

    def __init__(self, firstName, lastName, slack):
        super().__init__(firstName, lastName, slack)
        self.specialty = ""

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)