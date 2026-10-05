from students.model import  Student

def main():
    # Create a new student instance
    student = Student(
        student_id=1, 
        name="John Doe",
        email="john@example.com", 
        course="BSc Information Technology", 
        year=1
         )
    print("+++ STUDENT DETAILS +++")
    print(f"Student ID: {student.student_id:03d}")
    print(f"Name: {student.name}")
    print(f"Email: {student.email}")
    print(f"Course: {student.course}")

    years = {
        1: "First Year",
        2: "Second Year",
        3: "Third Year",
        4: "Fourth Year"
    }
    print(f"year: {years[student.year]}")

    
if __name__ == "__main__":
          main()





