student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num_students = 0
total_heights = 0
for height in student_heights:
  total_heights += height
  num_students += 1

print(round(total_heights/num_students))

