from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])  # Cambiado a 'password1'
            user.save()
            login(request, user)
            return redirect("login")  # Cambia esto si tienes una URL específica a la que redirigir
    else:
        form = UserRegisterForm()
    return render(request, "cuentas/register.html", {"form": form})


from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Especificar el request
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige al índice tras login
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})

@login_required
def logout_request(request):
    logout(request)
    return redirect('index')


@login_required
def vista_protegida(request):
    return render(request, 'cuentas/vista_protegida.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm
from .models import Profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Profile

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, CustomPasswordChangeForm


@login_required
def user_profile_view(request):
    """
    Vista para manejar y mostrar la información del usuario (UserForm)
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_profile_view')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'cuentas/user_profile.html', {
        'user_form': user_form,
    })




@login_required
def profile_details_view(request):
    """
    Vista para manejar y mostrar la información adicional del perfil (ProfileForm)
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_details_view')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'cuentas/profile_details.html', {
        'profile_form': profile_form,
    
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene al usuario autenticado
            return redirect('profile_view')  # Cambiar según tu URL de perfil
        else:
            return render(request, 'cuentas/change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'cuentas/change_password.html', {'form': form})

from django.contrib import messages  # Para mostrar mensajes de error

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Profile

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'cuentas/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

