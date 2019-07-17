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
       pwd = "omaha1234"
       username = "testuser"
       password = "omaha1234"
       date = "2019-03-10"


       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("https://omk2-msd.herokuapp.com/admin/login/?next=/admin/")
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


       #Adding a new User
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[1]/table/tbody/tr[8]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(username)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys(password)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys(password)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       elem = driver.find_element_by_id("id_last_login_0")
       elem.send_keys(date)
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"user_form\"]/div/fieldset[4]/div[1]/div/p/span[2]/a[1]")
       elem.click()
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Posted New Test User"


       # Deleting the last created User
       driver.get("https://omk2-msd.herokuapp.com/admin/attendance/user/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[5]/td[1]/input")
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
       assert "Deleted New Test User"


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
