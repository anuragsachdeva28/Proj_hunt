from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login

from .forms import RegisterForm,LoginForm

from user_detail.models import Profile


def index(request):
    return render(request,"1.html",{})

User=get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user=User.objects.create_user(username,email,password)
        print(new_user)
        leadername=form.cleaned_data.get("leadername")
        email1=form.cleaned_data.get("email1")
        email2=form.cleaned_data.get("email2")
        email3=form.cleaned_data.get("email3")
        branch1=form.cleaned_data.get("branch1")
        branch2=form.cleaned_data.get("branch2")
        branch3=form.cleaned_data.get("branch3")
        contact1=form.cleaned_data.get("contact1")
        contact2=form.cleaned_data.get("contact2")
        contact3=form.cleaned_data.get("contact3")
        participant2=form.cleaned_data.get("participant2")
        participant3=form.cleaned_data.get("participant3")

        new_profile=Profile.objects.create(
            leader=new_user,
            leadername=leadername,
            participant2=participant2,
            participant3=participant3,
            email1=email1,
            email2=email2,
            email3=email3,
            branch1=branch1,
            branch2=branch2,
            branch3=branch3,
            contact1=contact1,
            contact2=contact2,
            contact3=contact3
        )
        new_profile.save()
    return render(request,"auth/register.html",context)

def login_page(request):
    form=LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in ")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        #print(request.user.is_authenticated)
        print(user)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request,user)
            #context["form"] = LoginForm()
            return redirect("/")
        else:
            print("Error")
    return render(request,"auth/login.html",context)




