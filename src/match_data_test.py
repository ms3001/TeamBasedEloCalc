import pprint
import re #regular expression
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd

matchUrl = 'https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3717600649/38863171?tab=stats'
usernametext = 'vwu1111'
passwordtext = ''

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(matchUrl)
signinbutton = browser.find_element_by_css_selector(".riotbar-account-action")
signinbutton.click()

username = browser.find_element_by_name("username")
username.clear()
username.send_keys(usernametext)

password = browser.find_element_by_name("password")
password.clear()
password.send_keys(passwordtext)

submit = browser.find_element_by_css_selector(".mobile-button__submit")
submit.click()

time.sleep(8)

page_source = browser.page_source
soup = BeautifulSoup(page_source, 'html.parser')

browser.close()

stats = soup.find(id='main')

# game id
game_id = matchUrl.split("/")[6]
gameidList = []
for i in range(10):
    gameidList.append(game_id)

# players
playersList = []
for tag in soup.find_all(class_ = "champion-col name"):
	playersList.append(tag.find('a').get_text().strip())

# result
gameConclusions = soup.find_all(class_ = "game-conclusion") #list with two values 
winner = 1 if (gameConclusions[0].get_text().strip() == 'VICTORY') else 2
resultsList = []
for first_result in range(5):
    resultsList.append(gameConclusions[0].get_text())
for second_result in range(5):
    resultsList.append(gameConclusions[1].get_text())

# kda
kda = stats.find(id='grid-row-309')
kdaList = []
for i in kda:
    kdaList.append(i.get_text())
kdaList.pop(0)

# total damage to champions
total_damage_to_champions = stats.find(id='grid-row-362')
dmgstringList = []
for i in total_damage_to_champions:
    dmgstringList.append(i.get_text()[:-1])
dmgstringList.pop(0)

# picks
picksList = []
for tag in soup.find_all(class_ = "champion-nameplate-icon"):
    # for i in tag.descendants:
    print(list(tag.descendants)[1].get("data-rg-id"))
    # print(tag.find_all())


# master data table
data = {'game_id':gameidList,
        'player_name':playersList,
        'result':resultsList,
        'kda':kdaList,
        'total_damage_to_champions':dmgstringList}

df = pd.DataFrame(data)
print(df)

df.to_csv(r'C:\Users\vince\Documents\dataquest\match_data.csv')