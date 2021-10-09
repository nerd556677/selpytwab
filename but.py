from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe" # Location of the webdriver file

driver = webdriver.Chrome(PATH)
driver.implicitly_wait(15) 
driver.get('https://www.web.whatsapp.com')
driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
inputString = input("Enter message to send: ")
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)

    
    
    def getJsonData(file, attr_ret, attr1, attr2, attr_val1, attr_val2):
     
    # Load the file's data in 'data' variable
    data = json.load(file)
    retv =[]
 
    # If the attributes' value conditions are satisfied,
    # append the name into the list to be returned.
    for i in data:
        if(i[attr1]== attr_val1 and i[attr2]== attr_val2):
           retv.append(i[attr_ret])
    return retv
