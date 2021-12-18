from selenium import webdriver
import time


chave = input("Digite a Chave:")

driver = webdriver.Chrome()
driver.get('https://www.fsist.com.br/')
driver.set_window_size(1024,768)
print(driver.get_window_size())
driver.maximize_window()
print(driver.get_window_size())

driver.find_element_by_id("chave").send_keys(chave)
driver.find_element_by_xpath('//*[@id="msgok"]').click()
driver.find_element_by_xpath('//*[@id="butconsulta"]/a/div/span').click()
driver.find_element_by_xpath('/html/body/div[6]/div[1]/a[1]').click()
driver.find_element_by_xpath('/html/body/div[7]/div[1]/a[1]').click()

