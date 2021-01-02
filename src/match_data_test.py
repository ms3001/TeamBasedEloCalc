import pprint
import re #regular expression
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd

matchUrlList = ['https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3609773279/48333464?tab=overview',
                'https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3629408412/48333464?tab=overview',
                'https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3719763988/207962171?tab=overview']
            
usernametext = 'nikhil325'
passwordtext = 'manyupleasehelpme123'

def scraper(usernametext, passwordtext, matchUrl):
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
    gameConclusions = soup.find_all(class_ = "game-conclusion") 
    winner = 1 if (gameConclusions[0].get_text().strip() == 'VICTORY') else 2
    resultsList = []
    for first_result in range(5):
        resultsList.append(gameConclusions[0].get_text())
    for second_result in range(5):
        resultsList.append(gameConclusions[1].get_text())

    # duration
    duration = stats.find(id='binding-698')
    durationList = []
    for i in range(10):
        durationList.append(duration.get_text())

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

    # gold earned
    gold_earned = stats.find(id='grid-row-625')
    goldList = []
    for i in gold_earned:
        goldList.append(i.get_text()[:-1])
    goldList.pop(0)

    # picks and bans
    championsList = []
    for tag in soup.find_all(class_ = "champion-nameplate-icon"):
        championsList.append(list(tag.descendants)[1].get("data-rg-id"))
    picksList = championsList[-10:]
    bansList = championsList[5:10] + championsList[15:20]



    # master data table
    data = {'game_id':gameidList,
            'game_length':durationList,
            'player_name':playersList,
            'champion':picksList,
            'bans':bansList,
            'result':resultsList,
            'kda':kdaList,
            'total_damage_to_champions':dmgstringList,
            'gold_earned':goldList}

    # df = pd.DataFrame(data)
    return data

def main():
    dataList = []
    for url in matchUrlList:
        dataList.append(scraper(usernametext, passwordtext, url))
    for key, value in dataList[0].items():
        for i in range(1, len(dataList)):
            value.extend(dataList[i][key])
    df = pd.DataFrame(dataList[0])
    print(df)
    df.to_csv(r'C:\Users\vince\Documents\dataquest\match_data.csv')

if __name__ == "__main__":
  main()