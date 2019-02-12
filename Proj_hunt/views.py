from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login

from .forms import RegisterForm,LoginForm

from user_detail.models import Profile
from verify.models import verification
from Questions.models import question_model

User=get_user_model()



def index(request):
    if request.POST:
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/rules')
        else:
            print('error')
    return render(request,"Backend/index.html",{})










def register_page(request):
    context = {
        "bool":False
    }
    if request.POST:
        name = request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        signid=request.POST.get("signid")
        admission=request.POST.get("admission")
        password = request.POST.get("password")
        objs=verification.objects.filter(signid=signid)
        if objs.count()>0:
            objs.first().delete()
            new_user=User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )
            new=Profile.objects.create(
                    leader=new_user,
                    name=name,
                    admission=admission,
                    email=email,
                    number=number,
                    signid=signid
                )
            new.save()
            login(request,new_user)
            return redirect('/rules')
        else:
            context={
                "bool":True
            }
    return render(request,"Backend/register.html",context)





def rules(request):
    if request.user.is_authenticated:
        pro=Profile.objects.get(email=request.user.username)
        context={
            "name":pro.name,
        }
        return render(request,"Backend/rules.html",context)
    else:
        return render(request,"Backend/notfound.html",{})









def question(request):
    if request.user.is_authenticated:
        usr=Profile.objects.get(email=request.user.username)
        objs=question_model.objects.get(level=usr.level)
        context={
            'level':usr.level,
            'title':objs.title,
            'desc':objs.description,
        }
        if request.POST:
            lat=request.POST.get('lat')
            longi=request.POST.get('longi')
            print(lat)
            print(objs.latitude)
            print(longi)
            print(objs.longitude)
            # print(float(lat))
            if lat[:5]==str(objs.latitude)[:5] and longi[:5]==str(objs.longitude)[:5]:
                return redirect('/')
            else:
                return redirect('/rules')
        return render(request,"Backend/question.html",context)
    else:
        return render(request,"Backend/notfound.html",{})








# def login_page(request):
#     form=LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     print("User logged in ")
#     #print(request.user.is_authenticated)
#     if form.is_valid():
#         print(form.cleaned_data)
#         username=form.cleaned_data.get("username")
#         password=form.cleaned_data.get("password")
#         user=authenticate(request,username=username,password=password)
#         #print(request.user.is_authenticated)
#         print(user)
#         if user is not None:
#             #print(request.user.is_authenticated)
#             login(request,user)
#             #context["form"] = LoginForm()
#             return redirect("/")
#         else:
#             print("Error")
#     return render(request,"auth/login.html",context)




