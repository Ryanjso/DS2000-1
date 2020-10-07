# Ryan Soderberg
# DS2000-Sec02

price = int(input("Enter price in cents (1-100): "))

change = 100 - price

quarters = change // 25
dimes = change % 25 // 10
pennies = change % 25 % 10

print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Pennies: ", pennies)
