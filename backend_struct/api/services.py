from django.contrib.auth.hashers import make_password
from .models import User
from .validators import validate_registration

def register_user(data):
    errors = validate_registration(data)
    if errors:
        return {'success': False, 'errors': errors}
    
    if User.objects.filter(username=data['username']).exists():
        return {'success': False, 'errors': ['Username already exists']}
    
    user = User.objects.create(
        username=data['username'],
        password=make_password(data['password']),
        role=data.get('role', 'user')
    )
    return {'success': True, 'data': {'id': user.id, 'username': user.username}}