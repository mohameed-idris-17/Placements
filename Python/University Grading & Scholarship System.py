# Task: University Grading & Scholarship System
# Problem Statement:
# You are building a grading system for a university. The system should:

# Take student name, marks in 3 subjects, and attendance percentage as input.

# Calculate the average marks.

# Assign grades based on this logic:

# 90+ → Grade A+

# 80–89 → Grade A

# 70–79 → Grade B

# 60–69 → Grade C

# Below 60 → Grade F

# Scholarship rules (nested inside grade checks):

# If Grade is A+ and attendance ≥ 95% → "Full Scholarship"

# If Grade is A and attendance ≥ 90% → "Half Scholarship"

# Else → "No Scholarship"

# If any one subject score is below 40, the student fails regardless of average marks and no scholarship.

# Example:


# Input:
# Name: John Doe
# Marks: 95, 92, 88
# Attendance: 96

# Output:
# Student: John Doe
# Average Marks: 91.67
# Grade: A+
# Scholarship: Full Scholarship

name = input("Enter student's name")
mark1,mark2,mark3 = map(int,(input().split())
attendance = float(input())
print(f"student name is {name}")
average = mark1+mark2+mark3/3
print(f"average mark is {average:.2f}")
grade = "F"
if(average>=90):
    grade = "A+"
elif (average<=89) and (average>=80):
    grade = "A"
elif (average<=79) and (average>=70):
    grade = "B"
elif (average<=69) and (average>=60):
    grade = "c"
print(f"Grade: {grade}")
# scholarship
if(Grade=="A+") and (attendance>=95.00):
    print("Full Scholarship")
elif grade=="A" and attendance>=90.00:
    print("Half Scholarship")
else:
    print("No Scholarship")