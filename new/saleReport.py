
from selenium import webdriver
import time
from datetime import datetime
from datetime import timedelta
import pandas as pd
from selenium.webdriver.support import expected_condition as EC



PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get('file:///C:/Users/Offsepht/Desktop/Python/new/new%203.html')

time.sleep(1)

StartDate = datetime.strftime(datetime.today().replace(day=1), "%m/%d/%Y")
DayOne = browser.find_element_by_xpath('/html/body/form/input[1]').clear()
DayOne = browser.find_element_by_xpath('/html/body/form/input[1]')
DayOne.send_keys(StartDate)



EndDate = datetime.strftime(datetime.today() - timedelta( days = 1), "%m/%d/%Y")
DayTwo = browser.find_element_by_xpath('/html/body/form/input[2]').clear()
DayTwo = browser.find_element_by_xpath('/html/body/form/input[2]')
DayTwo.send_keys(EndDate)

Buyer = browser.find_element_by_xpath('/html/body/form/select/option[13]')
Buyer.click()

WebSale = browser.find_element_by_xpath('/html/body/form/input[3]')
WebSale.click()

ExportExcel = browser.find_element_by_xpath('/html/body/form/input[5]')
ExportExcel.click()

SelectClass = browser.find_element_by_xpath('/html/body/form/input[11]')
SelectClass.click()

SelectOrder = browser.find_element_by_xpath('/html/body/form/input[16]')
SelectOrder.click()

# SubmitRun = browser.find_element_by_xpath('/html/body/form/input[18]')
# SubmitRun.click()


browser.implicitly_wait(300)

excelPath = browser.find_element_by_xpath('/html/body/b[1]')

browser.close()



df = pd.read_txt(excelPath)
df.to_excel('Jon Sale.xlsx', 'Sheet1')



