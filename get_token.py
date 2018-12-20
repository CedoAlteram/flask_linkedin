import requests


CLIENT_ID = ''
CLIENT_SECRET = ''

# api-endpoint
URL = \
    'https://www.linkedin.com/oauth/v2/accessToken?grant_type=client_credentials&client_id={0}&client_secret={1}'\
    .format(CLIENT_ID, CLIENT_SECRET)

print(URL)
r = requests.get(URL)
print(r.json())
