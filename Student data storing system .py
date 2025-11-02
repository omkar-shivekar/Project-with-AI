# Student Data Storing System

import csv

limit = int(input("How many students do you want to enter? "))
students = []

for i in range(limit):
    print(f"\nstudent {i + 1}")
    name = input("Enter student name: ")
    roll = i + 1  # roll number added automatically
    students.append([name, roll])

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Roll Number"])
    writer.writerows(students)

print("\nAll data saved to 'students.csv' successfully!")

# Student Search System

search_roll = int(input("\nEnter roll number to search: "))
found = False

for s in students:
    if s[1] == search_roll:
        print("\n✅ Student found!")
        print("Name:", s[0])
        print("Roll No:", s[1])
        found = True
        break

if not found:
    print("❌ No student found with that rollnumber.")
