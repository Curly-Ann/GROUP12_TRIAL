from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return render(request, 'accounts/register.html', {'form': RegisterForm(), 'success': True})
    return render(request, 'accounts/register.html', {'form': form})

# 🔹 Add this function (for login page)
def login_view(request):
    return render(request, 'accounts/login.html')
