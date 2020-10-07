# Ryan Soderberg
# DS2000-Sec02

int_list = input("Enter a sorted list of integers each in the range (0-99): ").split(
    " "
)

# Convert list of strings to list of integers
int_list = [int(i) for i in int_list]


# Calculate mean
sum = 0
for i in int_list:
    sum += i

mean = sum / len(int_list)


# Calculate median
if len(int_list) % 2 != 0:  # Odd length
    median_index = len(int_list) // 2
    median = int_list[median_index]
else:  # Even length
    median_index = int(len(int_list) / 2)
    median_index_two = median_index - 1

    median = (int_list[median_index] + int_list[median_index_two]) / 2


# Calculate mode
# Find number of occurances of each int
counter = [0] * 100
for num in int_list:
    counter[num] += 1

# Find possible modes - the number(s) that occur the most
min_count = 0
possible_modes = []
for i in range(len(counter)):
    if counter[i] > min_count:
        min_count = counter[i]
        possible_modes = [i]
    elif counter[i] == min_count:
        possible_modes += [i]

# Find lowest int in possible_modes
lowest = possible_modes[0]
for num in possible_modes:
    if num < lowest:
        lowest = num

mode = lowest

print("Values: ", len(int_list))
print("Mean: ", round(mean, 1))
print("Median: ", median)
print("Mode: ", mode)
