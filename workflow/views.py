# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from workflow.forms import DonateForm
from workflow.models import Spectacle


def get_total_donation():
	return Spectacle.objects.count()

def index(request):
	if request.method == 'POST':
        	form =DonateForm(request.POST)
        	if form.is_valid():
            		donate = form.save()
			id = donate.id
			context =  { 'latest_count': get_total_donation(),
                     		     'form' : form,
				     'donate_id': id,	
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
