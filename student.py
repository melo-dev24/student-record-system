from db import get_connection


class Student:
    def __init__(self):
        """Initialize DB connection and cursor."""
        self.conn = get_connection()
        if self.conn is None:
            raise Exception("Failed to connect to database")
        self.cursor = self.conn.cursor()

    def add(self, first_name, last_name, age, course):
        """Add a new student to the database."""
        if age <= 0:
            print("Age must be positive.")
            return

        sql = """
        INSERT INTO students (first_name, last_name, age, course)
        VALUES (%s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (first_name, last_name, age, course))
            self.conn.commit()
            print(f"Student {first_name} {last_name} added!")
        except Exception as e:
            print(f"Error adding student: {e}")

    def view_all(self):
        """Display all students."""
        try:
            self.cursor.execute("SELECT * FROM students")
            rows = self.cursor.fetchall()

            if not rows:
                print("No students found.")
                return

            # Define column widths
            # ID, First, Last, Age, Course, Created At
            widths = [4, 12, 12, 5, 10, 20]

            # Print header
            headers = ["ID", "First Name", "Last Name",
                       "Age", "Course", "Created At"]
            header_row = " | ".join(
                f"{h:<{w}}" for h, w in zip(headers, widths))
            print(header_row)
            print("-" * len(header_row))

            # Print rows
            for row in rows:
                id_, fn, ln, age, course, created = row
                print(
                    f"{id_:<{widths[0]}} | "
                    f"{fn:<{widths[1]}} | "
                    f"{ln:<{widths[2]}} | "
                    f"{age:<{widths[3]}} | "
                    f"{course:<{widths[4]}} | "
                    f"{str(created):<{widths[5]}}"
                )

        except Exception as e:
            print(f"Error fetching students: {e}")

    def update(self,
               student_id,
               first_name=None,
               last_name=None,
               age=None,
               course=None
               ):
        """Update an existing student by ID."""
        if age is not None and age <= 0:
            print("Age must be positive.")
            return

        updates = []
        values = []

        if first_name is not None:
            updates.append("first_name=%s")
            values.append(first_name)

        if last_name is not None:
            updates.append("last_name=%s")
            values.append(last_name)

        if age is not None:
            updates.append("age=%s")
            values.append(age)

        if course is not None:
            updates.append("course=%s")
            values.append(course)

        if not updates:
            print("Nothing to update.")
            return

        sql = f"UPDATE students SET {', '.join(updates)} WHERE id=%s"
        values.append(student_id)

        try:
            self.cursor.execute(sql, values)
            if self.cursor.rowcount == 0:
                print("Student not found.")
            else:
                self.conn.commit()
                print(f"Student {student_id} updated!")
        except Exception as e:
            print(f"Error updating student: {e}")

    def delete(self, student_id):
        """Delete a student by ID."""
        try:
            self.cursor.execute(
                "DELETE FROM students WHERE id=%s", (student_id,))
            if self.cursor.rowcount == 0:
                print("Student not found.")
            else:
                self.conn.commit()
                print(f"Student {student_id} deleted!")
        except Exception as e:
            print(f"Error deleting student: {e}")

    def close(self):
        """Close cursor and connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
