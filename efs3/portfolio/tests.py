import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       #Pre-defined variables
       user = "instructor"
       pwd = "instructor1a"
       name = "test"
       address = "test"
       custno = "0000"
       city = "test"
       state = "test"
       zipcode = "00000"
       email = "test@test.com"
       cellphone = "0000000000"


       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("https://efs-danial.herokuapp.com/admin/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Logged In"


       #Adding a new Customer
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[last()]/table/tbody/tr[1]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address)
       elem = driver.find_element_by_id("id_cust_number")
       elem.send_keys(custno)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city)
       elem = driver.find_element_by_id("id_state")
       elem.send_keys(state)
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys(zipcode)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_cell_phone")
       elem.send_keys(cellphone)
       time.sleep(4)
       elem = driver.find_element_by_xpath("//*[@id=\"customer_form\"]/div/div/input[1]")
       elem.click()
       time.sleep(2)
       driver.get("https://efs-danial.herokuapp.com/customer_list")
       time.sleep(3)
       assert "Posted New Test Customer"


       #Deleting the last created Customer
       driver.get("https://efs-danial.herokuapp.com/admin/portfolio/customer/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[1]/td[1]/input")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select/option[2]")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/button")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]")
       elem.click()
       time.sleep(3)
       assert "Deleted New Test Customer"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
