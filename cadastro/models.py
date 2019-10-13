from django.db import models

# Create your models here.
class EmailCliente(models.Model):
	nome	= models.CharField(max_length=120)
	contato	= models.EmailField(max_length=254)
	dia		= models.DateField() #input_formats=['%d/%m/%Y']
	hora	= models.TimeField() #input_formats=['%H:%M']
	mandado	= models.BooleanField(default=False)
		