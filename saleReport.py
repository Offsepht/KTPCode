from selenium import webdriver
import time
from datetime import datetime
from datetime import timedelta
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Get path of chromedriver and web report URL
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('http://172.18.44.241/servlet/reality/BUYERRPT/RW_ENTER_SALES_BUYER')

# delay till browser has loaded
time.sleep(2)


## Get begginning date of the month
StartDate = datetime.strftime(datetime.today().replace(day=1), "%m/%d/%Y")
DayOne = browser.find_element_by_xpath('/html/body/form/input[1]').clear()
DayOne = browser.find_element_by_xpath('/html/body/form/input[1]')
DayOne.send_keys(StartDate)
# DayOne.send_keys('01/01/2021')


## Get last yesterday's date
EndDate = datetime.strftime(datetime.today() - timedelta( days = 1), "%m/%d/%Y")
DayTwo = browser.find_element_by_xpath('/html/body/form/input[2]').clear()
DayTwo = browser.find_element_by_xpath('/html/body/form/input[2]')
DayTwo.send_keys(EndDate)
# DayTwo.send_keys('01/01/2021')


#Locate all xpath ID's of elements needed for form
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

SubmitRun = browser.find_element_by_xpath('/html/body/form/input[18]')
SubmitRun.click()

# time.sleep()

## let report run and wait till data has populated
browser.implicitly_wait(300)

## get the path to the .txt file report has exported
element = browser.find_element_by_xpath('/html/body/b[1]').text

#print(element)



browser.close()


# Format and save .txt file for new .xlsx sheet
df = pd.read_csv(element, "|")
df.to_excel('Jon Sale.xlsx', 'Sheet1')