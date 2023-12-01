# Input a list of student scores
student_scores = input("Enter the numbers you intend to check\n ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

high_score = 0

for student_score in student_scores:
    if student_score > high_score:
        high_score = student_score
print(f"The highest score in the class is: {high_score}")