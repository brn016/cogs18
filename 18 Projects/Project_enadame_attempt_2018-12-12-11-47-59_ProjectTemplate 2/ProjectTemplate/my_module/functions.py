"""A collection of functions for doing my project."""
import csv


def add_new_student():
    """Adds new student and writes it to the corresponding 
    file.   
    """
 
    #user is prompted to input all the required fields
    print("Enter first name: ")
    firstName = input()
    
    print("Enter last name: ")
    lastName = input()
    
    print("Enter student ID number: ")
    studentId = input()
    
    print("Enter your major: ")
    major = input()
    
    print("Enter Assignment 1 (A1) score: ")
    A1 = input()
    
    print("Enter Assignment 2 (A2) score: ")
    A2 = input()
    
    print("Enter Assignment 3 (A3) score: ")
    A3 = input()
    
    print("Enter Assignment 4 (A4) score: ")
    A4 = input() 
    
    #opens Student file and writes new record
    with open('studentfile.py','a') as studentfile:
        studentfileWriter = csv.writer(studentfile)
        studentfileWriter.writerow([firstName, lastName, studentId, major, A1, A2, A3, A4])
        print("Record has been written to file")
        studentfile.close()
        menu()
        
        
def student_details():
    """Displays the record of students in our external file. 
    
    """
    # Open our file and read it
    f=open("studentfile.py","r", encoding = "utf8")
    
    #Create a list called "displaylist" into which all the files lines are read in to.
    displayList = f.read()
    
    # Print the list (that now has the file details in it)
    print(displayList)
    f.close()
    menu()
    
    
def calculate_grades():
    """Adds the number of assignments together.
    
    Takes the input from the user and assigns the grade
    to each variable. 
    
    print(A1 + A2 + A3 + A4)
    ------------------------
    
    returns the resuls of the addition
    """
    
    #prompts student to enter 4 different scores
    print("Enter your 4 assigment scores: ")
    A1 = int(input("Enter A1 grade: "))
    A2 = int(input("Enter A2 grade: "))
    A3 = int(input("Enter A3 grade: "))
    A4 = int(input("Enter A4 grade: "))  
    
    # Adds the four scores together 
    print("\nYour total assignment grade is: ")
    print(A1 + A2 + A3 + A4)
    print()
    menu()