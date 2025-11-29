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

base_url = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId=UUX60Q3DkcsbYNE6H8uQQuVA&key{API_KEY}"


playlistID=get_playlist_id()

if __name__ == "__main__": #name is for pushing the code directly, in this case the VS and not importing it. Main is the variable for running the script.
    get_playlist_id()

