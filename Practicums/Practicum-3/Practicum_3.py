# DS2001
# Practicum 3
# Ryan Soderberg

# Part 0 - Get the Data

FORECLOSURES = [
    11,
    10,
    6,
    8,
    4,
    13,
    11,
    8,
    6,
    10,
    3,
    4,
    10,
    10,
    6,
    2,
    6,
    8,
    10,
    11,
    14,
    6,
    10,
    6,
]
PETITIONS = [
    44,
    50,
    6,
    14,
    12,
    14,
    14,
    19,
    11,
    19,
    15,
    15,
    13,
    10,
    20,
    32,
    31,
    16,
    41,
    34,
    33,
    37,
    36,
    40,
]


# Part 1 - Sum of list


def my_sum(num_list):
    total = 0
    for num in num_list:
        total += num

    return total


# Part 2 - Maximum of a list


def my_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num

    return max_num


# Part 3 - Percent Change


def foreclosure_change(month_one_val, month_two_val):
    return month_two_val / month_one_val * 100


def main():
    # Call function for part one
    num_forclosures = my_sum(FORECLOSURES)
    num_petitions = my_sum(PETITIONS)
    print(
        "Over the entire dataset, we recorded",
        num_forclosures,
        "foreclosures and",
        num_petitions,
        "petitions",
    )

    # Call function for part 2
    max_foreclosures = my_max(FORECLOSURES)
    max_petitions = my_max(PETITIONS)
    print(
        "Max # of foreclosures:",
        max_foreclosures,
        "\n",
        "Max # of petitions:",
        max_petitions,
    )

    # Call functions for part 3
    start = int(input("Which month to start?\n"))
    end = int(input("Which month to end?\n"))

    # Validate that end is greater than start
    while end <= start:
        end = int(input(f"Please provide an end > {start}: "))

    foreclosure_pct = foreclosure_change(FORECLOSURES[start], FORECLOSURES[end])
    print("Change between those two months was...", foreclosure_pct, "\n")


main()
