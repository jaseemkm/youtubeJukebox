from django.core.management.base import BaseCommand
from slackclient import SlackClient
from youtubeJukebox.models import Video
from urllib.parse import urlparse,parse_qs
import re
import time
from jukebox.settings import ACCESS_TOKEN

 #YouTube video IDs form link          
def get_id(link):
	urlData = urlparse(link)
	query = parse_qs(urlData.query)
	videoId = query["v"][0]
	return videoId
#Adding values to database
def add_item(link):
	videoId = get_id(link)
	video = Video.objects.filter(videoId=videoId)
	if not video:
		values = Video(url = link, videoId = videoId)
		values.save()
		print("\nItem added to database")
	else :
		print("\nValue already exists")

def start_listening():
	#Bot User OAuth Access Token
	token = ACCESS_TOKEN
	linkFormat=r"^<((https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+)>$"
	slackClient = SlackClient(token)
	#Reading messages from slack 
	if slackClient.rtm_connect():
		while True:
			events = slackClient.rtm_read()
			for event in events:
				if event['type']=='message' and "hidden" not in event :
					#Matching YouTube links
					match = re.search(linkFormat, event['text'])
					if match :
						link = match.group(1)
						add_item(link)
			time.sleep(1)

class Command(BaseCommand):
    def handle(self,**option):
    	session = start_listening()
