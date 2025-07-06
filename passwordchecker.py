import unicodedata
import re

def check_password_strength(password):
    """
    Check if the password is valid and determine its strength.
    
    Returns:
        tuple: (is_valid, strength_level, feedback_messages)
    """
    feedback = []
    is_valid = True
    
    # Check minimum length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long")
        is_valid = False
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("Password must contain at least one uppercase letter")
        is_valid = False
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        feedback.append("Password must contain at least one lowercase letter")
        is_valid = False
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        feedback.append("Password must contain at least one digit")
        is_valid = False
    
    # Check for special characters
    special_chars = [char for char in password if unicodedata.category(char).startswith('P')]
    if not special_chars:
        feedback.append("Password must contain at least one special character")
        is_valid = False
    
    # Determine strength level
    strength_level = "Weak"
    if is_valid:
        if len(password) >= 12 and len(special_chars) >= 2:
            strength_level = "Very Strong"
        elif len(password) >= 10 and len(special_chars) >= 2:
            strength_level = "Strong"
        elif len(password) >= 10 or len(special_chars) >= 2:
            strength_level = "Good"
        else:
            strength_level = "Acceptable"
    
    return is_valid, strength_level, feedback

def check_common_passwords(password):
    """Check if password is in a list of common passwords."""
    common_passwords = {
        'password', '123456', '123456789', 'qwerty', 'abc123', 
        'password123', 'admin', 'letmein', 'welcome', 'monkey',
        'dragon', 'master', 'hello', 'freedom', 'whatever',
        'qwerty123', 'trustno1', 'jordan', 'harley', 'ranger',
        'jennifer', 'joshua', 'michael', 'jordan23', 'superman'
    }
    return password.lower() in common_passwords

def validate_password():
    """
    Interactive password validation with detailed feedback.
    """
    print("Password Requirements:")
    print("- At least 8 characters long")
    print("- Contains uppercase and lowercase letters")
    print("- Contains at least one digit")
    print("- Contains at least one special character")
    print("- Longer passwords (10+ chars) or multiple special characters for better strength")
    print()
    
    while True:
        password = input("Enter a password: ").strip()
        
        if not password:
            print("Please enter a password.")
            continue
        
        # Check for common passwords
        if check_common_passwords(password):
            print("⚠️  Warning: This is a commonly used password. Please choose something more unique.")
        
        # Check password strength
        is_valid, strength, feedback = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        
        if not is_valid:
            print("❌ Password is invalid. Issues found:")
            for issue in feedback:
                print(f"   • {issue}")
        else:
            print("✅ Password meets all requirements!")
            
            # Additional strength suggestions
            if strength in ["Acceptable", "Good"]:
                print("💡 Suggestions to improve strength:")
                if len(password) < 12:
                    print("   • Make it longer (12+ characters)")
                if len([c for c in password if unicodedata.category(c).startswith('P')]) < 2:
                    print("   • Add more special characters")
        
        print()
        
        # Ask if user wants to try again
        try_again = input("Try another password? (y/n): ").lower().strip()
        if try_again not in ['y', 'yes']:
            break
    
    print("Thank you for using the password checker!")

if __name__ == "__main__":
    validate_password()