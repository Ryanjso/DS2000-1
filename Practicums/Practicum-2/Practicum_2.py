# DS2001
# Practicum 1
# Ryan Soderberg

import random

# Part 1 - Roll a 6-Sided Dice

dice_roll = random.randint(1, 6)

print(f"You rolled a {dice_roll}")

if dice_roll % 2 == 0:
    print("...which is even")
else:
    print("...which is odd")


# Part 2 - Playing Craps

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)

sum_of_dice = dice_roll_1 + dice_roll_2

print(f"You rolled a {dice_roll_1} and a {dice_roll_2}")

if sum_of_dice == 7 or sum_of_dice == 11:
    print("You win!")
elif sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12:
    print("You lose!")
else:
    print("It's a tie!")

# Part 3 - Average of 10 Rolls

number_of_rolls = 10
total_dice_sums = 0

for i in range(number_of_rolls):
    first_dice_roll = random.randint(1, 6)
    second_dice_roll = random.randint(1, 6)

    dice_sum = first_dice_roll + second_dice_roll

    print(f"You rolled a {first_dice_roll} and a {second_dice_roll}, sum is {dice_sum}")

    total_dice_sums += dice_sum

average_of_sums = total_dice_sums / number_of_rolls

print(f"Average of your numbers is {average_of_sums}")

# Part 4 - Casino Solution

roll_count = 100
num_wins = 0
num_ties = 0
num_losses = 0

for i in range(roll_count):
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)
    roll_sum = roll_one + roll_two

    if roll_sum == 7 or roll_sum == 11:
        num_wins += 1
    elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
        num_losses += 1
    else:
        num_ties += 1

print(f"You got {num_wins} wins, {num_losses} losses, and {num_ties} ties!")

# Part 5 - Average and Minimum of Even Numbers

num_rolls = 10

num_of_even_sums = 0
sum_of_evens = 0
lowest_roll = 13

for i in range(num_rolls):
    roll_number_one = random.randint(1, 6)
    roll_number_two = random.randint(1, 6)

    sum_of_rolls = roll_number_one + roll_number_two

    print(
        f"You rolled a {roll_number_one} and a {roll_number_two}, sum is {sum_of_rolls}"
    )

    # Add up evens
    if sum_of_rolls % 2 == 0:
        num_of_even_sums += 1
        sum_of_evens += sum_of_rolls

        # find lowest sum
        if sum_of_rolls < lowest_roll:
            lowest_roll = sum_of_rolls

avg_of_evens = sum_of_evens / num_of_even_sums

print(f"Average of your even numbers is {avg_of_evens}")

print(f"The minimum value we saw was {lowest_roll}")
