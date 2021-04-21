from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd


# Get path of chromedriver and web report URL
PATH = """C:\Program Files (x86)\chromedriver.exe"""
driver = webdriver.Chrome(PATH)
driver.get('http://172.18.44.241/servlet/reality/SEARCH/RW_csi_onhand')
# driver.get('http://172.18.44.241/servlet/reality/SEARCH/CSI.ONHAND.1')
frame1 = driver.find_element_by_xpath('/html/frameset/frame[1]')
frame2 = driver.find_element_by_xpath('/html/frameset/frame[2]')


driver.switch_to.frame('BOTTOM')
#print(driver.find_element_by_xpath('/html/body/center/i/b').text)

time.sleep(1)
driver.switch_to.default_content()
driver.page_source
driver.switch_to.frame(frame1)

vendor = driver.find_element_by_xpath('/html/body/form/input[4]')
vendor.send_keys("C404")

SubmitRun = driver.find_element_by_xpath('/html/body/form/input[5]')
SubmitRun.click()

time.sleep(1)
driver.switch_to.default_content()
driver.page_source
driver.switch_to.frame('BOTTOM')
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))

allStyle = driver.find_element_by_xpath('/html/body/form/input[2]')
allStyle.click()


exportExcel = driver.find_element_by_xpath('/html/body/form/input[3]')
exportExcel.click()



submit2 = driver.find_element_by_xpath('/html/body/form/input[5]')
submit2.click()

driver.implicitly_wait(30)
element = driver.find_element_by_xpath('/html/body/b[2]').text


##### Close unneeded driver
driver.close()


# ####Format and save .txt file for new .xlsx sheet
my_cols = [str(i) for i in range(17)]
df = pd.read_csv(element, sep='\t', names=my_cols, header=None, engine='python')
df.to_excel('gooseInv.xlsx', 'Sheet1', header=None, index = False)

