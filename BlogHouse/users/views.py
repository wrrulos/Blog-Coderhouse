from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from publicaciones.models import publicacion
from users.forms import custom_user_creation_form,profile_form, profile_main_fields_form
from users.models import Profile


def profile_view(request):
    """
    Show posts
    """
    
    posts = get_user_posts(request)

    if posts is None:
        aux = {'errors': 'Aún no tienes publicaciones'}

    else:
        aux = {'posts': posts}
        
    try:
        user_profile = Profile.objects.get(user=request.user.id)

    except:
        user_profile = None
    
    if user_profile is None:
        context = create_profile_view(request)

    else:
        context = update_profile_view(request,user_profile)
    
    context.update(aux)
    return render(request,'user_profile/user_profile_template.html',context=context)


def create_profile_view(request):
    """
    Create the profile
    """

    context = {}

    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES or None)

        if form.is_valid():
            new_profile = Profile.objects.create(
                user = request.user,
                name = form.cleaned_data['name'],
                surname = form.cleaned_data['surname'],
                birthday = form.cleaned_data['birthday'],
                country = form.cleaned_data['country'],
                img_profile = form.cleaned_data['img_profile']
            )
            form = profile_form(instance=new_profile)
            context = {'form': form}

        else:
            form_errors = form.errors
            form = profile_form()
            context = {'error_message':form_errors,'form':form}
            
    else:
        form = profile_form()
        context = {'form':form}
    
    return context    
    
def update_profile_view(request,profile):
    """
    Update posts
    """
    
    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES or None, instance=profile)
        
        if form.is_valid():
            form.save()
            form = profile_form(instance = form.instance)
            context = {'form': form}     

    else:
        form = profile_form(instance = profile)
        context = {'form':form}

    return context


def get_user_posts(request):
    """
    Get user posts
    """

    publicaciones = publicacion.objects.filter(user=request.user)
    
    if not publicaciones.exists():
        publicaciones = None
    
    return publicaciones


def register_view(request):
    """
    Registration function for the page
    """

    if request.method == 'POST':
        form = custom_user_creation_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            context = {'message':f'¡Gracias por registrarse en Bloggerhouse!¡Bienvenido {username}!'}            
            return redirect('index')

        else:            
            errors = form.errors
            form = custom_user_creation_form()
            context = {'errors':errors,'form':form}            
            return render (request, 'auth/user_register_template.html', context = context)

    else:
        form = custom_user_creation_form()
        context = {'form' : form}
        return render(request,'auth/user_register_template.html',context = context)
    
    
def login_view(request):
    """
    Login function for the page
    """

    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']            
            user = authenticate(username = username,password = password)

            if user is not None:
                login(request,user)
                return redirect('index')

            else:
                context = {'errors': 'Usuario y/o contraseña invalidos'}
                form = AuthenticationForm()                
                return render(request,'auth/user_login_template.html',context = context)
                
        else:
            errors = form.errors        
            form = AuthenticationForm()        
            context = {'errors':errors,'form':form}
            return render(request,'auth/user_login_template.html',context = context)
            
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'auth/user_login_template.html',context = context)


def logout_view(request):
    """
    Logout
    """

    logout(request)
    return redirect('index')
