import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def get_channel_id(username: str):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": username,  # e.g., "YouTube"
        "type": "channel",
        "maxResults": 1,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    try:
        return data['items'][0]['id']['channelId']
    except IndexError:
        return None
        
def get_videos_by_channel_id(channel_id: str):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    videos = []
    
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "maxResults": 50,  # Max allowed per request (50)
        "order": "date",  # Sort by upload date (newest first)
        "type": "video",  # Only get videos (not playlists/channels)
        "key": api_key
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    with open('data.json', "w+") as f:
        json.dump(data, f, indent=4)
    
    for video in data['items']:
        videos.append(get_video_details_by_id(video['id']['videoId']))
    
    with open('videos.json', "w+") as f:
        json.dump(videos, f, indent=4)
        
    # for video in data['items']:
    #     print(video['id']['videoId'])
        
def get_video_details_by_id(video_id: str):
    video = dict()
    url = 'https://www.googleapis.com/youtube/v3/videos'
    
    params = {
        'part': 'snippet,statistics',
        'id': video_id,
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # with open('data.json', "w+") as f:
    #     json.dump(data, f, indent=4)
    
    try:
        video['url'] = f'https://youtu.be/{video_id}'
        video['title'] = data['items'][0]['snippet']['title']
        video['publishedAt'] = data['items'][0]['snippet']['publishedAt']
        video['description'] = data['items'][0]['snippet']['description']
        video['viewCount'] = int(data['items'][0]['statistics']['viewCount'])
        
        try:
            video['tags'] = data['items'][0]['snippet']['tags']
        except KeyError:
            video['tags'] = []
    except IndexError:
        with open('error.json', "w+") as f:
            json.dump(data, f, indent=4)
        exit(1)
    
    print(video)
    return video

while True:
    username = input('Enter channel username: @')
    channel_id = get_channel_id(username)

    if channel_id == None:
        print('No channel with that username found.')
        continue

    get_videos_by_channel_id(channel_id)
    
    break