from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .admin import CustomUserCreationForm
from django.urls import reverse_lazy


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='friends')
            user.groups.add(group)
            user.save()
            print(user.groups)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
