from django.shortcuts import render, redirect
from django.http import HttpResponse
from youtubeJukebox.models import Video, User, Vote
from django_slack_oauth.models import SlackUser


def index(request):
	if request.session.test_cookie_worked():
		print (">>>> TEST COOKIE WORKED!")
		request.session.delete_test_cookie()
	url_list = Video.objects.all()
	newlist = sorted(url_list, key=lambda x: x.vote, reverse=True)
	k=[x.videoId for x in newlist] 
	first=str(k[0])
	last=','.join(k)
	context = {'first':first,'last':last}
	response = render (request, 'youtubeJukebox/index.html', context)
	if 'user' in request.session :
		print("jaseem")
		response.set_cookie('user',request.session['user'] )
	return response

def vote(request):
	vid = request.GET['vid']
	values = Vote(user_id=request.session['userid'],videoId=vid)
	values.save()
	data = Video.objects.get(videoId=vid)
	data.vote+=1
	data.save()
	return redirect('/youtubeJukebox')
	

def debug_oauth_request(request, api_data):
	print(api_data)
	request.session['foo'] = 'bar'
	return request, api_data

def register_user(request, api_data):
	if api_data['ok']:
		useridList = User.objects.all()
		userList = {q.user_id for q in useridList}
		if api_data['user']['id'] not in userList :
			values = User(user=api_data['user']['name'],user_id=api_data['user']['id'])
			values.save()
			print("\nNew User added to database")
		else :
			print("\nUser already exist")
	request.session['user'] = api_data['user']['name']
	request.session['userid'] = api_data['user']['id']
	request.session['access_token'] = api_data['access_token']


	return request, api_data

def logout(request):
	del request.session['user']
	return redirect('/youtubeJukebox')