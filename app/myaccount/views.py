from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile
from .forms import ProfileForm


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account/profile.html', context)


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            avatar = form.cleaned_data['avatar']
            if avatar:
                user_profile.avatar = avatar
            user_profile.save()

            return redirect('myaccount:profile')
    else:
        default_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': user_profile.avatar,
        }
        form = ProfileForm(default_data)
        context = {
            'form': form,
            'user': user,
        }

        return render(request, 'account/profile_update.html', context)
