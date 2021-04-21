from selenium import webdriver
import time
import urllib.request

chrome_browser= webdriver.Chrome(executable_path=r'C:\Users\Suprakash\Anaconda3\chromedriver')
url1='https://www.instagram.com/'
#user_handle=input('Enter the user handle : ')
user_handle="marvelstudios" # Mention the user handle
url=url1+user_handle

try: # This block will execute if the user handle is correct
	chrome_browser.get(url)

	fileName = user_handle + '.jpg'
	try:
		#For public accounts
		image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img')
	except:
		#For private accounts
		image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/div/button/img')
	imageSrc=image.get_attribute('src')
	urllib.request.urlretrieve(imageSrc,fileName)

	print("Image downloaded successfully")

except: #Incase the user handle is incorrect it will show this message
	print("Sorry this intagram handle doesn't exist")

chrome_browser.quit()

