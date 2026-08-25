# Student Grade Calculator

A beginner-friendly Python command-line program that calculates a student's total marks, percentage, grade, and pass/fail result.

## Features

- Accepts marks for five subjects
- Validates marks between 0 and 100
- Rejects non-numeric input
- Calculates total marks and percentage
- Assigns a grade based on percentage
- Marks the student as failed if any subject is below 33
- Saves multiple student results locally in `student_results.csv`
- Keeps previous results by adding each new student as a separate row

## Requirements

- Python 3.10 or newer

## How to Run

```bash
python grade_calculator.py
```

## Grade Scale

| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 33–49.99 | E |
| Below 33 | F |

A student must score at least 33 in every subject to pass.

## Author

Created by [Chaturbhuj075](https://github.com/Chaturbhuj075) as a beginner Python project.
