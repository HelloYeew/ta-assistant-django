from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserConfigGeneralForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'page_title': 'Profile'
    }

    return render(request, 'users/profile.html', context)


@login_required
def general_setting(request):
    if request.method == 'POST':
        general_setting_form = UserConfigGeneralForm(request.POST, instance=request.user.config)
        if general_setting_form.is_valid():
            general_setting_form.save()
            messages.success(request, 'Save successful!')
            return redirect('setting-general')

    else:
        general_setting_form = UserConfigGeneralForm(instance=request.user.config)

    context = {
        'page_title': 'General Settings',
        'general_setting_form': general_setting_form
    }

    return render(request, 'users/settings-general.html', context)
