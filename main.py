from student import Student


def main():
    student_system = Student()

    while True:
        print("\n=== Student Record System (MySQL) ===")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_system.view_all()

        elif choice == "2":

            fn = input("First name: ").strip()
            ln = input("Last name: ").strip()

            if not fn or not ln:
                print("First and last name cannot be empty.")
                continue

            try:
                age = int(input("Age: "))
                if age <= 0:
                    print("Age must be positive.")
                    continue
            except ValueError:
                print("Invalid age. Must be a number.")
                continue

            course = input("Course: ").strip()
            if not course:
                print("Course cannot be empty.")
                continue

            student_system.add(fn, ln, age, course)

        elif choice == "3":

            try:
                sid = int(input("Student ID to update: "))
            except ValueError:
                print("Invalid ID. Must be a number.")
                continue

            fn = input("New first name (leave blank to skip): ").strip()
            ln = input("New last name (leave blank to skip): ").strip()

            age_input = input("New age (leave blank to skip): ").strip()
            if age_input:
                try:
                    age = int(age_input)
                    if age <= 0:
                        print("Age must be positive.")
                        continue
                except ValueError:
                    print("Invalid age. Must be a number.")
                    continue
            else:
                age = None

            course = input("New course (leave blank to skip): ").strip()

            student_system.update(
                sid,
                fn or None,
                ln or None,
                age,
                course or None
            )

        elif choice == "4":

            try:
                sid = int(input("Student ID to delete: "))
            except ValueError:
                print("Invalid ID. Must be a number.")
                continue

            student_system.delete(sid)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
