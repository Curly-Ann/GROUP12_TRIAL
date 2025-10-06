#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

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

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_struct.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
