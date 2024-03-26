
#This code represents a loop that iterates a certain number of times based on user input.
#In each iteration, the code attempts to perform integer division by dividing two integers 'a' and 'b' entered by the user.
#If the division is successful, the result is printed. However, if an exception occurs during the division (such as a ValueError due to incorrect input format),
#an error message is printed along with the specific error code.

# Prompting the user to enter a number that determines the number of iterations for the loop
# The loop will run 'n' times, where 'n' is the number entered by the user
for i in range(int(input())):

    try:
        # Prompting the user to enter two integers separated by a space
        # The 'map' function is used to apply 'int' function to each element entered by the user
        a, b = map(int, input().split())

        # Attempting to perform integer division by dividing 'a' by 'b'
        # The result of the division is printed
        print(a // b)

    except Exception as e:
        # If an exception occurs during the division (e.g., ValueError),
        # an error message is printed along with the specific error code
        print("Error Code:", e)
