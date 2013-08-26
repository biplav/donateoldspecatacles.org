from django.db import models

class Power(models.Model):
    	right_distance_spherical = models.FloatField(default=0)
    	right_distance_cylinderical = models.FloatField(default=0)
	right_distance_cylinderical_axis = models.FloatField(default=0)
	right_near_spherical = models.FloatField(default=0)
        right_near_cylinderical = models.FloatField(default=0)
        right_near_cylinderical_axis = models.FloatField(default=0)
	right_prism = models.FloatField(default=0)
	left_distance_cylinderical_axis = models.FloatField(default=0)
	left_distance_cylinderical = models.FloatField(default=0)
	left_distance_spherical = models.FloatField(default=0)
        left_near_spherical = models.FloatField(default=0)
        left_near_cylinderical = models.FloatField(default=0)
        left_near_cylinderical_axis = models.FloatField(default=0)
	left_prism = models.FloatField(default=0)
	add = models.FloatField(default=0)
	def __unicode__(self):
		right_eye =  u'OD -%s +%s SPH -%s x%s +%s x%s %s add %s p.d' % (self.right_distance_spherical,self.right_near_spherical,self.right_distance_cylinderical,self.right_distance_cylinderical_axis, self.right_near_cylinderical, self.right_near_cylinderical_axis,self.add,self.right_prism)
		left_eye =  u'OD -%s +%s SPH -%s x%s +%s x%s %s add %s p.d' % (self.left_distance_spherical,self.left_near_spherical,self.left_distance_cylinderical,self.left_distance_cylinderical_axis, self.left_near_cylinderical, self.left_near_cylinderical_axis,self.add,self.left_prism)
	        return right_eye+'::'+left_eye

class Optician(models.Model):
	name = models.CharField(max_length=400)
	address = models.CharField(max_length=600)
	emailId = models.EmailField(max_length=200)
	image_logo = models.SlugField(max_length=600)
	phone = models.BigIntegerField(default=0)

class NGO(models.Model):
	name = models.CharField(max_length=400)
        address = models.CharField(max_length=600)
        emailId = models.EmailField(max_length=200)
        image_logo = models.SlugField(max_length=600)
        phone = models.BigIntegerField(default=0)
	

class Spectacle(models.Model):
	SIZES = (
        	('S', 'Kids'),
	        ('M', 'Medium'),
        	('L', 'Large'),
   	 )
    	id = models.AutoField(primary_key=True)
	email_id = models.CharField(max_length=200)
	size = models.CharField(max_length=1,choices=SIZES)
	donate_date = models.DateField(auto_now_add=True)
	power = models.ForeignKey(Power,null=True)
	date_recieved = models.DateTimeField('date recived', blank=True, null=True)
	processed_by = models.ForeignKey(Optician,null=True)
	donated_to = models.ForeignKey(NGO,null=True)
	final_comments = models.CharField(max_length=400,null=True)
	donation_image = models.SlugField(max_length=400,null=True) 

