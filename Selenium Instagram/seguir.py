from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from time import sleep
from random import randint

driver = webdriver.Chrome("C:/Users/Jocker/Downloads/chromedriver.exe")
driver.implicitly_wait(30)
driver.get('https://www.instagram.com/')
driver.find_element_by_name("username").click()
driver.find_element_by_name('username').send_keys('ocarinhadeti')
sleep(3)
driver.find_element_by_name("password").click()
driver.find_element_by_name('password').send_keys('SUA SENHA AQUI')
sleep(3)
t = driver.find_elements_by_tag_name("button")
t[1].click()
sleep(3)
driver.get('https://www.instagram.com/SEUPERFIL')
sleep(3)
itens = driver.find_elements_by_class_name("Y8-fY ")
itens[2].click()
sleep(3)

seguir = driver.find_elements_by_css_selector('button')
sleep(3)
c = 0
for x in seguir:
    try:
        if x.text == "Seguir":
            print("Achou o botão seguir")
            x.click()
            tempo = randint(1, 30)
            print("Esperando {} segundos".format(tempo))
            sleep(tempo)
            c += 1

    except: print("Botão errado!")
print("Seguiu {} pessoas".format(c))


'''
#sistema de sair da conta
driver.find_element_by_css_selector("img[alt='Foto do perfil de ocarinhadeti']").click()
sleep(3)
sair = driver.find_elements_by_css_selector('div[style*="height: 28px; width: 170px"]')
sair[4].click()
sleep(3)
'''