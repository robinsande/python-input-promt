import sys

def get_user_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            converted_input = input_type(user_input)
            return converted_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def main():
    # Prompt the user to enter their birth year
    birth_year = get_user_input("Enter your birth year: ", int)

    # Calculate their age based on the entered birth year
    current_year = 2024  # You may update this with the current year
    age = current_year - birth_year

    # Ask the user to provide their height in meters
    height = get_user_input("Enter your height in meters: ", float)

    # Determine the data type of each input and display it
    print(f"\nData Types:\n- Birth Year: {type(birth_year)}\n- Age: {type(age)}\n- Height: {type(height)}")

    # Determine the size of each input and display it
    print(f"\nSize (in bytes):\n- Birth Year: {sys.getsizeof(birth_year)}\n- Age: {sys.getsizeof(age)}\n- Height: {sys.getsizeof(height)}")

if __name__ == "__main__":
    main()
