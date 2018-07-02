from django.core.management.base import BaseCommand
from slackclient import SlackClient
from youtubeJukebox.models import Video
from urllib.parse import urlparse,parse_qs
import re
import time

class Command(BaseCommand):
    def handle(self,**option):
    	session = start_listening()

def start_listening():
	token = 'xoxb-392118745879-390358916160-HUJ3Tc7ldBHUomAQDUQYyxV9'
	link_format=r"^<((https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+)>$"
	slack_client = SlackClient(token)
	if slack_client.rtm_connect():
		while True:
			events = slack_client.rtm_read()
			print(events)
			for event in events:
				if event['type']=='message' and "hidden" not in event :
					match = re.search(link_format, event['text'])
					if match :
						link = match.group(1)
						add_item(link)
			time.sleep(1)


            
def add_item(link):
	videoId = get_id(link)
	values = Video(url = link, videoId = videoId)
	values.save()
	print("\nItem added to database")

def get_id(link):
	url_data = urlparse(link)
	query = parse_qs(url_data.query)
	videoId = query["v"][0]
	return videoId

