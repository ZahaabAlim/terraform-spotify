import base64
import requests
import os

client_id = os.environ['c4ec12b33f8548bfb9152254836b777f']
client_secret = os.environ['fe2392ff7b8a4fb3a59c1ccc9188fc52']
redirect_uri = os.environ['http://localhost:27228/spotify_callback']
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
