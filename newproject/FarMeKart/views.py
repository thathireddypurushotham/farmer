from django.shortcuts import render,redirect
from FarMeKart.forms import UsregFo,ChpwdForm,UpdPfle,Vegfr
from django.contrib.auth.decorators import login_required
from farmer import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from FarMeKart.models import Vegpro

# Create your views here.

def home(request):
	return render(request,"html/home.html")

def contact(re):
	return render(re,"html/contact.html")

def about(re):
	return render(re,"html/about.html")

def registration(request):
	if request.method=="POST":
		k = UsregFo(request.POST)
		if k.is_valid():
			e = k.save(commit=False)
			sb = "Testing Email For FarMeKart"
			mg = "Hi Welcome{}. You have successfully registered for FarMeKart portal.".format(e.username)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[e.email])
			if snt == 1:
				e.save()
				return redirect('/lg')
			else:
				return redirect('/')
	k=UsregFo()
	return render(request,'html/register.html',{'h':k})

@login_required
def cgf(re):
	if re.method=="POST":
		c=ChpwdForm(user=re.user,data=re.POST)
		if c.is_valid():
			c.save()
			return redirect('lg/')
	c=ChpwdForm(user=re.user)
	return render(re,'html/changepassword.html',{'t':c})

@login_required
def profile(req):
	return render(req,'html/profile.html')

@login_required
def updprofile(request):
	if request.method == "POST":
		t = UpdPfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			return redirect('/pro')
	t = UpdPfle(instance=request.user)
	return render(request,'html/updateprofile.html',{'z':t})


@login_required
def dashboard(re):
	return render(re,'html/dashboard.html')

@login_required
def farmerdashboard(request):
	return render(request,'html/farmerdashboard.html')

@login_required
def delitem(req,t):
	data=Vegpro.objects.get(id=t)
	print(data.id)
	if req.method == "POST":
		print(data.id)
		data.delete()
		return redirect('/dt')
	return render(req,'html/userdelete.html',{'sd':data})


@login_required
def vegf(request):
	t = Vegpro.objects.filter(a_id=request.user.id)
	if request.method == "POST":
		s = Vegfr(request.POST,request.FILES)
		if s.is_valid():
			r = s.save(commit=False)
			r.a_id = request.user.id
			r.save()
			return redirect('/dsf')
	s=Vegfr()
	return render(request,'html/data.html',{'a':s,'e':t})







