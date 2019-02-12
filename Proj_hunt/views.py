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
        if usr.level>2:
            return render(request,'Backend/completed.html',{})
        objs=question_model.objects.get(level=usr.level)
        context={
            'level':usr.level,
            'title':objs.title,
            'desc':objs.description,
            'wrong':False
        }
        if request.POST:
            ans=objs.correct_ans
            ans1=request.POST.get('ans1')
            if ans==ans1:
                usr.level=usr.level+1
                if usr.attempts<=3:
                    usr.points=usr.points+10-((usr.attempts)*2)
                else:
                    usr.points=usr.points+4
                usr.attempts=0
                usr.save()
                if usr.level<=objs.top_level:
                    objs=question_model.objects.get(level=usr.level)
                    context={
                        'level':usr.level,
                        'title':objs.title,
                        'desc':objs.description,
                    }
                else:
                    return render(request,'Backend/completed.html',{})
            else:
                context['wrong']=True
                usr.attempts=usr.attempts+1
                usr.save()
        return render(request,"Backend/question.html",context)
    else:
        return render(request,"Backend/notfound.html",{})




def leaderboard(request):
    objs=Profile.objects.all().order_by('-points')
    context={
        "object":objs,
    }
    if request.user.is_authenticated:
        obj=Profile.objects.filter(email=request.user.username).first()
        context={
            "hg":True,
            "point":obj.points,
            "object":objs,
        }

    return render(request,'Backend/leaderboard.html',context)






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




