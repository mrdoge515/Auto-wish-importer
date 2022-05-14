# Imports
import time
import subprocess, sys
import pyperclip as clipboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Config
ffProfilePath = r'yourPathHere'
waitTime = 20 # Change it depending on how often you import your wishes, beacause the more there are wishes between imports, the more time it takes. 20 seconds should be generally fine

# Running PowerShell script to get feedback link
ps = subprocess.Popen('powershell.exe -ExecutionPolicy Unrestricted -file "importer.ps1"', stdout=sys.stdout)
ps.communicate()
link = clipboard.paste()

# Using Firefox profile to save data
ffProfile = webdriver.FirefoxProfile(ffProfilePath)

# Starting webdriver to import wishes
browser = webdriver.Firefox(ffProfile)
browser.get("https://paimon.moe/wish/import")

# Finding box to paste link and pasting it
input = browser.find_element_by_tag_name('input')
input.send_keys(link)

# Finding import button and clicking it
buttonsList = browser.find_elements_by_xpath(f'//button')
selectedButton = buttonsList[10]
selectedButton.click()

# Waiting for paimon.moe to finish importing
time.sleep(waitTime)

# Finding save button and clicking it
buttonsList2 = browser.find_elements_by_xpath(f'//button')
selectedButton2 = buttonsList2[10]
selectedButton2.click()

# Waiting to make sure everything is saved and closing browser
time.sleep(3)
browser.close()