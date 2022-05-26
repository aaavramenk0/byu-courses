import math
from datetime import datetime

current_date_and_time = datetime.now()

def tire_volume(w, a, d):
    space_volume = (math.pi * w**2 * a * (w * a + 2540 * d))/10000000000
    return space_volume
    

tire_width = int(input('Enter the width of the tire in mm (ex 198): '))
tire_aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 45): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 32): '))

print(f"The approximate volume is {tire_volume(tire_width, tire_aspect_ratio, wheel_diameter):.2f} liters")

buy_tires = input("Do you want to buy tires with the dimensions that you entered? (Y/N) ")
if buy_tires.lower() == 'y':
    name = input("Enter your first and last names: ")
    phone_number = input("Enter your phone number with the country code: ")

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_file:
    # Print the information to the file.
    print(f"{current_date_and_time:%H:%M:%S %d-%b-%Y}", file = volumes_file)
    print(f"Width: {tire_width}, aspect ratio: {tire_aspect_ratio}, wheel diameter: {wheel_diameter}, volume of the tire: {tire_volume(tire_width, tire_aspect_ratio, wheel_diameter):.2f}", file = volumes_file) 
    if buy_tires.lower() == 'y':
        print(f"Name: {name}, phone number: {phone_number}\n", file = volumes_file)