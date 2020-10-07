# Ryan Soderberg
# DS2000-Sec02

grade_weights = input("Enter grade weights: ").split(" ")

course_grade = 0

for i in grade_weights:
    # Make a list of assignments grades for a given weight
    assignment_list = input(f"Enter grades ({i}%): ").split(" ")
    int_assignment_list = [int(i) for i in assignment_list]

    # Calculate avg assignment grade for given weight
    assignments_avg = sum(int_assignment_list) / len(int_assignment_list) * int(i) / 100

    course_grade += assignments_avg

print(round(course_grade))