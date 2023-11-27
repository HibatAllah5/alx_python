def validate_password(password):
    if len(password < 8):
        return False
    if ' ' in password:
        return False
    
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)

    return lower and upper and digit    
