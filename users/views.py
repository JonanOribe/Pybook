from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

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
