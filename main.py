from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# The learning objective of this exercise is to practice creating instances of custom types that you defined with class, establishing the relationships between them, and practicing basic data structures in Python.

# Create 4, or more, exercises.
exercise1 = Exercise("Exercise 1", "HTML")
exercise2 = Exercise("Exercise 2", "JavaScript")
exercise3 = Exercise("Exercise 3", "React")
exercise4 = Exercise("Exercise 4", "Python")

# Create 3, or more, cohorts.
cohort41 = Cohort("Cohort 41")
cohort42 = Cohort("Cohort 42")
cohort43 = Cohort("Cohort 43")

# Create 4, or more, students and assign them to one of the cohorts.
student1 = Student("Fynley", "Wiggins", "wigginslack")
student2 = Student("Vikki","Vaillancourt","vikkislack")
student3 = Student("Jimmy", "John", "jimmieJsSlack")
student4 = Student("John", "Smith", "jsmithslack")

cohort41.students.append(student1)
cohort42.students.append(student2)
cohort42.students.append(student3)
cohort43.students.append(student4)

# Create 3, or more, instructors and assign them to one of the cohorts.
instructor1 = Instructor("Joey", "Joe", "jojoslack")
instructor2 = Instructor("Lucy", "Lui", "luluslack")
instructor3 = Instructor("Braxton", "Saxton", "braxtonslack")

cohort41.instructors.append(instructor1)
cohort42.instructors.append(instructor2)
cohort43.instructors.append(instructor3)

# Have each instructor assign 2 exercises to each of the students.
instructor1.assign_exercise(student1, exercise1)
instructor1.assign_exercise(student1, exercise2)
instructor1.assign_exercise(student2, exercise1)
instructor1.assign_exercise(student2, exercise2)
instructor1.assign_exercise(student3, exercise3)
instructor1.assign_exercise(student3, exercise4)
instructor1.assign_exercise(student4, exercise3)
instructor1.assign_exercise(student4, exercise4)

instructor2.assign_exercise(student1, exercise1)
instructor2.assign_exercise(student1, exercise2)
instructor2.assign_exercise(student2, exercise1)
instructor2.assign_exercise(student2, exercise2)
instructor2.assign_exercise(student3, exercise3)
instructor2.assign_exercise(student3, exercise4)
instructor2.assign_exercise(student4, exercise3)
instructor2.assign_exercise(student4, exercise4)

instructor3.assign_exercise(student1, exercise1)
instructor3.assign_exercise(student1, exercise2)
instructor3.assign_exercise(student2, exercise1)
instructor3.assign_exercise(student2, exercise2)
instructor3.assign_exercise(student3, exercise3)
instructor3.assign_exercise(student3, exercise4)
instructor3.assign_exercise(student4, exercise3)
instructor3.assign_exercise(student4, exercise4)


#Challenge
students = [student1, student2, student3, student4]
exercises = [exercise1, exercise2, exercise3, exercise4]

for student in students:
  student.student_summary()