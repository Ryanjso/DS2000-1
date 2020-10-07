# Ryan Soderberg
# DS2000-Sec02

digit_sequence = input("Enter digit sequence: ")

# Count the occurance of each digit
digit_occurances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in digit_sequence:
    digit_occurances[int(num)] += 1


# Create a new sequence of ordered digits
new_sequence = ""

for i in range(len(digit_occurances)):
    new_sequence += str(i) * digit_occurances[i]


print(new_sequence)