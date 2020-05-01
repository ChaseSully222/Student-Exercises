# Find any common properties and/or behaviors on students and instructors and create a new parent class for both of them to inherit from.

class NSSPerson():
    def __init__(self, firstName, lastName, slack):
        self.firstName = firstName
        self.lastName = lastName
        self.slack = slack
        self.cohort = ""