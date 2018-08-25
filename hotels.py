#This program runs the chromedriver and goes to hotels.com and inputs and searches for Dallas

import selenium
from selenium import webdriver

#Define the path to the chromedriver on the computer
path_to_chromedriver = '/mnt/c/Users/user/Downloads/chromedriver/chromedriver.exe'

#Creates a new webdriver
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#defines the URL that will be accessed
url = 'https://www.hotels.com'

#Opens the url in the chrome browser
browser.get(url)

#Finds the path to the destination search on the webpage
path = browser.find_element_by_xpath('//*[@id="qf-0q-destination"]')

#Enters Dallas as the searched destination
path.send_keys('Dallas')

#Acts as clicking enter on the keyboard
path.send_keys(Keys.ENTER)

#Closes the browser after completion, commeneted in order to show the results
# browser.close()
