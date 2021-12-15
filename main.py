from selenium import webdriver 
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager


from fbchat import Client 
username = 'tranlamphong7504@gmail.com'
password = 'mitCollege123'


driver = webdriver.Chrome(executable_path='C:/chromedriver')
driver.get('https://www.facebook.com')


txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)

txtPassword = driver.find_element_by_id('pass')
txtPassword.send_keys(password)

btnlogin = driver.find_element_by_name('login')
btnlogin.submit()

friend = Client.searchForUsers('Khoa Tran')
friend2 = 'Khoa Tran'
msg = 'Ngủ ngon nha '
sent = client.send(fbchat.models.Message(msg),friend2.uid)

if sent:
  print('sent to Khoa Tran')
else :
 print('error'
 )