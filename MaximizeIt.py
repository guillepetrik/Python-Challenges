# Maximize It!

from itertools import product

# Read the values of k and m from input
k, m = list(map(int, input().split()))

# Read the lines and create a list of integer values
lines = []
for i in range(k):
    lines.append(list(map(int, input().split()))[1:])

# Generate the Cartesian product of the integer values in lines
res_list = list(product(*lines))

# Calculate the result for each tuple in the Cartesian product
result = []
for tup in res_list:
    tot = 0
    for item in tup:
        tot += item ** 2
    result.append(tot % m)

# Print the maximum result
print(max(result))
