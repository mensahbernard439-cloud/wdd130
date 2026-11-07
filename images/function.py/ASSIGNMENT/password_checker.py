import random
import string
import re

def check_length(password, min_length=8):
    """Checks if the password meets the minimum length requirement."""
    return len(password) >= min_length

def check_character_sets(password):
    """Counts how many distinct character types (lowercase, uppercase, digits, symbols) are present."""
    score = 0
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&._\-#]", password):
        score += 1
    return score

def calculate_strength_rating(length_valid, char_score):
    """Calculates a strength rating based on length validity and character diversity score."""
    if not length_valid:
        return "Too Short / Weak"
    elif char_score <= 2:
        return "Weak"
    elif char_score == 3:
        return "Moderate"
    else:
        return "Strong"

def generate_password(length=12, include_symbols=True):
    """Generates a random secure password of a given length."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if include_symbols else ""
    
    all_chars = lower + upper + digits + symbols
    if not all_chars:
        all_chars = lower
        
    # Ensure at least one character from each basic set if length permits
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    if include_symbols and symbols:
        password_chars.append(random.choice(symbols))
        
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))
        
    random.shuffle(password_chars)
    return "".join(password_chars)

def main():
    print("--- Password Strength Checker & Generator ---")
    print("1. Check password strength")
    print("2. Generate a secure password")
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == "1":
        pwd = input("Enter password to check: ")
        valid_len = check_length(pwd)
        score = check_character_sets(pwd)
        rating = calculate_strength_rating(valid_len, score)
        print(f"Strength Rating: {rating}")
    elif choice == "2":
        try:
            length_input = int(input("Enter desired length (default 12): ") or 12)
        except ValueError:
            length_input = 12
        symbols_input = input("Include symbols? (y/n): ").strip().lower() != 'n'
        new_pwd = generate_password(length_input, symbols_input)
        print(f"Generated Password: {new_pwd}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()