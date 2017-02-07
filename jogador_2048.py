#!/usr/bin/python
#--coding:utf8--

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

jogo = "http://gabrielecirulli.github.io/2048/"
browser = webdriver.Firefox()
browser.get(jogo)
caixa = browser.find_element_by_class_name("game-container")
game = browser.find_element_by_class_name("retry-button")

while game.is_displayed() == False:

    caixa.send_keys(Keys.UP)
    caixa.send_keys(Keys.RIGTH)
    caixa.send_keys(Keys.DOWN)
    caixa.send_keys(Keys.LEFT)

print("Voce perdeu!")
