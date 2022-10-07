import requests as requests
from bs4 import BeautifulSoup

val = input()
# https://web.archive.org/web/20220310110507/https://www.imdb.com/title/tt0080684/
# val = 'https://web.archive.org/web/20220310110507/https://www.imdb.com/title/tt0080684/'
# val = 'https://www.imdb.com/name/nm0001191/'
response = requests.get(val, headers={'Accept-Language': 'en-US,en;q=0.5'} )

# jsonified_response = response.json()
# print(response.json())
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
p4 = soup.find('h1', { 'data-testid':"hero-title-block__title"})
p5 = soup.find('span',{'data-testid': 'plot-l'} )
if response.status_code != 200 or p4 is None or p5 is None:
    print("Invalid movie page!")
else:
    empty_dict = {"title": p4.text, "description": p5.text}
    print(empty_dict)
# p3 = soup.find_all('section')
# empty_dict = {"title": p4[0].text, "description": p5.text}
# print(empty_dict)
# print(p5)
# if response.status_code != 200 or not ("content" in response):
#     print("Invalid quote resource!")
# else:
#     print("hey")
    # print(jsonified_response.find("h1"))
    # print(response.json())