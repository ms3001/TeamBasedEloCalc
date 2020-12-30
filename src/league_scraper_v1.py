import pprint
import re #regular expression
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

def scrapeMatchHistoryUrl(usernametext, passwordtext, matchUrl):

	#options = webdriver.ChromeOptions()
	#options.add_argument('--headless') #TODO: see if headless possible
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

	delay = 30 #seconds
	try:
	    elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'game-conclusion')))
	    print("Page is ready!")
	except TimeoutException:
	    print("Loading took too much time!")

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

	resultList = []
	resultList.append(winner) #resultList[0] = winner
	resultList.append(playersList) #resultList[1] = playersList (first 5 players are team 1)

	return resultList

def scrapeMatchHistoryUrlList(usernametext, passwordtext, matchUrlList):

	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get(matchUrlList[0])

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

	delay = 30 #seconds
	#need a wait for login
	try:
	    elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'game-conclusion')))
	    print("Page is ready!")
	except TimeoutException:
	    print("Loading took too much time!")
	    exit()

	finalresultList = []
	gamenum = 0
	for url in matchUrlList:
		gamenum += 1
		print("Game " + str(gamenum) + " data")
		print("reading from: " + url)
		browser.get(url)

		delay = 10 #seconds
		for i in range(0,5): #try loading 5 times
			try:
				elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'game-conclusion')))
				print("Page is ready!")
				page_source = browser.page_source
				soup = BeautifulSoup(page_source, 'html.parser')
				tweethref = soup.find(class_="share-button tweet-button").get('href')
				while(url.split("/")[6] not in tweethref): #wait for page data to match URL
					time.sleep(1) #wait 1 second and retry if not loaded yet
					page_source = browser.page_source
					soup = BeautifulSoup(page_source, 'html.parser')
					tweethref = soup.find(class_="share-button tweet-button").get('href')
				break
			except TimeoutException:
				print("Loading took too much time!Reloading")
				browser.get(url)
			except AttributeError as error:
				print(error)
				print("tweet had not loaded? Reloading")
				browser.get(url)

		playersList = []
		for tag in soup.find_all(class_ = "champion-col name"):
			playersList.append(tag.find('a').get_text().strip())

		gameConclusions = soup.find_all(class_ = "game-conclusion") #list with two values, DEFEAT and 
		winner = 1 if (gameConclusions[0].get_text().strip() == 'VICTORY') else 2

		#print game results
		print(gameConclusions[0].get_text())
		for player in playersList[:5]:
			print(player)
		print(gameConclusions[1].get_text())
		for player in playersList[5:]:
			print(player)

		resultList = []
		resultList.append(winner) #resultList[0] = winner
		resultList.append(playersList) #resultList[1] = playersList (first 5 players are team 1)
		finalresultList.append(resultList)
	browser.close()
	return finalresultList


