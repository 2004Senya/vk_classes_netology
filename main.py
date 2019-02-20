from urllib.parse import urlencode
import requests

APP_ID = 6869362
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.92'
}

print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = 'TOKEN'

class User:
    def __init__(self, token):
        self.token = token

    def getMutual(self, source_uid, target_uid):
        params = {
            'v': '5.92',
            'source_uid': source_uid,
            'target_uid': target_uid,
            'access_token': self.token
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.text

user = User(TOKEN)
print(user.getMutual("1000", "2000"))
