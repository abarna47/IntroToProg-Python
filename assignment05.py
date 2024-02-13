# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates data processing using dictionaries and exception handling
# Change Log: (Who, When, What)
# Abarna,2/12/2024, Created Script
# ------------------------------------------------------------------------------------------ #
#include sys module
import sys

#creating constants for a course registration program
MENU: str = """
----Course Registration Program----
Select from the following menu
1. Register a student for a course
2. Show current data
3. Save data to the file
4. Exit the program
------------------------------------
"""
FILE_NAME: str = "Enrollments.csv"

#variable declaration
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file = None
csv_data: str =""
menu_choice: str = ""
student_data: dict = {}
students: list = []

#Reading from Enrollments.csv 
try:
    with open(FILE_NAME, 'r') as file:
        all_students = file.readlines()
        
#file not found error
except FileNotFoundError:
    print(f"Error : The file {FILE_NAME} was not found")
    
#list of strings to list of dictionary  
for student in all_students:
    try:
        csv_data = student.strip().split(',')
        student_data = {
            "student_first_name" : csv_data[0],
            "student_last_name" : csv_data[1],
            "course_name" : csv_data[2]
        }
        students.append(student_data)
        
    # Index out of range
    except IndexError:
        print("Error: Not enough data fields")

#Creating a while loop
while True:
    print(MENU)
    menu_choice = input("what would you like to do: ")

    #using match-case statement
    match menu_choice:
        
        #collect user data and add to the list of dictionary rows
        case "1":
            try:
                student_first_name = input("Enter student's first name: ")
                student_last_name = input("Enter student's last name: ")

            #value error    
            except ValueError:
                print(f'Name should not contain numeric values')
                
            course_name = input("Enter the course name: ")
            student_data = {
                "student_first_name" : student_first_name,
                "student_last_name" : student_last_name,
                "course_name" : course_name
                }
            students.append(student_data)
            
         #print data to the user
        case "2":
            for student in students:
                print(f"{student['student_first_name']}\t\t{student['student_last_name']}\t\t{student['course_name']}")

        #writing data to the file
        case "3":
            try:
                file = open(FILE_NAME, 'w')
                for student in students:
                    file.write(f"{student['student_first_name']},{student['student_last_name']},{student['course_name']}\n")
                    print(f"You have registered {student['student_first_name']} {student['student_last_name']} for {student['course_name']}")
                file.close()
                
            #Input/Output operation fails    
            except IOError:
                print("Error: There was an issue writing to the file.")

        #exit out of the program
        case "4":
            print("program ends")
            sys.exit()
        case _:
            print("Choose one of the options from above")
            
                
                
            
