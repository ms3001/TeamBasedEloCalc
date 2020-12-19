import requests
import pprint
from bs4 import BeautifulSoup
from getpass import getpass

URL = 'https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3700380075/213681463?tab=stats'
# URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
page = requests.get(URL)

if page.status_code == 200:
    print('Success!')
elif page.status_code == 404:
    print('Not Found.')

#u will get a merge conflict

# beautiful soup object that takes html content earlier as input
# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find(id='main')
# print(soup.prettify())
# job_elems = results.find_all('section', class_='card-content')
# title_elem = soup.find('div', class_='grid-cell-298')
# print(title_elem)


# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()

#u will get another merge conflict

# python_jobs = results.find_all('h2', string=lambda text: 'japan' in text.lower())
# for p_job in python_jobs:
#     link = p_job.find('a')['href']
#     print(p_job.text.strip())
#     print(f"Apply here: {link}\n")

# allo