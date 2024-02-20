# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates how to use functions and class
# Change Log: (Who, When, What)
#   Abarna,2/18/2024, Created Script
# ------------------------------------------------------------------------------
import json
import sys
from typing import IO
from json import JSONDecodeError

#creating a constant for a course registration program
MENU: str = """
----Course Registration Program----
Select from the following menu
1. Register a student for a course
2. Show current data
3. Save data to the file
4. Exit the program
------------------------------------
"""
FILE_NAME: str = 'Enrollments.json'
menu_choice: str = ""
students: list = []


class FileProcessor:
    global FILE_NAME
    global students
    global file

# reading the data from json file
    @staticmethod
    def read_data_from_file(FILE_NAME , students) -> dict:
        """
        reads data from specified json file
        :param FILE_NAME
        :param students
        :return: list of students
        """
        try:
            with open(FILE_NAME, 'r') as file:
                students = json.load(file)
            for student in students:
                print(f'{student["first_name"]} {student["last_name"]} {student["course_name"]}')
        except FileNotFoundError as e:
            IO.output_error_message("JSON file not found", e)
            print("Creating a file")
            with open(FILE_NAME, 'w') as file:
                json.dump(file, students)
        except JSONDecodeError as e:
            IO.output_error_message("Invalid file", e)
            print("Creating a valid file...")
            with open(FILE_NAME, 'w') as file:
                json.dump(file, students)
        except Exception as e:
            IO.output_error_message("unhandled exception", e)
        return students
# writing to the json file
    @staticmethod
    def add_data_to_file(FILE_NAME , students) -> None:
        """
        writing data to the json file
        :param FILE_NAME
        :param students
        """
        try:
            student_first_name = input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only alphabets")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only alphabets")
            course_name = input("Enter course name: ")
            student_data = {"first_name" : student_first_name, "last_name" : student_last_name, "course_name" : course_name}
            students.append(student_data)
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
        except ValueError as e:
            IO.output_error_message("User entered invalid name")
        except Exception as e:
            IO.output_error_message("There was an error writing to the file", e)
        return students

    @staticmethod
    def write_data_to_file(FILE_NAME, students):
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
                for student in students:
                    print(f"You have registered {student['first_name']} {student['last_name']} for {student['course_name']}")
            return True
        except Exception as e:
            IO.output_error_message("There was an error writing to the file", e)
        except ValueError as e:
            IO.output_error_message("Unhandled excetion ",e)
        return False






class IO:
    global students

    @staticmethod
    def output_error_message(message, error: Exception = None) -> None:
        print(message)
        if Exception is not None:
            print("__Technical Information__")
            print(error, error.__doc__)

    def input_menu_choice(MENU):
        print(MENU)
        str_choice = input("what would you like to do:")
        return str_choice
        while str_choice not in ["1", "2", "3", "4"]:
            print("Please enter the choice between 1 and 4")
            str_choice = input(MENU)
        return str_choice

    @staticmethod
    def get_input(message):
        return input(message)

    @staticmethod
    def input_student_data(students):
        try:
            student_first_name = IO.get_input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only alphabets")
            student_last_name = IO.get_input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only alphabets")
            course_name = IO.get_input("Enter course name: ")
            student_data = {"first_name" : student_first_name, "last_name" : student_last_name, "course_name" : course_name}
            students.append(student_data)
        except ValueError as e:
            IO.output_error_message("User entered invalid name")
        finally:
            return students

    @staticmethod
    def output_student_courses(students):
        try:
            for student in students:
                print(f"{student['first_name']} {student['last_name']} registered for {student['course_name']}")
        except Exception as e:
            IO.output_error_message("unhandled exception",e)
        finally:
            return students

students = FileProcessor.read_data_from_file(FILE_NAME, students)
while True:
    choice = IO.input_menu_choice(MENU)
    # getting input from user
    if choice == "1":
        students = IO.input_student_data(students)

    # displaying student information
    elif choice == "2":
        IO.output_student_courses(students)

    # writing data to the file
    elif choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)

    # exit the program
    elif choice == "4":
        sys.exit()

    else:
        print("user entered invalid choice")








print(students)
