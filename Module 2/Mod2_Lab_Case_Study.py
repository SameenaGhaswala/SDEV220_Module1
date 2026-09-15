"""File name: Mod2_Lab_Case_Study.py
Description: This app accepts student's name and GPA to test if they qualify for \
Dean's List or Honor Roll.
Author: Sameena Ghaswala"""

while True:
    student_last_name = input("Enter student's last name: ")
    if student_last_name == "ZZZ":
        break
    student_first_name = input("Enter student's first name: ")
    gpa = float(input("Enter GPA: "))
    if gpa >= 3.5:
        print(f"{student_first_name} {student_last_name} have made it to the Dean's List with {gpa} GPA!")
    elif gpa >= 3.25:
        print(f"{student_first_name} {student_last_name} have made it to the Honor Roll with {gpa} GPA!")
