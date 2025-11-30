import requests
import json
import os
from dotenv import load_dotenv

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"
maxResults = 50


load_dotenv(dotenv_path="./.env")

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        print(response)

        data=response.json()

        print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistid = channel_items['contentDetails']['relatedPlaylists']['uploads']
        print(channel_playlistid)

        return channel_playlistid

    except requests.exceptions.RequestException as e:
        raise e




#playlistID=get_playlist_id()

def get_video_ids(playlistId):
    video_ids = []
    pageToken = None
    #https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=1&pageToken=EAAaHlBUOkNBRWlFRVUxTlVFNVFqZzJRVEF4UXprMU1rRQ&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key=[YOUR_API_KEY]
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key{API_KEY}"

    try:
        while True:
            url = base_url
            if pageToken:
                url += f"&pageToken={pageToken}"

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            for item in data.get('items',[]):    
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')
            if not pageToken:
                break

        #print(video_ids)
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__": #name is for pushing the code directly, in this case the VS and not importing it. Main is the variable for running the script.
    playlistID = get_playlist_id()
    print(get_video_ids(playlistID))
