import csv
students = [
  ["Name", "RollNo", "Marks1", "Marks2"],
  ["A", 1, 100, 100],
  ["B", 2, 90, 90],
  ["C", 3, 80, 80]
]
with open("students.csv", "w") as f:
  writer = csv.writer(f)
  for student in students:
    writer.writerow(student)
with open("students.csv", "r") as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
