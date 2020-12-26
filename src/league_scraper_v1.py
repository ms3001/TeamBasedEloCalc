import pprint
import re #regular expression
import time
from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3710954943/207962171?tab=stats'
# URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
#page = requests.get(URL)

#if page.status_code == 200:
#    print('Success!')
#elif page.status_code == 404:
#    print('Not Found.')

usernametext = input("Username:")
passwordtext = input("Password:")

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3710954943/207962171")
signinbutton = browser.find_element_by_css_selector(".riotbar-account-action")
signinbutton.click()


username = browser.find_element_by_name("username")
username.clear();
#username.send_keys("BRODesuex")
username.send_keys(usernametext)

password = browser.find_element_by_name("password")
password.clear();
#password.send_keys("havefunbr0") #boost me please
password.send_keys(passwordtext)
#time.sleep(15)

submit = browser.find_element_by_css_selector(".mobile-button__submit")
submit.click()

time.sleep(10) #sleep while page loads

page_source = browser.page_source
soup = BeautifulSoup(page_source, 'html.parser')

browser.get("https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3695072658/207962171?tab=overview")
browser.get("https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3695072658/207962171?tab=overview")

#test print statements
#print(soup.prettify())
#print(soup.get_text())
#print("---------BREAK----------")

playersList = []
for tag in soup.find_all(class_ = "champion-col name"):
	playersList.append(tag.find('a').get_text())

gameConclusions = soup.find_all(class_ = "game-conclusion")
print(gameConclusions[0].get_text())
for player in playersList[:5]:
	print(player)
print(gameConclusions[1].get_text())
for player in playersList[5:]:
	print(player)

