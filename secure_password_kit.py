import random
from validation import valid_number

def pass_strength(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    digits = "0123456789"
    symbols = "!@#$%^&*()"
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch in lowercase:
            has_lower = True
        elif ch in uppercase:
            has_upper = True
        elif ch in digits:
            has_digit = True
        elif ch in symbols:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        if len(password) >= 12:
            return "STRONG"
        elif len(password) >= 8:
            return "MEDIUM"
        else:
            return "WEAK"
    else:
        return "WEAK"
        
def create():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    digits = "0123456789"
    symbols = "!@#$%^&*()"
    all_chars = lowercase + uppercase + digits + symbols
    while True:
        length = input("Enter password length (8 - 20): ").strip()
        if not length:
            print("Input a length")
            continue
        if not valid_number(length):
            print("Enter a valid number")
            continue
        length = int(length)
        if length < 8:
            print("Length of password cannot be less than 8 characters")
            continue
        if length > 20:
            print("Length of password cannot be more than 20 characters")
            continue
        chars = []
        chars.append(random.choice(lowercase))
        chars.append(random.choice(uppercase))
        chars.append(random.choice(digits))
        chars.append(random.choice(symbols))
        for i in range(length - 4):
            chars.append(random.choice(all_chars))
        random.shuffle(chars)
        password = ""
        for ch in chars:
            password += ch
        break
    print(f"Generated password: {password}")
    strength = pass_strength(password)
    print(f"Strength: {strength}")
    
def check():
    while True:
        password = input("Input the password to be checked: ").strip()
        if not password:
            print("Enter a password")
            continue
        break
    strength = pass_strength(password)
    print(f"Strength: {strength}")

def show_rules():
    print("\n" + "="*40)
    print("PASSWORD GENERATION RULES")
    print("="*40)
    print("• Length: between 8 and 20 characters")
    print("• Must include at least one of each:")
    print("  - Uppercase letter (A-Z)")
    print("  - Lowercase letter (a-z)")
    print("  - Digit (0-9)")
    print("  - Special character (!@#$%^&*())")
    print("\nSTRENGTH CRITERIA:")
    print("• WEAK   : length < 8 OR missing any type")
    print("• MEDIUM : length 8-11 AND all types present")
    print("• STRONG : length ≥ 12 AND all types present")
    print("="*40 + "\n")
    
def leave():
    exit()    
print("====================================\n\tPASSWORD GENERATOR & CHECKER\n====================================")
print("1. Generate a new password\n2. Check strength of a password you provide\n3. View generation rules\n4. Exit\n")
choices = ["1", "2", "3", "4"]
options = [create, check, show_rules, leave]
while True:
    choice = input("Pick a choice from 1 - 4: ").strip()
    if choice not in choices:
        print("Invalid choice")
        continue
    index = int(choice) - 1
    action = options[index]
    action()
    print()
