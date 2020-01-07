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

# open/use new browser
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
#Search for certain parameters

from selenium.webdriver.support.ui import WebDriverWait
#Wait for page to load

from selenium.webdriver.support import expected_conditions as EC
#Specify what you are looking for on a specific page in order to determine that the webpage has loaded.

###----------------------------------------------------------------###

def Automatic():
	bot_start_time = time.time()
	print datetime.datetime.time(datetime.datetime.now())
	print 'BOT COMMENCED'

	browser = webdriver.Chrome()
	action = ActionChains(browser)

	global itemslist
	itemslist = {}
	global itemssizes
	itemssizes = {}
	global itemscat
	itemscat = {}
	global itemscol
	itemscol = {}
	global NotAgain
	NotAgain = {}

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
	Name = '[NAME]'
	Address = '[ADDRESS]'
	ZIP = '[ZIP CODE]'
	City = '[CITY]'
	Phone = '[PHONE NUMBER]'
	Email = '[EMAIL]'
	Fakecard = '00000012456'
	FakeCVV = '789'
	Card = '[CARD NUMBER]'
	CVV = '[CARD CVV]'
	ExpMon = '[EXP MONTH]'
	ExpYear = '[EXP YEAR]'

	### ITEM SAVER ###
	def itemsaveprotocol():
		NoMoItems = False
		Kn = 0
		while NoMoItems == False:
			Kn = Kn+1
			Knstr = str(Kn)
			ItemInfo = raw_input( "Info for Item #" + Knstr + ": ").lower()
			try:
				if ItemInfo in ('d','done'):
					NoMoItems = True
					Kn = Kn-1
				else:
					global Keyword
					global Colour
					global Size
					global Category
					Keyword,Colour,Size,Category = ItemInfo.split(",")
					Keyword = Keyword.title()
					Colour = Colour.title()
					print Keyword + "," + Colour
					usr_item_verif = "Item with keywords: " + color.BOLD + Keyword + ", " + Colour + color.END + " stored, getting in size: " + color.BOLD + Size + color.END + "."
					if Size == 's':
						Size = 'Small'
						print usr_item_verif
						itemsave(Kn)
					elif Size == 'm':
						Size = 'Medium'
						print usr_item_verif
						itemsave(Kn)
					elif Size == 'l':
						Size = 'Large'
						print usr_item_verif
						itemsave(Kn)
					elif Size == 'xl':
						Size = 'XLarge'
						print usr_item_verif
						itemsave(Kn)
					elif Size == 'na':
						Size = 'NA'
						print usr_item_verif
						itemsave(Kn)
					elif int(Size) in (30,32,34,36):
						Size = str(Size)
						print usr_item_verif
						itemsave(Kn)
					else:
						print "Incorrect size. Try again."
						Kn = Kn-1
			except ValueError:
				print "Incorrect formatting. Try again."
				Kn = Kn-1
		else:
			print color.UNDERLINE + color.BOLD + color.RED + 'ALL ITEM KEYWORDS ENTERED' + color.END
			global Num_Items
			Num_Items = Kn
			print str(Num_Items) + ' items'
			print itemslist
			print itemscol
			print itemssizes

	def itemsave(num):
		itemnum = 'item' + str(num)
		itemslist[itemnum] = Keyword
		itemscol[itemnum] = Colour
		itemssizes[itemnum] = Size
		itemscat[itemnum] = Category

	def common_elements(list1, list2):
		return list(set(list1) & set(list2))


	### SETTING TARGET TIME ###
	perspectivetime = datetime.datetime.now()
	targetstart = perspectivetime.replace(hour=10, minute=59, second=50, microsecond=0)



	print color.UNDERLINE + color.BOLD + color.RED + 'Enter Items ("d" when done):' + color.END + color.UNDERLINE + color.CYAN + ' (Keywords,Colour,Size,Category)' + color.END
	print color.UNDERLINE + color.CYAN + 'Sizes: S/M/L/XL/na' + color.END
	itemsaveprotocol()


	ActivateWait = raw_input('Would you like to use the waiting tool? (y/n)').lower()
	if ActivateWait in ("y","yes"):
		ActWait = True
		print color.BOLD + color.GREEN + 'Using Waiting Tool' + color.END
	else:
		ActWait = False
		print color.BOLD + color.RED + 'Not Using Waiting Tool' + color.END

	print 'Let\'s go...'

	print color.BOLD + color.RED + 'Login to Gmail' + color.END
	browser.get('https://www.gmail.com')
	time.sleep(0.2)
	main_window = browser.current_window_handle
	browser.execute_script("window.open('');")
	browser.switch_to.window(browser.window_handles[1])
	timer_window = browser.current_window_handle
	browser.get('~/SupremeBot_Timer.html')
	browser.switch_to_window(main_window)
	action.send_keys(Email).perform()
	raw_input("Press Enter to continue...")

	print color.BOLD + color.RED + 'FIRING UP' + color.END

	#Supreme Info Saver
	print color.UNDERLINE + color.BLUE + 'Started Saving Info' + color.END
	start_save_info = time.time()
	start_safeitem_time = time.time()

	browser.get('https://www.supremenewyork.com/shop/all/accessories')

	time.sleep(2)

	STOP = False
	F = 0
	while STOP == False:
		try:
			press(browser.find_element_by_partial_link_text('White'), '')
			time.sleep(1)
			press(browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input'), '')
			time.sleep(2)
			browser.get('https://www.supremenewyork.com/checkout')
			end_safeitem_time = time.time()
			safe_item_time = end_safeitem_time - start_safeitem_time
			safe_item_time = "%.2f" % safe_item_time
			safe_item_time = str(safe_item_time)
			print safe_item_time
			STOP = True
		except:
			print color.UNDERLINE + color.RED + 'Safet Item SOLD OUT' + color.END
			Fail = 'item' + str(F)
			browser.get('https://www.supremenewyork.com/shop/all/accessories')
			NotAgain[Fail] = get_attribute('href')
			#NOT AT ALL FINISHED>>> Should create list like real item finder


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
	press(browser.find_element_by_xpath('//*[@id="item_59754"]/td[4]/form/button'), 'Removed item')
	time.sleep(0.5)

	end_save_info = time.time()

	#Anti Captcha
	print 'Prepare for anti-cactcha'

	if ActWait == True:
		CaptchaTime = perspectivetime.replace(hour=10, minute=58, second=0, microsecond=0)
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

	print color.BOLD + color.GREEN + 'It\'s 10. Supreme live any moment.' + color.END


	###SUPREME REAL DEAL

	z = 1
	T = 0
	SU = 0
	SO = 0
	skiptoend = False
	ASO = False

	while T < Num_Items:
		itemfound = False
		try:

			targetitem = 'item' + str(z)
			catpage = 'https://www.supremenewyork.com/shop/all/' + itemscat[targetitem]
			browser.get(catpage)
			print color.UNDERLINE + 'Looking for ' + itemslist[targetitem] + color.END

			PosItemTargs = browser.find_elements_by_partial_link_text(itemslist[targetitem])
			table1 = []
			for element in PosItemTargs:
					table1.append(element.get_attribute('href'))

			PosItemColTargs = browser.find_elements_by_partial_link_text(itemscol[targetitem])
			table2 = []
			for element in PosItemColTargs:
					table2.append(element.get_attribute('href'))

			CommonURL = common_elements(table1,table2)
			CommonURL = CommonURL[0]

			print color.BOLD + color.GREEN + 'Found' + color.END
			browser.get(CommonURL)
			itemfound = True
		except:
			print color.BOLD + color.RED + itemslist[targetitem] + ' not found. Refreshing...' + color.END
			time.sleep(0.25)
			browser.refresh()

		if itemfound == True:
			try:
				time.sleep(0.5)
				if itemssizes[targetitem] != 'NA':
					select = Select(driver.find_element_by_name('s'))
					select.select_by_visible_text(itemssizes[targetitem])
				time.sleep(0.25)
				press(browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input'), 'Added to cart')
				SU = SU + 1
			except:
				print color.RED + itemslist[targetitem] + ' SOLD OUT' + color.END
				SO = SO + 1
		T = SU + SO
		if T == SO:
			ASO = True

	if ASO == False:
		time.sleep(0.25)
		browser.get('https://www.supremenewyork.com/checkout')

		print color.UNDERLINE + color.BLUE + 'Item Added to Cart. Checking out.' + color.END

		time.sleep(0.5)
		ffktype(browser.find_element_by_xpath('//*[@id="nnaerb"]'), Card, '1.Card Number')
		ffktype(browser.find_element_by_xpath('//*[@id="orcer"]'), CVV, '2.Card CVV')
		optionfill('credit_card_month', ExpMon)
		optionfill('credit_card_year', ExpYear)
		press(browser.find_element_by_xpath('//*[@id="order_terms"]'), '4.Accept Terms')
		press(browser.find_element_by_xpath('//*[@id="pay"]/input'), '5.Processing')

		print color.BOLD + color.GREEN + 'ORDER COMPLETE' + color.END
	else:
		print color.BOLD + color.RED + 'ALL SOLD OUT' + color.END
	#CLEANUP

	bot_end_time = time.time()

	Total_time = bot_end_time - bot_start_time
	Total_time = "%.2f" % Total_time
	Total_time = str(Total_time)

	Save_info_time = end_save_info - start_save_info
	Save_info_time = "%.2f" % Save_info_time
	Save_info_time = str(Save_info_time)

	print '#######'
	print color.BOLD + color.PURPLE + 'SUMMARY' + color.END
	print 'Saving Info Time= ' + Save_info_time + ' seconds'
	print 'BOT TIME ACTIVE = ' + Total_time + ' seconds'
	print '#######'

	browser.quit()
