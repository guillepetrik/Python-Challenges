#Alphabet Rangoli Challenge

def print_rangoli(size):
    n = size  # Assign the size of the rangoli pattern
    l1 = list(map(chr, range(97, 123)))  # Create a list of lowercase letters from 'a' to 'z'
    x = l1[n-1::-1]+l1[1:n]  # Construct the string for the rangoli pattern
    m = len("-".join(x))  # Calculate the length of the line for centering

    # Print the upper half of the rangoli pattern
    for i in range(1, n):
        print("-".join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m, "-"))

    # Print the lower half of the rangoli pattern
    for i in range(n, 0, -1):
        print("-".join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m, "-"))
