import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Final evaluation
    if strength == 5:
        return "Strong password ✅", []
    elif strength >= 3:
        return "Moderate password ⚠️", feedback
    else:
        return "Weak password ❌", feedback

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password to check strength: ")
    result, advice = check_password_strength(pwd)
    print("\nResult:", result)
    if advice:
        print("Suggestions to improve your password:")
        for tip in advice:
            print("-", tip)
