def calculate_grade(marks):
    if marks >= 90:
        return "S"
    elif marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


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
