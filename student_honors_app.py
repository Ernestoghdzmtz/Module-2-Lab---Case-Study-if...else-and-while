# Author: Ernesto Hernández Martínez
# Filename: student_honors_app.py
# Description: This app accepts student names and GPAs 
# to determine if the student qualifies for the Dean's List or the Honor Roll.

def main():
    print("Enter 'ZZZ' as the last name to quit.")

    while True:
        # Get the student's last name
        last_name = input("Enter the student's last name: ")
        if last_name.upper() == 'ZZZ':
            print("Exiting the program.")
            break

        # Get the student's first name
        first_name = input("Enter the student's first name: ")

        # Get and validate the student's GPA
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
            continue

        # Check GPA for Dean's List and Honor Roll
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

# Run the app
if __name__ == "__main__":
    main()
