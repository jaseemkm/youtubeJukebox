from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	first = 'vaeFlvODsDs'
	last = ['vaeFlvODsDs','Rd9wF5fAnVw','AQWPkdE6jbw']
	context = {'first':first,'last':",".join(last)}
	return render (request, 'youtubeJukebox/index.html', context)