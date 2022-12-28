# Python program to demonstrate
# selenium
# import webdriver
from selenium import webdriver
import time

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys
import datetime
# create webdriver object


drupal_site_url = 'drupal site url (/user - must)'
user_name = 'user_name'
password = 'password'


print("\n\tProgram started !!!!")

def cache():
  firefox_options = Options()
  firefox_options.add_argument("--headless")
  driver = webdriver.Chrome(service=Service('/usr/local/bin/geckodriver'), options=firefox_options)

  driver.get(drupal_site_url)
  inputElement = driver.find_element("name", "name")
  inputElement.send_keys(user_name)

  inputElement = driver.find_element("name", "pass")
  inputElement.send_keys(password)

  time.sleep(2)

  driver.find_element('name','op').click()
  time.sleep(2)

  driver.find_element('id','toolbar-link-system-admin_config').click()
  time.sleep(2)

  driver.find_element("link text", "Performance").click()
  time.sleep(2)

  driver.find_element('id','edit-clear').click()
  time.sleep(2)
  print("\nCahe clear!") 

  driver.close()

  current_time = datetime.datetime.now()
  lines = ['Last Cahe clear - '+str(current_time)]
  with open('cahe_clear_list.txt', 'a') as f:
      for line in lines:
          f.write(line)
          f.write('\n')

for i in range(99999999999999999):
  try:
    cache()
  except:
    print("\n\tAn exception occurred \n \t Restarting the function ")
    time.sleep(2)
    cache()