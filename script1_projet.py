from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import time

#Connexion au webdriver
browser = webdriver.Chrome('C:/Users/melis/chromedriver_win32/chromedriver')
browser.get('https://fr.shopping.rakuten.com/')
time.sleep(2)

#Agrandir la fenêtre 
browser.maximize_window()
time.sleep(2)

#Accepter les cookies
cookies = browser.find_element('xpath', '//*[@id="didomi-notice"]/div/div[2]/div[1]/span')
time.sleep(2)
cookies.click()
time.sleep(2)
categories = browser.find_element('xpath', '//*[@id="header"]/div/div/div/header/div[2]/nav/div[1]')
time.sleep(2)
categories.click()
time.sleep(2)

def scroll_to(x): 
    ActionChains(browser).scroll_to_element(x).perform()

deals = browser.get('https://fr.shopping.rakuten.com/event/rakuten-deals#xtatc=PUB-[fonc]-[Header]-[Rakuten-Deals]-[ToutUnivers]-[]-[]-[]')
time.sleep(2)
promos = browser.find_element('xpath', '//*[@id="stickyTabContainer"]/div/a[2]')
time.sleep(2)
promos.click()
time.sleep(2)
x = browser.find_element(By.XPATH,'//*[@id="jahiaContent"]/section[2]')
scroll_to(x)
seeAll = browser.find_element('xpath', '//*[@id="flux1"]/div/div[2]/div')
time.sleep(1)
seeAll.click()
time.sleep(1)
x = browser.find_element(By.XPATH,'//*[@id="jahiaContent"]/section[2]')
scroll_to(x)
seeAll = browser.find_element('xpath', '//*[@id="flux1"]/div/div[2]/div')
time.sleep(1)
seeAll.click()
time.sleep(1)
x = browser.find_element(By.XPATH,'//*[@id="jahiaContent"]/section[2]')
scroll_to(x)
seeAll = browser.find_element('xpath', '//*[@id="flux1"]/div/div[2]/div')
time.sleep(1)
x = browser.find_element(By.XPATH,'//*[@id="stickyTabContainer"]/div')
scroll_to(x)
time.sleep(4)
seeAll.click()


articles_element = browser.find_element('xpath', '//*[@id="flux1"]/div/div/div')

# Définir le pas de scrolling à 500 pixels
scroll_step = 500
last_count = 0

# Scroller par pas de 500 pixels et récupérer les articles affichés à chaque fois
while True:
    # Scroller de 500 pixels vers le bas
    browser.execute_script(f"window.scrollBy(0, {scroll_step});")
    # Récupérer les articles affichés dans la page actuelle
    articles = browser.find_elements(By.CLASS_NAME,"flux-promo-item-link-large_device")
    nom_classes = []
    for article in articles:
        div_elements = article.find_elements('xpath','./div')
        if(len(div_elements) > 1):
            for div_element in div_elements:
                classes = div_element.get_attribute('class')
                mes_classes = classes.split()
                first_classe = mes_classes[0]
                nom_classes.append(first_classe)
                
    nom_classes = list(set(nom_classes))
    avantages=[]
    titles=[]
    prices=[]
    others=[]
    categories = []
    for classe in nom_classes:
        contents = browser.find_elements(By.CLASS_NAME, classe)
        if "clubR" in classe:
            for content in contents:
                avantages.append(content.text)
        elif "blocPrice" in classe:
            for content in contents:
                prices.append(content.text)

        elif "item-description" in classe:
            for content in contents:
                titles.append(content.text)
        elif "sticker" in classe:
            for content in contents:
                categories.append(content.text)
        else:
            for content in contents:
                others.append(content.text)

    print(len(titles))
    print(len(avantages))
    print(len(prices))
    # Sortir de la boucle si tous les articles ont été récupérés
    if len(articles) == last_count:
        break
    # Mettre à jour le dernier nombre d'articles récupérés
    last_count = len(articles)



print(len(articles))
[article.text for article in articles]



def create_article(i):
    return {'title': titles[i], 'price': prices[i], 'category': categories[i], 'advantages_clubR': avantages[i]}


browser.quit()