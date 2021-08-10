from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    url='users/login.html'
    error_dict={'error':'Invalid username or password'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,url,error_dict)
    return render(request,url)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
