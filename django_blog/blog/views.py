from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally: user.is_active=False and email verification flow could be added.
            messages.success(request, f'Account created for {user.username}. You can now log in.')
            return redirect('blog:login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile
# For login/logout, use Django's built-in auth views via urls (see urls.py below)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('blog:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'blog/profile.html', context)