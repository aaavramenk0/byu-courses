import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

def main():
    names_list = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303' ]
    radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
    height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    for i in range(0, 12):
        volume = compute_volume(radius_list[i], height_list[i])
        surf_area = compute_surface_area(radius_list[i], height_list[i])
        storage_efficiency = volume / surf_area
        print(f"{names_list[i]} {storage_efficiency:.1f}")
main()