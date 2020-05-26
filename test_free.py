import selenium
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

browser.get("https://freebitco.in/?op=home")

class TestFree():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_free(self):
    # Test name: free
    # Step # | name | target | value
    # 1 | open | /?op=home | 
    self.driver.get("https://freebitco.in/?op=home")
    # 2 | setWindowSize | 694x761 | 
    self.driver.set_window_size(694, 761)
    # 3 | click | id=free_play_form_button | 
    self.driver.find_element(By.ID, "free_play_form_button").click()
  
