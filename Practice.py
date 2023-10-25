from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service

# serv_obj = Service("/Users/ashutoshpal/Downloads/chromedriver_mac64")
# driver = webdriver.Chrome(serv_obj)
driver = webdriver.Safari()
driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.implicitly_wait(100)
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")

driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.implicitly_wait(100)
driver.find_element(By.XPATH, "//details//summary[text()='Table Data']").click()
data = [{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name":
"Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name":
"Jennifer", "age" : 42, "gender": "female"}]
driver.implicitly_wait(100)

driver.find_element(By.XPATH, "//textarea[@id='jsondata']").clear()
driver.find_element(By.ID, "jsondata").send_keys(data)
driver.find_element(By.XPATH, "//button[text()='Refresh Table']").click()
driver.implicitly_wait(100)

l1_name=driver.find_elements(By.XPATH, "//caption[text()='Dynamic Table']/..//tr//td[1]")
l2_age=driver.find_elements(By.XPATH, "//caption[text()='Dynamic Table']/..//tr//td[2]")
l3_gender=driver.find_elements(By.XPATH, "//caption[text()='Dynamic Table']/..//tr//td[3]")

actualOutput = []
for i in range(len(l1_name)):
    di = {}
    di['name']=l1_name[i].text
    di['age']=l2_age[i].text
    di['gender']=l3_gender[i].text
    actualOutput.append(di)

assert actualOutput==data
driver.close()
