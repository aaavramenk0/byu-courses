import math

def tire_volume(w, a, d):
    space_volume = (math.pi * w**2 * a * (w * a + 2540 * d))/10000000000
    print(f"The approximate volume is {space_volume:.2f} liters")

tire_width = int(input('Enter the width of the tire in mm (ex 198): '))
tire_aspect_radio = int(input('Enter the aspect ratio of the tire (ex 45): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 32): '))

tire_volume(tire_width, tire_aspect_radio, wheel_diameter)