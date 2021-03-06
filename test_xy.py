from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


print "This is for Redmi 3S prime from Flipkart"
print time.ctime()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


for val in range(1,2):
	val = str(val)
	driver.get('https://www.flipkart.com/redmi-3s-prime-gold-32-gb/product-reviews/itmehbejabfb46rg?page='+val+'&pid=MOBEKWZYSHHJNWGZ')
	if(val == '1'):
		#Click element for the Certified Users
		driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[5]/div').click()
	#Loop for the elements in the page
	for item in range(1,11):
		item = str(item)
		try:
			#checking the presence of date element
			date = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div['+item+']/div/div/div[3]/div[1]/div/p[3]')
		except Exception:
			print "Review date elements not populated\t" + str(time.ctime())
			time.sleep(20)
			driver.refresh()
			time.sleep(5)
		try:
			#checking for the "Read more button"
			but = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div['+item+']/div/div/div[2]/div/span/span/span')
		except Exception:
			print "Some error in finding the read more button\t" + str(time.ctime())
			pass
		try:
			para = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div['+item+']/div/div/div[2]/div/div')
		except Exception:
			print "Review elements not found for: " +val+ " page \t" + str(time.ctime())
			pass
		try:
			but.click()
		except Exception:
			pass
		try:
			if(len(date.text)>1):
				with open('reveiw.txt','a') as file1:
					file1.write(para.text+'\r\n')
				with open('date.txt','a') as file2:
					file2.write(date.text+'\r\n')
			else:
				print "Some problem here at row: " +str(row) + str(time.ctime())
		except Exception:
			pass
	print "End of page: "+val
driver.quit()
print "Done" 
print time.ctime()	