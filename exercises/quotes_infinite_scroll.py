from parsel import Selector
import requests
import json
import time



headers = {'content-type': 'application/json'}
data = {"page": 2}
base_url = 'http://quotes.toscrape.com'

with open(f'exercises/quotes/quotes.txt', 'w') as file:        

    for page in range(1, 4):
        print(f'\n ____________page: {page}______________\n')
        
        response = requests.get(f'{base_url}/api/quotes', params={'page': page}, timeout=1)
        quotes = response.json()['quotes']

        file.write(f'\n ____________page: {page}______________\n')

        for quote in quotes:                            
            file.write(f'{quote["text"]} - {quote["author"]["name"]}\n')        
    