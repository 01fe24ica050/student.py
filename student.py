# Student Grade Calculator


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"


def main():
    # Accept student details
    name = "pallavi"
    department = "BCA"
    semester = 3

    marks = []
    sample_mark=[75,82,68]
    
    for i in range(len(sample_mark)):
        marks.append(sample_mark[i])
        
        avg = sum(marks) / len(marks)

    

    # Determine grade
    grade = calculate_grade(avg)

    # Display student details and grade
    print("\n--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Marks      : {marks}")
    print(f"Average    : {avg:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()