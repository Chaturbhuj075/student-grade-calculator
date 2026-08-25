print("=== Student Grade Calculator ===")

student_name = input("Enter the student's name: ")
print("Calculating grades for", student_name)


subjects = ["Hindi", "English", "Mathematics", "Science", "Computer"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total_marks = sum(marks)
percentage = total_marks / len(subjects)

print("\n=== Result ===")
print("Student:", student_name)
print("Total marks:", total_marks, "out of", len(subjects) * 100)
print("Percentage:", round(percentage, 2), "%")
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 33:
    grade = "E"
else:
    grade = "F"

if min(marks) < 33:
    result = "Fail"
    grade = "F"
else:
    result = "Pass"

print("Grade:", grade)
print("Result:", result)
