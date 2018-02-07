import django
from django.db import models

# Create your models here.

##########################################################################################
# First, define the Manager subclass.
class QuestionManager(models.Manager):
#	def get_queryset(self):
#		return super().get_queryset().filter(author='Roald Dahl')
	def new(self):
	    return self.order_by('-added_at')

	def popular(self):
	    return self.order_by('-rating')

##########################################################################################

##########################################################################################


class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField()
	# username = "NoNameUser", password = "NoPassword"
	# author = django.contrib.auth.models.User()
	author = models.ForeignKey( django.contrib.auth.models.User, related_name="questions", related_query_name="author", null=True, on_delete=models.SET_NULL)





	# List - ?
	likes = models.ManyToManyField( django.contrib.auth.models.User)

	# Then hook it into the model explicitly.
	#objects = models.Manager() # The default manager.
	objects = QuestionManager()
	#dahl_objects = DahlBookManager() # The Dahl-specific manager.


#	def __unicode__(self):
#		return self.title
	def get_absolute_url(self):
		return '/question/%d/' % self.pk
	class Meta:
		db_table = 'questions'
		ordering = ['-added_at']

##########################################################################################



class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey( Question, null=False, on_delete=models.CASCADE)
	author = models.ForeignKey( django.contrib.auth.models.User, null=True, on_delete=models.SET_NULL)

#	def __unicode__(self):
#		return self.title
#	def get_absolute_url(self):
#		return '/question/%d/' % self.pk

	class Meta:
		db_table = 'answers'
		ordering = ['-added_at']


##########################################################################################
