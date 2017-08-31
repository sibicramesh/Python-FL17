# Program to find numbers divisible by 5 and multiple of 2

# Result array declare
res = []

# Loop over the range to find numbers which are divisible by 5 and multiple of 2
for dm in range(700, 1700):
    if (dm % 2 == 0) and (dm % 5 == 0):
        res.append(str(dm))

# Print the result
print(res)
