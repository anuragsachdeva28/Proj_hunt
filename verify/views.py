from django.shortcuts import render
from django.contrib.auth import get_user_model,authenticate,login

from .models import verification
User=get_user_model()

def gen(request):
	objs=verification.objects.all()
	li=[]
	for i in objs:
		li.append(i.signid)
	data={
		'reg':li,
		'range':range(4)
	}
	return render(request,"Backend/gen.html",data)



def gen2(request):
	if request.POST:
		u=request.POST.get('e')
		p=request.POST.get('p')
		s=request.POST.get('s')
		if s=="asdfghjkl":
			usr=User.objects.create_superuser(username=u,email=u,password=p)
			usr.save()

	return render(request,"Backend/gen2.html",{})

