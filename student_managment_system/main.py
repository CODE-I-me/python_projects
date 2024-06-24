from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from tabulate import tabulate
from models import Base, Student

DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/db_testing"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def add_student(session, roll_no, name, class_name, subjects, gender, dob, mobile_no, address):
    dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
    new_student = Student(roll_no=roll_no, name=name, class_name=class_name, subjects=subjects, gender=gender, dob=dob_date, mobile_no=mobile_no, address=address)
    session.add(new_student)
    session.commit()
    print(f"Student {name} added successfully.")

def remove_student(session, roll_no):
    student = session.query(Student).filter(Student.roll_no == roll_no).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {roll_no} removed successfully.")
    else:
        print(f"Student {roll_no} not found.")

def update_student(session, roll_no, **kwargs):
    student = session.query(Student).filter(Student.roll_no == roll_no).first()
    if student:
        for key, value in kwargs.items():
            if hasattr(student, key):
                if key == 'dob':
                    value = datetime.datetime.strptime(value, '%Y-%m-%d').date()
                setattr(student, key, value)
        session.commit()
        print(f"Student {roll_no} updated successfully.")
    else:
        print(f"Student {roll_no} not found.")

def display_students(session):
    students = session.query(Student).all()
    if students:
        table = [[student.roll_no, student.name, student.class_name, student.subjects, student.gender, student.dob, student.mobile_no, student.address] for student in students]
        print(tabulate(table, headers=["Roll No", "Name", "Class", "Subjects", "Gender", "DOB", "Mobile No", "Address"], tablefmt="pretty"))
    else:
        print("No Students Found.")

def search_student(session, search_term):
    students = session.query(Student).filter((Student.name.ilike(f'%{search_term}%')) | (Student.roll_no == search_term)).all()
    if students:
        table = [[student.roll_no, student.name, student.class_name, student.subjects, student.gender, student.dob, student.mobile_no, student.address] for student in students]
        print(tabulate(table, headers=["Roll No", "Name", "Class", "Subjects", "Gender", "DOB", "Mobile No", "Address"], tablefmt="pretty"))
    else:
        print("No Students Found.")

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def exit_program():
    print("Exiting Program.")
    exit()

def main():
    session = SessionLocal()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Display Students")
        print("5. Exit Program")
        print("6. Search Student")
        choice = input("Enter your choice: ")
        if choice == "1":
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            class_name = input("Enter Class: ")
            subjects = input("Enter Subjects (comma-separated): ")
            gender = input("Enter Gender: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            if not validate_date(dob):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            mobile_no = input("Enter Mobile No: ")
            address = input("Enter Address: ")
            add_student(session, roll_no, name, class_name, subjects, gender, dob, mobile_no, address)
        elif choice == "2":
            roll_no = int(input("Enter Roll No to remove: "))
            remove_student(session, roll_no)
        elif choice == "3":
            roll_no = int(input("Enter Roll No to update: "))
            fields = ['name', 'class_name', 'subjects', 'gender', 'dob', 'mobile_no', 'address']
            kwargs = {}
            for field in fields:
                value = input(f"Enter new {field} (or press Enter to skip): ")
                if value:
                    if field == 'dob' and not validate_date(value):
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        continue
                    kwargs[field] = value
            update_student(session, roll_no, **kwargs)
        elif choice == "4":
            display_students(session)
        elif choice == "5":
            exit_program()
        elif choice == "6":
            search_term = input("Enter name or roll number to search: ")
            search_student(session, search_term)
        else:
            print("Invalid Choice. Please try again")

if __name__ == "__main__":
    main()