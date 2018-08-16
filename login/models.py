from django.db import models
import collections



# Create your models here.
class registration(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

	def __int__(self):
		return self.id

	class Meta:
		db_table="login_registration"

