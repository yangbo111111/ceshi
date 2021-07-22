import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('http://192.168.0.161:8000/flexoffice/web/dist/modules/login/login.html')
driver.find_element_by_name('username').send_keys('yangbo')
driver.find_element_by_id("password").send_keys('123qwe!')
driver.find_element_by_xpath("//*[@id='container']/div[3]/div/div[1]/div[2]/form/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main-navbar-collapse']/ul[1]/li[1]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main-menu-inner"]/ul/li/ul/li[2]/a/span').click()
time.sleep(3)
element = driver.find_element_by_id("cmsColumnTree_1_span")
ActionChains(driver).move_to_element(element).perform()
ActionChains(driver).context_click(element).perform()