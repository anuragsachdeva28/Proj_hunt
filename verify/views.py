from django.shortcuts import render

from .models import verification

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

