from django.shortcuts import render ,redirect 
from django.http import HttpResponse 
from .models import contact_info ,Blog_Category ,Subscription,blog_post
from .form import Blog_Form
# from .form import BlogPost_Form
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    # return HttpResponse('<h1>This is My Home Page </h1>')
      #fetch the data from db
    x=Blog_Category.objects.all()
    print (x)
    return render(request, 'myblogs/home.html',{"category":x})
    
def Contact(request):
    # return HttpResponse('<h1>This is My Contact Page </h1>')
    if request.method == 'GET':
        return render(request, 'myblogs/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'myblogs/contact.html',{'feedback':'Your message has been recorded'})
        return render(request,"myblogs/contact.html")

def Support(request):
    # return HttpResponse('<h1>This is My Support Page </h1>')
    return render(request,"myblogs/support.html")

def subscription(request):
#    return HttpResponse('<h1> Sucbcribe to Our Newsletter </h1>')
   if request.method == 'GET':
        return render(request, 'myblogs/newslatter.html')
   elif request.method == 'POST':
        email = request.POST.get('email')
        
        y = Subscription(u_email=email)
        
        if(Subscription.objects.filter(u_email = email).exists()):
          return render(request,"myblogs/newslatter.html",{'feedback':'You are already subscribed'})   
        else:
          y.save()
        #   print(email)
          return render(request,"myblogs/newslatter.html",{'feedback':'You are subscribed now'})
    
def blog(request):
    x = Blog_Form()  
    if request.method == "GET":
        return render(request,'myblogs/blog.html',{"x":x})
    else:
        print("hi")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("hi")
            return redirect('home')
        else:
            return render(request,'myblogs/blog.html',{"x":x})
        
def ck(request):
    x = BlogPost_Form()
    return render(request,'myblogs/ck.html',{"x":x})
        

def allblogs(request):
    y=blog_post.objects.all()
    paginator = Paginator(y, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myblogs/allblogs.html',{"y":page_obj})

def blog_details(request,blog_id):
    y=blog_post.objects.get(id=blog_id)
    
    return render(request,'myblogs/blog_details.html',{"y":y})

def loginuser(request):
    if request.method =='GET':
        return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid Credentials'})
        else:
            login(request,user)
            return redirect('home')
            
    
def signupuser(request):
    if request.method =='GET':
        return render(request,'myblogs/signupuser.html',{'form':UserCreationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password1')
        c = request.POST.get('password2')
        if b == c:
            # check wether user name is unique
            if(User.object.filter(username = a)):
                return render(request,'myblogs/signupuser.html',{'error':'Username already exist'})
            else:
                user = User.object.create_user(username =a,password=b)
                user.save()
                login(request,user)
                return redirect('home')

                
        else:
            #password 1 and 2 do not match
            return render(request,'myblogs/signupuser.html',{'error':'password Mismatch Try Again'})
    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
    
def allblog(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_post.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_post.objects.all()

    return render(request, 'myblogs/blog.html', {"blogs": blogs, "category": category_name})