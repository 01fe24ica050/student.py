from student import calculate_grade

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(80) == "B"

def test_grade_C():
    assert calculate_grade(60) == "C"

def test_grade_F():
    assert calculate_grade(30) == "F"



def main():
    name = "pallavi"
    department = "BCA"
    semester = 3
    marks = [75, 82, 68]

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Marks      : {marks}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
