from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import webbrowser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyA0kLPG3WHvA1tCdLsH5TuWiNMnR7SUxVI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q="Google",
    part="id,snippet",
    maxResults=2
  ).execute()

videos = []
channels = []
playlists = []

ID = ""

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
for search_result in search_response.get("items", []):
	if search_result["id"]["kind"] == "youtube#video":
      		videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
    		ID = search_result["id"]["videoId"]	
	'''
	elif search_result["id"]["kind"] == "youtube#channel":
    		channels.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["channelId"]))
    	elif search_result["id"]["kind"] == "youtube#playlist":
      		playlists.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["playlistId"]))
	'''
print "Videos:\n", "\n".join(videos), "\n"
#print "Channels:\n", "\n".join(channels), "\n"
#print "Playlists:\n", "\n".join(playlists), "\n"
print ID

url = "https://www.youtube.com/watch?v=" + ID
print url
webbrowser.open(url, new=2)
'''
argparser.add_argument("--q", help="Search term", default="Google")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()

print args
print args.q
print args.max_results
'''
