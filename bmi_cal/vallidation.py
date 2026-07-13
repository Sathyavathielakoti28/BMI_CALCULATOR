def get_user_input():

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))

            if weight <= 0:
                print("Weight must be greater than 0.")
                continue

            if height <= 0:
                print("Height must be greater than 0.")
                continue

            return weight, height

        except ValueError:
            print("Invalid input! Please enter numbers only.")