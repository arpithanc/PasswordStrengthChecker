
import string
import secrets


# Function to check password strength
def check_password(password):

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use 12 or more characters.")

    # Check uppercase letters
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Check lowercase letters
    if any(ch.islower() for ch in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Check numbers
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9).")

    # Check special characters
    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        suggestions.append("Add special characters (!, @, #).")

    # Check repeated characters
    if len(set(password)) == len(password):
        score += 1
    else:
        suggestions.append("Avoid excessive repeated characters.")

    # Check common passwords
    common_passwords = [
        "password",
        "12345678",
        "qwerty123",
        "admin123",
        "password123"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    # Display password report
    print("\n------ PASSWORD REPORT ------")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MEDIUM")
    elif score <= 6:
        print("Strength: STRONG")
    else:
        print("Strength: VERY STRONG")

    print("Score:", score, "/ 7")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Excellent! Your password meets all these checks.")


# Function to generate a strong password
def generate_password():

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        secrets.choice(characters) for _ in range(16)
    )

    return password


# Main program
print("====================================")
print("      PASSWORD STRENGTH CHECKER")
print("====================================")

while True:

    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        password = input("Enter a sample password: ")

        if password:
            check_password(password)
        else:
            print("Password cannot be empty.")

    elif choice == "2":

        new_password = generate_password()

        print("\nGenerated Password:", new_password)

    elif choice == "3":

        print("\nThank you for using Password Checker!")
        break

    else:
        print("\nInvalid choice. Please try again.")

