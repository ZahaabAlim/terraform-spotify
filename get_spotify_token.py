import requests
import base64

# Your Client ID and Client Secret
client_id = 'c4ec12b33f8548bfb9152254836b777f'
client_secret = 'fe2392ff7b8a4fb3a59c1ccc9188fc52'

# Encode the client ID and client secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Request headers
headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Request body
data = {
    'grant_type': 'client_credentials'
}

# Make the POST request
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

# Get the access token from the response
access_token = response.json().get('access_token')
print(f"Access Token: {access_token}")