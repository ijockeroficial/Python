from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from time import sleep

driver = webdriver.Chrome("C:/Users/Jocker/Downloads/chromedriver.exe")
driver.implicitly_wait(30)
driver.get('https://www.instagram.com/')
driver.find_element_by_name("username").click()
driver.find_element_by_name('username').send_keys('seuinstagram')
driver.find_element_by_name("password").click()
driver.find_element_by_name('password').send_keys('SUA SENHA AQUI')
t = driver.find_elements_by_tag_name("button")
t[1].click()
sleep(3)
driver.get('https://www.instagram.com/')
sleep(3)
driver.get('https://www.instagram.com/seuinstagram')
sleep(3)
seguir = driver.find_elements_by_tag_name("button")
seguir[1].click()
sleep(3)
driver.find_element_by_css_selector("img[alt='Foto do perfil de ocarinhadeti']").click()
sleep(3)
sair = driver.find_elements_by_css_selector('div[style*="height: 28px; width: 170px"]')
sair[4].click()
