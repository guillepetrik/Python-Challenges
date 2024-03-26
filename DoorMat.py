#Designer Door Mat Challenge

# Prompting the user to enter two integers separated by a space
# 'n' represents the total number of lines in the design, and 'm' represents the width of each line
n, m = map(int, input().split())

# Defining two strings used for the design
a = ".|."
b = "WELCOME"

# UPPER
# Looping through the first half of the lines in the design
for i in range(n // 2):
    # Printing a pattern with increasing repetitions of the string 'a'
    # The pattern is centered within a line of width 'm' and filled with '-'
    print((a * ((i * 2) + 1)).center(m, "-"))

# Printing the line with the string 'b' in the center, surrounded by '-'
print(b.center(m, "-"))

# LOWER
# Looping through the second half of the lines in the design in reverse order
for i in range(n // 2 - 1, -1, -1):
    # Printing a pattern with decreasing repetitions of the string 'a'
    # The pattern is centered within a line of width 'm' and filled with '-'
    print((a * ((i * 2) + 1)).center(m, "-"))
