class Student:
    def __init__(self, name, roll_no, marks, attendance):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.attendance = attendance

    def calculate_grade(self):
        # Grade logic based on PDF criteria [cite: 502-509, 1000-1007]
        if self.marks >= 75: return "Distinction"
        elif self.marks >= 60: return "First Class"
        elif self.marks >= 50: return "Pass"
        else: return "Fail"

    def display(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name} | Roll: {self.roll_no} | Marks: {self.marks} | Attendance: {self.attendance}% | Grade: {grade}")

def save_record(student_obj):
    # File handling with Exception Handling [cite: 758-764, 1387]
    try:
        f = open("student_database.txt", "a")
        data = f"{student_obj.name},{student_obj.roll_no},{student_obj.marks},{student_obj.attendance}\n"
        f.write(data)
    except Exception as e:
        print("Error saving to file:", e)
    finally:
        f.close()

def main():
    student_list = []
    
    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add New Student")
        print("2. View All Records")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                # Input validation using Exception Handling [cite: 649-653, 996-999]
                name = input("Enter Name: ")
                roll = input("Enter Roll No: ")
                marks = int(input("Enter Marks (0-100): "))
                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100")
                
                attendance = int(input("Enter Attendance %: "))
                
                new_student = Student(name, roll, marks, attendance)
                student_list.append(new_student)
                save_record(new_student)
                print("Record saved successfully!")
                
            except ValueError as v:
                print("Invalid Input:", v)
        
        elif choice == "2":
            if not student_list:
                print("No records in current session.")
            else:
                for s in student_list:
                    s.display()
                    
        elif choice == "3":
            print("Closing system...")
            break
        else:
            print("Invalid Option.")

main()