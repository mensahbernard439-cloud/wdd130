
# Enhancement: Added an option for the customer to buy the tires
# and save their phone number in the volumes.txt file.

import math

print()
print ("Write a programme that ask user's to describe a tire then calculate and display the tire's volume")
print()

width =float(input("Enter the width of the tire in mm: "))
a_ratio =float(input("Enter the aspect ratio of the tire: "))
diameter =float(input("Enter the diameter of the wheel in inches: "))

#formular
volume = math.pi * width**2 * a_ratio*(width * a_ratio + 2540 * diameter) / 10_000_000_000

volume = round(volume, 2)
print(f"The approximate volume is: {volume:.2f} liters")


from datetime import date

# 1. Get today's date
today = date.today()

# 2. Calculate volume
volume = math.pi * width**2 * a_ratio * (width * a_ratio + 2540 * diameter) / 10_000_000_000

# 3. Round volume
volume = round(volume, 2)

# 4. Open and append to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(f"{today},{width},{a_ratio},{diameter},{volume}\n")

# Enhancement: Ask the customer if they want to buy the tires and,
# if yes, save their phone number in volumes.txt.

buy = input("Do you want to buy these tires? ")

if buy.lower() == "yes":
    phone = input("Enter your phone number: ")

    with open("volumes.txt", "a") as file:
        file.write(f"{today},{width},{a_ratio},{diameter},{volume},{phone}\n")
