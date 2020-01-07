### IMPORTS ###
import time
import datetime
import os
from time import sleep
import selenium
import random
import sys
import pytz
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

###----------------------------------------------------------------###

browser = webdriver.Chrome()
action = ActionChains(browser)
perspectivetime = datetime.datetime.now()
targetstart = perspectivetime.replace(hour=9, minute=59, second=59, microsecond=0)

print datetime.datetime.time(datetime.datetime.now())
print 'BOT COMMENCED'


### TYPING SIM ###
slow_typing_speed = 35
fast_typing_speed = 70
def slow_type(x):
	y = len(x)
	n=0
	while n<y:
		action.reset_actions()
		action.send_keys(x[n]).perform()
		n = n+1
		time.sleep(random.random()*10.0/slow_typing_speed)
def fast_type(x):
	y = len(x)
	n=0
	while n<y:
		action.reset_actions()
		action.send_keys(x[n]).perform()
		n = n+1
		time.sleep(random.random()*10.0/fast_typing_speed)

### INTERACTION TOOL ###
def fktype(txtbox, info, step):
	action.reset_actions()
	action.click(on_element=txtbox).perform()
	slow_type(info)
	print step
def ffktype(txtbox, info, step):
	action.reset_actions()
	action.click(on_element=txtbox).perform()
	fast_type(info)
	print step
def doubleclickfktype(txtbox, info, step):
	action.reset_actions()
	action.double_click(on_element=txtbox).perform()
	slow_type(info)
	print step
def press(button, step):
	action.reset_actions()
	action.click(button).perform()
	print step
def dpress(button, step):
	action.reset_actions()
	action.double_click(button).perform()
	print step
def optionfill(target, desired):
	action.reset_actions()
	el = browser.find_element_by_id(target)
	for option in el.find_elements_by_tag_name('option'):
	    if option.text == desired:
	        option.click()
	        break
	#browser.find_element_by_xpath("//select[@name=%s]/option[text()=%s]" % (target, option)).click().perform()

### WAITING TOOL ###
def delay_until(start):
	while start > datetime.datetime.now():
		time.sleep(0.25)
### Formatting Tool ###
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

### PERSONAL INFO ###
Name = ''
Address = ''
ZIP = ''
City = ''
Phone = ''
Email = ''
Fakecard = '00000012456'
FakeCVV = '789'
Card = ''
CVV = ''
ExpMon = ''
ExpYear = ''

ActivateWait = raw_input('Would you like to use the waiting tool? (y/n)').lower()
if ActivateWait in ("y","yes"):
	ActWait = True
	print color.BOLD + color.GREEN + 'Using Waiting Tool' + color.END
else:
	ActWait = False
	print color.BOLD + color.RED + 'Not Using Waiting Tool' + color.END

print color.BOLD + color.RED + 'Login to Gmail' + color.END
browser.get('https://www.gmail.com')
action.send_keys(Email).perform()
raw_input("Press Enter to continue...")


browser.get('https://www.supremenewyork.com/shop/all/accessories')

time.sleep(2)

press(browser.find_element_by_partial_link_text('Boxer Briefs'), '')
time.sleep(1)
press(browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input'), '')
time.sleep(2)
browser.get('https://www.supremenewyork.com/checkout')

print color.UNDERLINE + color.BLUE + 'Safety Item Added to Cart. Checking out.' + color.END
time.sleep(0.1)

fktype(browser.find_element_by_xpath('//*[@id="order_billing_name"]'), Name, '1.Name')
fktype(browser.find_element_by_xpath('//*[@id="order_email"]'), Email, '2.Email')
fktype(browser.find_element_by_xpath('//*[@id="order_tel"]'), Phone, '3.Phone Number')
fktype(browser.find_element_by_xpath('//*[@id="bo"]'), Address, '4.Address')
fktype(browser.find_element_by_xpath('//*[@id="order_billing_zip"]'), ZIP, '5.ZIP Code')
time.sleep(1)
press(browser.find_element_by_xpath('//*[@id="store_address"]'), '6.Save Address')
fktype(browser.find_element_by_xpath('//*[@id="nnaerb"]'), Fakecard, '7.Fake Card Number')
fktype(browser.find_element_by_xpath('//*[@id="orcer"]'), FakeCVV, '8.Fake Card CVV')
press(browser.find_element_by_xpath('//*[@id="order_terms"]'), '9.Accept Terms')
doubleclickfktype(browser.find_element_by_xpath('//*[@id="order_billing_city"]'), City, '10.City Name')
press(browser.find_element_by_xpath('//*[@id="pay"]/input'), '11.Processing')

time.sleep(1.5)

raw_input("Press Enter to continue...(in case hit by Captcha)")

time.sleep(0.5)

print color.BOLD + color.GREEN + '[Confirmed]:Info Saved' + color.END

browser.get('https://www.supremenewyork.com/shop/cart')
press(browser.find_element_by_xpath('//*[@id="item_53642"]/td[4]/form/button'), 'Removed item')
time.sleep(0.5)

if ActWait == True:
	CaptchaTime = perspectivetime.replace(hour=9, minute=58, second=0, microsecond=0)
	delay_until(CaptchaTime)

Time2Go = False

if targetstart < datetime.datetime.now() or ActWait == False:
	SkipAntiCaptcha = True
else:
	SkipAntiCaptcha = False

if SkipAntiCaptcha == True:
	print 'skipping anti captcha'
else:
	browser.get('http://login.wordpress.org/register')
	time.sleep(2)
	fktype(browser.find_element_by_xpath('//*[@id="user_login"]'), 'BLAHBLAH', 'Wordpress login')
	fktype(browser.find_element_by_xpath('//*[@id="user_email"]'), 'BLAHBLAH@.com', 'Wordpress email')

	action.reset_actions()
	Wordpress_confirm = browser.find_element_by_xpath('//*[@id="wp-submit"]')
	action.click(Wordpress_confirm).perform()

delay_until(targetstart)

browser.get('https://www.supremenewyork.com/shop/new')
print color.BOLD + color.GREEN + 'WAITING FOR ITEM SELECTION' + color.END
wait = WebDriverWait(browser, 10)
wait.until(EC.url_changes("https://www.supremenewyork.com/shop/new"))
time.sleep(0.25)
wait.until(EC.url_changes(browser.current_url))
