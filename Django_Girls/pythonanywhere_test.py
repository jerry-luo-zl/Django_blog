import requests
username = 'lzl'
token = '63d46700267d9a01796a032b4d614d6d3245cd94'
host = 'www.pythonanywhere.com'

response = requests.get(
    'https://{host}/api/v0/user/{username}/cpu/'.format(
        host=host, username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))