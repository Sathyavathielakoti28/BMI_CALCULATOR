def calculate_bmi(weight, height):
    """Calculate and return BMI."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"