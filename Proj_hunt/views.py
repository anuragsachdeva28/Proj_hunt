from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from django.utils import timezone

from .forms import RegisterForm,LoginForm

from user_detail.models import Profile
from verify.models import verification
from Questions.models import question_model
import random

User=get_user_model()



def index(request):
    if request.POST:
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            pro=Profile.objects.get(email=username)
            if pro.rules:
                if request.GET.get('q')!=None:
                    return redirect('/question?q='+request.GET.get('q'))
                else:
                    return redirect('/question')
            else:
                return redirect('/rules')
        else:
            print('error')
    return render(request,"Backend/index.html",{})










def register_page(request):
    context = {
        "bool":False
    }
    print(request.POST)
    if request.POST:
        name = request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        signid=request.POST.get("signid")
        admission=request.POST.get("admission")
        password = request.POST.get("password")
        objs=verification.objects.filter(signid=signid)
        if objs.count()>0:
            if objs.first().signid!='archit':
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
                    signid=signid,
                    lastsub=timezone.now(),
                    rules=True
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
        if not(pro.freeze):
            context={
                "name":pro.name,
                "login":True
            }
            return render(request,"Backend/rules.html",context)
        else:
            return render(request,"Backend/freeze.html",{})
    else:
        context={
            "login":False
        }
        return render(request,"Backend/rules.html",context)









def question(request):
    if request.user.is_authenticated:
        usr=Profile.objects.get(email=request.user.username)
        if not(usr.freeze):
            if usr.level>4:
                return render(request,'Backend/completed.html',{})
            objs=question_model.objects.get(level=usr.level)
            context={
                'level':usr.level,
                'title':objs.title,
                'desc':objs.description,
                'wrong':False,
                'obj':objs,
                'correct':False,
                'lucky':False,
                'unlucky':False
            }
            if request.GET.get('q')!=None:
                ans=objs.correct_ans
                ans1=request.GET.get('q')
                if ans1=="CqCOHJwQMRzGVtPCO46m" and not(usr.q1):
                    usr.q1=True
                    asd=random.choice([1,0])
                    if asd==1:
                        usr.points=usr.points+10
                        context['lucky']=True
                    else:
                        usr.points=usr.points-10
                        context['unlucky']=True
                    usr.save()
                elif ans1=="JeWVPtXTB7vqCXKPhOdC" and not(usr.q2):
                    usr.q2=True
                    asd=random.choice([1,0])
                    if asd==1:
                        usr.points=usr.points+10
                        context['lucky']=True
                    else:
                        usr.points=usr.points-10
                        context['unlucky']=True
                    usr.save()
                elif ans1=="szKEehshvHyRnljQW9UM" and not(usr.q3):
                    usr.q3=True
                    asd=random.choice([1,0])
                    if asd==1:
                        usr.points=usr.points+10
                        context['lucky']=True
                    else:
                        usr.points=usr.points-10
                        context['unlucky']=True
                    usr.save()
                elif ans1=="Nk7fclTlPrfYjUaMP72G" and not(usr.q4):
                    usr.q4=True
                    asd=random.choice([1,0])
                    if asd==1:
                        usr.points=usr.points+10
                        context['lucky']=True
                    else:
                        usr.points=usr.points-10
                        context['unlucky']=True
                    usr.save()
                elif ans==ans1:
                    usr.level=usr.level+1
                    if usr.attempts<=3:
                        usr.points=usr.points+10-((usr.attempts)*2)
                    else:
                        usr.points=usr.points+4
                    usr.attempts=0
                    usr.lastsub=timezone.now()
                    usr.save()
                    if usr.level<=objs.top_level:
                        objs=question_model.objects.get(level=usr.level)
                        context={
                            'level':usr.level,
                            'title':objs.title,
                            'desc':objs.description,
                            'obj':objs,
                            'correct':True
                        }
                    else:
                        return render(request,'Backend/completed.html',{})
                else:
                    context['wrong']=True
                    usr.attempts=usr.attempts+1
                    if usr.attempts>=5:
                        usr.freeze=True
                        usr.save()
                        return render(request,'Backend/freeze.html',{})
                    usr.save()
            return render(request,"Backend/question.html",context)
        else:
            return render(request,"Backend/freeze.html",{})
    else:
        if request.GET.get('q')!=None:
            return redirect('/?q='+request.GET.get('q'))
        else:
            return redirect('/')




def leaderboard(request):
    objs=Profile.objects.all()
    context={
        "object":objs,
    }
    if request.user.is_authenticated:
        obj=Profile.objects.filter(email=request.user.username).first()
        count=0
        for i in objs:
            count=count+1
            if i.email==obj.email:
                break
        context={
            "hg":True,
            "point":obj.points,
            "object":objs,
            "rank":count,
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




