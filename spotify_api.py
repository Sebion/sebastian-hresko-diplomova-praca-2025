import json
import requests
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization":"Basic " + auth_base64,
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}

    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token

def get_auth_header(token):
    return {"Authorization":"Bearer " + token}

def get_playlist(playlist_id, token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    return response.json()

def get_playlist_tracks(playlist_id, token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    return response.json()

def get_track(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    return response.json()

def get_artist(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    return response.json()

def get_track_audio_analysis(track_id, token):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    features = response.json()

    # Extract tempo and key
    tempo = features['tempo']
    key = features['key']
    mode = features['mode']
    danceability = features['danceability']
    energy = features['energy']
    speechiness = features['speechiness']
    valence = features['valence']

    return tempo, key, mode, danceability, energy, speechiness, valence

