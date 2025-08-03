import random
import string
import sys

# Password Generation Function
def generate_advanced_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = []
    if use_upper: chars.extend(string.ascii_uppercase)
    if use_lower: chars.extend(string.ascii_lowercase)
    if use_digits: chars.extend(string.digits)
    if use_symbols: chars.extend(string.punctuation)

    if not chars:
        raise ValueError("At least one character type must be selected")

    password = []
    if use_upper: password.append(random.SystemRandom().choice(string.ascii_uppercase))
    if use_lower: password.append(random.SystemRandom().choice(string.ascii_lowercase))
    if use_digits: password.append(random.SystemRandom().choice(string.digits))
    if use_symbols: password.append(random.SystemRandom().choice(string.punctuation))

    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.SystemRandom().choice(chars) for _ in range(remaining_length))
    
    random.SystemRandom().shuffle(password)
    return ''.join(password)

# User Input Handling
def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ('y', 'n', ''):
            return response != 'n'
        print("Please enter 'y' or 'n': ")

# Main Program Execution
def main():
    print("\nGenerate advanced password: ")
    print("--------------------------------")
    try:
        length = int(input("Password length (default 12): ") or 12)
        if length < 8:
            print("Password length must be at least 8 characters")
            sys.exit(1)

        print("\nSelect character types (press Enter for Yes, 'n' for No):")
        use_upper = get_yes_no_input("Include uppercase letters (A-Z)? [Y/n]: ")
        use_lower = get_yes_no_input("Include lowercase letters (a-z)? [Y/n]: ")
        use_digits = get_yes_no_input("Include digits (0-9)? [Y/n]: ")
        use_symbols = get_yes_no_input("Include symbols (!@#$)? [Y/n]: ")

        password = generate_advanced_password(
            length=length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols
        )

        print(f"\n✅ Generated Password: {password}")
        print(f"Password strength: {'Strong' if length >= 12 and (use_symbols or use_digits) else 'Medium' if length >= 8 else 'Weak'}")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
