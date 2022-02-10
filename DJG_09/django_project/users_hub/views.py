from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users_hub.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}! Your account has been created! Now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users_hub/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users_hub/profile.html')
