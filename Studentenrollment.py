# Student Course Enrollment, Attendance and Grade System

students = {}
courses = {}

# Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    
    students[sid] = {
        "name": name,
        "courses": {}
    }
    print("Student added successfully!\n")


# Add Course
def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    
    courses[cid] = cname
    print("Course added successfully!\n")


# Enroll in Course
def enroll_student():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    
    if sid in students and cid in courses:
        students[sid]["courses"][cid] = {
            "attendance": 0,
            "grade": None
        }
        print("Student enrolled successfully!\n")
    else:
        print("Invalid Student ID or Course ID!\n")


# Mark Attendance
def mark_attendance():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    
    if sid in students and cid in students[sid]["courses"]:
        students[sid]["courses"][cid]["attendance"] += 1
        print("Attendance marked!\n")
    else:
        print("Student not enrolled in this course!\n")


# Assign Grade
def assign_grade():
    sid = input("Enter Student ID: ")
    cid = input("Enter Course ID: ")
    
    if sid in students and cid in students[sid]["courses"]:
        grade = input("Enter Grade: ")
        students[sid]["courses"][cid]["grade"] = grade
        print("Grade assigned!\n")
    else:
        print("Student not enrolled in this course!\n")


# View Student Report
def student_report():
    sid = input("Enter Student ID: ")
    
    if sid in students:
        print("\nStudent Name:", students[sid]["name"])
        print("Courses:")
        for cid, data in students[sid]["courses"].items():
            print("Course:", courses[cid])
            print("Attendance:", data["attendance"])
            print("Grade:", data["grade"])
            print("-------------")
    else:
        print("Student not found!\n")


# Course-wise Report
def course_report():
    cid = input("Enter Course ID: ")
    
    if cid in courses:
        print("\nCourse Name:", courses[cid])
        print("Enrolled Students:")
        
        for sid, sdata in students.items():
            if cid in sdata["courses"]:
                print("Student:", sdata["name"])
                print("Attendance:", sdata["courses"][cid]["attendance"])
                print("Grade:", sdata["courses"][cid]["grade"])
                print("-------------")
    else:
        print("Course not found!\n")


# Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Mark Attendance")
    print("5. Assign Grade")
    print("6. View Student Report")
    print("7. Course-wise Report")
    print("8. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        mark_attendance()
    elif choice == "5":
        assign_grade()
    elif choice == "6":
        student_report()
    elif choice == "7":
        course_report()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")
