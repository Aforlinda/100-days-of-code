# Input a Python list of student heights
student_heights = input("Enter the heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0 

number_of_students = 0 

for student_height in student_heights:
    sum += student_height
    number_of_students += 1
ave_height = round(sum / number_of_students)

print(f"total height = {sum}")
print(f"number of students = {number_of_students}")
print(f"average height = {ave_height}")