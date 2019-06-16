from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time




br=webdriver.Chrome()
br.get('https://web.whatsapp.com')
input()
search=br.find_element_by_tag_name('input')
time.sleep(10)
search.send_keys("9610633186",Keys.ENTER)
time.sleep(10)


y=br.find_element_by_class_name('_2y17h').click()
time.sleep(10)
while True:
    try:
        if ('online' in br.page_source):
            print('Online at ',time.asctime())


    except Exception as e:
        print(e)
        pass

    
