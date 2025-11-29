import requests
import json

API_KEY = "AIzaSyDKhUBOX8wEadDtaFX0Y1J6k6zJCZAR-rA"
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        print(response)

        data=response.json()

        print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistid = channel_items['contentDetails']['relatedPlaylists']['uploads']
        #print(channel_playlistid)

        return channel_playlistid

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__": #name is for pushing the code directly, in this case the VS and not importing it. Main is the variable for running the script.
    get_playlist_id()

