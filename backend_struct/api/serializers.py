def validate_registration(data):
    errors = []
    if not data.get('username'):
        errors.append('Username is required')
    if not data.get('password') or len(data.get('password', '')) < 6:
        errors.append('Password must be at least 6 characters')
    return errors

def validate_login(data):
    errors = []
    if not data.get('username'):
        errors.append('Username is required')
    if not data.get('password'):
        errors.append('Password is required')
    return errors