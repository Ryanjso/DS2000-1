# DS2001
# Practicum 1
# Ryan Soderberg

# Part 1 - Stone to Pounds

dog_name = input("What is the name of your dog?\n")
dog_weight_stones = input("how much does %s weight, in stone?\n" % dog_name)

POUNDS_IN_STONE = 14
dog_weight_pounds = float(dog_weight_stones) * POUNDS_IN_STONE

rounded_final_weight = round(dog_weight_pounds, 2)

print("Ok, then %s weighs %f pounds" % (dog_name, rounded_final_weight))

# Part 2 - Eating Out With a Group

num_people = int(input("How many people are there?\n"))

SPACE_PER_PERSON = 36
space_needed = num_people * SPACE_PER_PERSON

bill_before_tip = float(input("What is the total bill?\n"))
tip_percent = float(input("What percent would everyone like to tip?\n"))

tot_bill = bill_before_tip * (1 + tip_percent)
bill_per_person = tot_bill / num_people

print("We need a total of %dsf for safe distancing." % space_needed)
print("Everyone cough up ${:.2f}".format(bill_per_person))


# Part 3 - Making Change

PRODUCT_COST = 2.37
dollar_input = int(input("How many dollars are you putting in?\n"))
change_due = dollar_input - PRODUCT_COST

print("Your change is ${:.2f}".format(change_due))
print("I'm giving you back:")

change_due_100 = change_due * 100

DOLLAR = 100
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

dollars_to_return = change_due_100 // DOLLAR

new_change_due_100 = change_due_100 - dollars_to_return * DOLLAR

quarters_to_return = new_change_due_100 // QUARTER

new_change_due_100 = new_change_due_100 - quarters_to_return * QUARTER

dimes_to_return = new_change_due_100 // DIME

new_change_due_100 = new_change_due_100 - dimes_to_return * DIME

nickels_to_return = new_change_due_100 // NICKEL

new_change_due_100 = new_change_due_100 - nickels_to_return * NICKEL

pennies_to_return = new_change_due_100 // PENNY

print("%d dollars" % int(dollars_to_return))
print("%d quarters" % int(quarters_to_return))
print("%d dimes" % int(dimes_to_return))
print("%d nickels" % int(nickels_to_return))
print("%d pennies" % int(pennies_to_return))

# Part 4 - Isolating Digits

num = int(input("Enter a non-negative integer\n"))

hundreds = num // 100

updated_num = num - hundreds * 100

tens = updated_num // 10

updated_num = updated_num - tens * 10

ones = updated_num // 1

print("hundreds = %d" % hundreds)
print("tens = %d" % tens)
print("ones = %d" % ones)
