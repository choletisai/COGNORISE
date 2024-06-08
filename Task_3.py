import string 
import random

def generate_password(length, complexity):
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation

    if complexity == 1:
        # Weak: only lowercase letters
        combine = lowerD
    elif complexity == 2:
        # Medium: lowercase and uppercase letters
        combine = lowerD + upperD
    elif complexity == 3:
        # Strong: lowercase, uppercase, and digits
        combine = lowerD + upperD + digitD
    elif complexity == 4:
        # Very strong: lowercase, uppercase, digits, and symbols
        combine = lowerD + upperD + digitD + symbolsD
    else:
        print("Invalid complexity level. Please choose a valid option.")
        return None

    if length < 1:
        print("Invalid length. Length must be greater than 0.")
        return None

    password = ''.join(random.sample(combine, length))
    return password

def main():
    print("Welcome to our Password Generator")
    try:
        length = int(input("Enter the length of password you want: "))
        print("Select password strength: ")
        print("1. Weak (only lowercase letters)")
        print("2. Medium (lowercase and uppercase letters)")
        print("3. Strong (lowercase, uppercase, and digits)")
        print("4. Very Strong (lowercase, uppercase, digits, and symbols)")
        complexity = int(input("Enter the complexity level (1-4): "))
        
        password = generate_password(length, complexity)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for length and complexity.")

if __name__ == "__main__":
    main()
