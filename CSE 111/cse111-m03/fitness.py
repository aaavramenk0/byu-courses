# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
from xml.etree.ElementInclude import include


def main():
    # Get the user's gender, birthdate, height, and weight.

    gender = input("Enter your gender (M or F): ")
    birthdate = input("Enter a birthdate in this format: YYYY-MM-DD: ")
    pounds = int(input("Enter a weight in U.S. pounds: "))
    inches = int(input("Enter a height in U.S. inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    print(f"Age (years): {compute_age(birthdate)}\nWeight (kg): {kg_from_lb(pounds):.1f}\nHeight (cm): {cm_from_in(inches):.1f}\nHeight (m): {m_from_cm(inches):.1f}\nBody mass index: {body_mass_index(kg_from_lb(pounds), cm_from_in(inches)):.1f}\nBasal metabolic rate (kcal/day): {basal_metabolic_rate(gender, kg_from_lb(pounds), cm_from_in(inches), compute_age(birthdate)):.1f}")
    pass


def compute_age(birthdate):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight = pounds * 0.45359237
    return weight


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * 2.54
    return height


def m_from_cm(inches):
    cm = inches * 2.54
    meters = cm / 100
    return meters


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * weight / (height ** 2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.lower() == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
