from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import speech_recognition as sr
import webbrowser

DEVELOPER_KEY = "AIzaSyA0kLPG3WHvA1tCdLsH5TuWiNMnR7SUxVI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

r = sr.Recognizer()
query = ""
while(1):
	print 'say the song name...'
	with sr.Microphone() as source:                # use the default microphone as the audio source
	    	audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
	try:
	 	query = r.recognize_google(audio)   
		print("You said " + query)    # recognize speech using Google Speech Recognition
		break
	except LookupError:                            # speech is unintelligible
	    	print("Could not understand audio")

search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=1
  ).execute()

ID = ""

for search_result in search_response.get("items", []):
	if search_result["id"]["kind"] == "youtube#video":
      		#videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
    		ID = search_result["id"]["videoId"]

url = "https://www.youtube.com/watch?v=" + ID
webbrowser.open(url, new=2)
