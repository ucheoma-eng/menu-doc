   def __str__(self):
        return f"{self.student_number} | {self.first_name} {self.last_name} | {self.date_of_birth.strftime('%Y-%m-%d')} | {self.sex} | {self.country_of_birth} | Age: {self.calculate_age()}"

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) < 100:
            self.students.append(student)
        else:
            print("Student database is full.")

    def find_student_by_number(self, student_number):
        for student in self.students:
            if student.get_student_number() == student_number:
                return student
        return None

    def remove_student(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            self.students.remove(student)
            print(f"Student {student_number} has been removed.")
        else:
            print(f"Student with number {student_number} not found.")

    def modify_student(self, student_number):
        student = self.find_student_by_number(student_number)
        if student:
            print("Select field to modify:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth")
            print("4. Sex")
            print("5. Country of Birth")
            choice = int(input("Enter your choice: "))
            new_value = input("Enter new value: ")
            if choice == 1:
                student.set_first_name(new_value)
            elif choice == 2:
                student.set_last_name(new_value)
            elif choice == 3:
                student.set_date_of_birth(new_value)
            elif choice == 4:
                student.set_sex(new_value)
            elif choice == 5:
                student.set_country_of_birth(new_value)
            print("Student record modified.")
        else:
            print(f"Student with number {student_number} not found.")

    def show_all_students(self):
        if not self.students:
            print("No students in the database.")
        for student in self.students:
            print(student)

    def show_students_born_in_year(self, year):
        found = False
        for student in self.students:
            if student.get_date_of_birth().year == year:
                print(student)
                found = True
        if not found:
            print(f"No students born in the year {year}.")

    def write_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)
            print(f"Student data saved to {filename}.")

    def read_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.students = pickle.load(file)
                print(f"Student data loaded from {filename}.")
        except FileNotFoundError:
            print("File not found. No data loaded.")

def menu():
    db = StudentDatabase()
    while True:
        print("\nStudent Database Menu")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Add a new student")
        print("4. Find student by number")
        print("5. Show all students")
        print("6. Show students born in a specific year")
        print("7. Modify student record")
        print("8. Delete a student")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            filename = input("Enter filename to save to: ")
            db.write_to_file(filename)
        elif choice == 2:
            filename = input("Enter filename to load from: ")
            db.read_from_file(filename)
        elif choice == 3:
            student_number = input("Enter student number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            sex = input("Enter sex: ")
            country_of_birth = input("Enter country of birth: ")
            student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
            db.add_student(student)
        elif choice == 4:
            student_number = input("Enter student number to find: ")
            student = db.find_student_by_number(student_number)
            if student:
                print(student)
            else:
                print(f"Student with number {student_number} not found.")
        elif choice == 5:
            db.show_all_students()
        elif choice == 6:
            year = int(input("Enter the year: "))
            db.show_students_born_in_year(year)
        elif choice == 7:
            student_number = input("Enter student number to modify: ")
            db.modify_student(student_number)
        elif choice == 8:
            student_number = input("Enter student number to delete: ")
            db.remove_student(student_number)
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()