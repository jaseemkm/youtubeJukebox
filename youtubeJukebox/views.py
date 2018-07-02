from django.shortcuts import render
from django.http import HttpResponse
from youtubeJukebox.models import Video


def index(request):
	url_list = Video.objects.all()
	newlist = sorted(url_list, key=lambda x: x.vote, reverse=True)
	k=[x.videoId for x in newlist] 
	first=str(k[0])
	last=','.join(k)
	context = {'first':first,'last':last}
	return render (request, 'youtubeJukebox/index.html', context)