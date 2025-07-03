import unicodedata

def password():
    """
    Check if the password is valid.
    A valid password must:
    - Be at least 8 characters long
    - contain at least one uppercase letter
    - contain at least one lowercase letter
    - contain at least one digit
    - contain at least one special character
    - be at least 10 characters long or contain at least two special characters
    """
    prompt = 'Enter a password: '
    password = input(prompt)
    if len(password) < 8 or not any(l.isupper() for l in password) or not any(l.islower() for l in password) or not any (l.isdigit() for l in password) or not any (unicodedata.category(l).startswith('P') for l in password):
        return 'Invalid password'
    count = 0
    for l in password:
        if unicodedata.category(l).startswith('P'):
            count += 1
    if len(password) > 10 or count >= 2:
        return 'Strong Password'

print(password())