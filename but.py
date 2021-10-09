from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe" # Location of the webdriver file

driver = webdriver.Chrome(PATH)
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
inputString = input("Enter message to send: ")
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
