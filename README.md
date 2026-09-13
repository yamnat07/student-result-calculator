# Student Marks Management System

A simple command-line program built in Python using basic programming concepts — loops, conditionals, and input validation. It takes a student's details and marks in five subjects, then calculates their total, percentage, and grade.

## Features

- Menu-driven interface (enter marks / exit)
- Input validation for roll number and marks (must be within valid ranges)
- Calculates:
  - Total marks (out of 500)
  - Percentage
  - Grade (A+ to F) based on percentage and a minimum passing mark per subject
- Displays a pass/fail result based on subject-wise minimum marks (33) and overall percentage

## Subjects Covered

- Science
- Social Science
- Mathematics
- English
- Language

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python marking-system.py
```

Follow the on-screen prompts to enter student details and marks.

## Sample Output

```
================================
----STUDENT MARKS MANAGEMENT----
================================
1.Enter Marks and Details.

2.Exit.

Enter your choice: 1
Enter Student`s name: Rahul
Enter Student`s class: 10
Enter Student`s Exam Roll number: 21
Enter the marks of Science Subject: 85
Enter the marks of Social Science subject: 78
Enter the marks of Mathematics Subject: 92
Enter the marks of English Subject: 88
Enter the marks of Language Subject: 80

=============================
-------STUDENT RESULTS-------
=============================

Name of Student:  Rahul
Class of Student:  10
Student`s Roll number:  21
Total marks obtained:  423 out of 500
Percentage acquired:  84.6 %
Grade: A-
Congratulations,You have been promoted to next class!
```

## Grading Criteria

| Percentage | Grade |
|------------|-------|
| 90 and above | A+ |
| 80 - 89 | A- |
| 70 - 79 | A |
| 60 - 69 | B |
| 50 - 59 | C |
| 40 - 49 | D |
| 33 - 39 | E |
| Below 33 (or fails any subject) | F |

A student must score at least 33 marks in **every** subject to be considered for promotion, regardless of overall percentage.

## Known Limitations

This is an early/basic version of the project. Planned improvements include:

- Using a `for` loop to reduce repeated code across subjects
- Saving/exporting student results (e.g., to a file or list) instead of processing one student per run
- Better handling of invalid (non-numeric) input

## Concepts Used

`while` loops, `if`/`elif`/`else` conditionals, `input()`/`print()`, basic arithmetic, and type casting (`int()`).
