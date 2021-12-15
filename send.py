from selenium import webdriver 
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

import time 
from fbchat import Client 
username = 'tranlamphong7504@gmail.com'
password = 'mitCollege123'

#search facebook 
driver = webdriver.Chrome(executable_path='C:/chromedriver')
driver.get('https://www.facebook.com')

#login 

txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)

txtPassword = driver.find_element_by_id('pass')
txtPassword.send_keys(password)

btnlogin = driver.find_element_by_name('login')
btnlogin.submit()
driver.find_element_by_xpath(".//*[@id='u_0_h']/li[1]/div/a/span").click() 

#search for Khoa Tran 
# time.sleep(5)
# friend = 'Khoa Tran'
# search = driver.find_element_by_name('global_typeahead')
# search.send_keys(friend)



#click on the first account 
# time.sleep(5)
# first_account = driver.find_element_by_('a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7')
# first_account.click()





if sent:
  print('sent to Khoa Tran')
else :
 print('error'
 )