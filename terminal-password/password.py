import random
import string

def generate_password(length, use_numbers, use_uppercase, use_lowercase, use_symbols):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Generate a random password of specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main program loop
while True:
    print("\n--- Random Password Generator ---")
    print("1. Generate Password")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        # Get user input for password options
        while True:
            try:
                length = int(input("Enter the length of the password (between 8 and 16): "))
                if length < 8 or length > 16:
                    print("Please enter a length between 8 and 16.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_symbols = input("Include special symbols? (y/n): ").lower() == 'y'

        # Generate and print a random password
        print("Random Password:", generate_password(length, use_numbers, use_uppercase, use_lowercase, use_symbols))
    
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1 or 2.")
