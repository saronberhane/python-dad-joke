import requests
from colorama import init, Fore, Back

init()

response = requests.get(
    'https://icanhazdadjoke.com/',
    headers={'Accept': 'application/json'}
)

if response.status_code == 200:
    data = response.json()
    joke = data['joke']
    print(Back.BLACK + Fore.YELLOW + 'Your dad joke: {0}'.format(joke))
else:
    print('Failed to fetch dad joke.')

input("Press ENTER to continue!")
