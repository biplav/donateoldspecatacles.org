# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from workflow.forms import DonateForm
from workflow.models import Spectacle
from django.core.mail import send_mail


def get_total_donation():
	return Spectacle.objects.count()

def mail(to,subject,content):
	send_mail(subject, content, "donateoldspectacles@gmail.com", [to], fail_silently=False)

def index(request):
	if request.method == 'POST':
        	form =DonateForm(request.POST)
        	if form.is_valid():
            		donate = form.save()
			id = donate.id
			message="""
Hello,

Thanks for your donation.
Your donation id is %s. Please wrap the spectacles with a piece of paper with this id written.
Please visit http://www.donateoldspectacles.org/home/search?query=%s to track your donation.
				
Regards,
DonateoldSpectacles.org Team.
					
			""" % (("BS00"+str(id)),("BS00"+str(id)))
			mail(donate.email_id,"Thanks for your donation",message)

			context =  { 'latest_count': get_total_donation(),
                     		     'form' : form,
				     'donate_id': id,	
                	}
		else: #Form error scenario
			context =  { 'latest_count': get_total_donation(),
                     		     'form' : form,
                	}

	else:
		form = DonateForm()
		context =  { 'latest_count': get_total_donation(),
		     'form' : form,
		}
	return render(request, 'index.html', context)

def how(request):
	context =  { 'latest_count': get_total_donation(),}
	return render(request, 'how.html', context)

def contact(request):
	context = { 'latest_count':get_total_donation() }
	return render(request,'contact.html',context)

def ngo(request):
	context = { 'latest_count':get_total_donation() }
	return render(request,'ngo.html',context)

def optical(request):
	context = { 'latest_count':get_total_donation() }
	return render(request,'optical.html',context)

def corporate(request):
	context = { 'latest_count':get_total_donation() }
	return render(request,'corporate.html',context)

def search(request):
	query=request.GET['query']
	query_id=query.replace("BS00","")
	data = Spectacle.objects.filter(id__iexact=query_id) | Spectacle.objects.filter(email_id__icontains=query)
	context = { 'latest_count':get_total_donation(),
		    'data':data		
	 }
	return render(request,'search.html',context)
