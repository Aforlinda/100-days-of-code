line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Take a good look at the the grid provided. Use the grid to provide spot description of \
where you want hide your treasure. You can choose either A, B or C and 1, 2 or 3 for a spot. Where do you \
want to put the treasure? ") 
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower() 
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
