from vallidation import get_user_input
from bmi import calculate_bmi, get_bmi_category

def display_result(weight, height, bmi, category):
    """Display the BMI results."""
    print("\n===== Result =====")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"Your BMI is: {round(bmi, 2)}")
    print(f"Category: {category}")

def main():
    print("===== BMI Calculator =====")

    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    display_result(weight, height, bmi, category)

if __name__ == "__main__":
    main()