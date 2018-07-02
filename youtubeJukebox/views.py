from django.shortcuts import render, redirect
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

def vote(request):
	vid = request.GET['vid']
	data = Video.objects.get(videoId=vid)
	data.vote+=1
	data.save()
	return redirect('/youtubeJukebox')