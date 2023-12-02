# target = int(input("Enter a number between 0 and 1000 ")) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇


# the_sum = 0

# for n in range(2, (target + 1), 2):
#     the_sum += n
# print(the_sum)

target = int(input("Enter a number between 0 and 1000 ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇


the_sum = 0

for n in range(2, (target + 1)):
    if n % 2 == 0:
        the_sum += n
print(the_sum)

