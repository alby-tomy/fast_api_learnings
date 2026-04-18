'''
Create a variable (grade) holding an integer between 0 and 100
Code if, elif, else statement to print the letter grade based on the following criteria:
Grade A: 90-100
Grade B: 80-89
Grade C: 70-79
Grade D: 60-69
Grade F: 0-59
'''

grade = 85
if grade >= 90 and grade <= 100:
    print("Grade A")
elif grade >= 80 and grade < 90:
    print("Grade B")
elif grade >= 70 and grade < 80:
    print("Grade C")
elif grade >= 60 and grade < 70:
    print("Grade D")
else:
    print("Grade F")
    