from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Post
# Create your views here.
def index(request):
    post = Post.objects.all()

    context = {'post':post}
    return render(request,'index.html',context)
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        a = authenticate(username=username,password=password)
        if a is not None:
            login(request,a)
            return redirect('index')
    context = {}    
    return render(request,'login.html',context)
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            user  = User.objects.create_user(username,email,password)
            user.save()
            return redirect('login')
    context = {}
    return render(request,'signup.html',context)
def blog(request):
    context = {}
    return render(request,'blog.html',context)
def post(request,postid):
    post = Post.objects.get(id=postid)
    context = {'post':post}
    return render(request,'Post.html',context)

def logout1(request):
    logout(request)
    return redirect('login')