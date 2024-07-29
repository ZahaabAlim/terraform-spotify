import base64
import requests
import os

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIFY_REDIRECT_URI']
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded"
}
auth_url = f"https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope=playlist-modify-public&redirect_uri={redirect_uri}"
print(f"Authorize your app by visiting this url: {auth_url}")
code = input("Enter the authorization code obtained from the URL: ")
data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri
}
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
response_data = response.json()
access_token = response_data['access_token']
print(f"::set-output name=spotify_access_token::{access_token}")
