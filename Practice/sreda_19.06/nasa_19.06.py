import requests
api_key = 'jWyy53Dwb5T6pe19FNkMcBleBrC1NNBa8350ZmsC'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'


response = requests.get(url)
   
if response.status_code == 200:
    data = response.json()
    print(f'Title: {data['title']}')
    print(f'Date: {data['date']}')
    print(f'URL: {data['url']}')
else:
    print('fail')

