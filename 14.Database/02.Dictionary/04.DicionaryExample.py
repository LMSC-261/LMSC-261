# Space for students
students = []
# Prompt for students' names and dorms
for i in range(3):
  name = input("name: ")
  dorm = input("dorm: ")
  students.append({"name": name, "dorm": dorm})
# Print students' names and dorms
for student in students:
  print(f"{student['name']} is in {student['dorm']}.")