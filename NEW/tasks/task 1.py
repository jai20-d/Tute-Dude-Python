# personalized_greeting_enhanced.py

print("Enhanced Personalized Greeting Program")
print("--------------------------------------")


def get_name_input():
    """Get and validate name input from user"""
    while True:
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()

        if not first_name or not last_name:
            print("Both first and last names are required. Please try again.\n")
            continue

        if not first_name.isalpha() or not last_name.isalpha():
            print("Names should contain only letters. Please try again.\n")
            continue

        return first_name, last_name


def format_name(first, last, style='default'):
    """Format the name based on selected style"""
    if style == 'formal':
        return f"{last.upper()}, {first.title()}"
    elif style == 'title':
        return f"{first.title()} {last.title()}"
    else:  # default style
        return f"{first} {last}"


def select_greeting_style():
    """Let user select a greeting style"""
    print("\nSelect greeting style:")
    print("1. Casual (Hi [Name]!)")
    print("2. Formal (Dear [Name],)")
    print("3. Enthusiastic (HELLO [Name]! WELCOME!)")
    print("4. Custom")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def get_custom_greeting():
    """Get a custom greeting from the user"""
    return input("Enter your custom greeting (use {name} where the name should appear): ")


def main():
    # Get user's name
    first_name, last_name = get_name_input()

    # Select name format
    print("\nHow would you like your name formatted?")
    print("1. First Last (default)")
    print("2. LAST, First (formal)")
    print("3. First Last (title case)")

    format_choice = input("Enter choice (1-3, default is 1): ").strip()
    format_styles = {'1': 'default', '2': 'formal', '3': 'title'}
    format_style = format_styles.get(format_choice, 'default')

    # Create formatted full name
    full_name = format_name(first_name, last_name, format_style)

    # Select greeting style
    greeting_choice = select_greeting_style()

    # Generate appropriate greeting
    if greeting_choice == 1:
        greeting = f"Hi {full_name}! Great to see you!"
    elif greeting_choice == 2:
        greeting = f"Dear {full_name},\nWe are pleased to welcome you to our program."
    elif greeting_choice == 3:
        greeting = f"HELLO {full_name.upper()}! A WARM WELCOME TO YOU!"
    else:  # custom greeting
        custom_template = get_custom_greeting()
        greeting = custom_template.format(name=full_name)

    # Display the greeting
    print("\n" + "=" * 50)
    print(greeting)
    print("=" * 50)


if __name__ == "__main__":
    main()