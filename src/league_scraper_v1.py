import pprint
import re #regular expression
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def scrapeMatchHistoryUrl(usernametext, passwordtext, matchUrl):

	#options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get(matchUrl)
	signinbutton = browser.find_element_by_css_selector(".riotbar-account-action")
	signinbutton.click()


	username = browser.find_element_by_name("username")
	username.clear();
	username.send_keys(usernametext)

	password = browser.find_element_by_name("password")
	password.clear();
	password.send_keys(passwordtext)

	submit = browser.find_element_by_css_selector(".mobile-button__submit")
	submit.click()

	time.sleep(8) #sleep while page loads #TODO: better way to do this

	page_source = browser.page_source
	soup = BeautifulSoup(page_source, 'html.parser')

	browser.close()

	#test print statements
	#print(soup.prettify())
	#print(soup.get_text())
	#print("---------BREAK----------")

	playersList = []
	for tag in soup.find_all(class_ = "champion-col name"):
		playersList.append(tag.find('a').get_text().strip())

	gameConclusions = soup.find_all(class_ = "game-conclusion") #list with two values, DEFEAT and 
	winner = 1 if (gameConclusions[0].get_text().strip() == 'VICTORY') else 2

	#print game results
	#print(gameConclusions[0].get_text())
	#for player in playersList[:5]:
	#	print(player)
	#print(gameConclusions[1].get_text())
	#for player in playersList[5:]:
	#	print(player)

	resultList = [] #list
	resultList.append(winner) #resultList[0] = winner
	resultList.append(playersList) #resultList[1] = playersList (first 5 players are team 1)

	return resultList