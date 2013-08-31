from django.forms import ModelForm
from workflow.models import Spectacle

class DonateForm(ModelForm):	
	class Meta:
		model = Spectacle
	        fields = ['email_id', 'size','location']



