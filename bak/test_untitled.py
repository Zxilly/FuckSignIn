# Generated by Selenium IDE
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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("http://yqjk.jgsu.edu.cn:8090/user/qdwcIndex?yaMap=7d92105fc9376b34e1cf55afb958d71e")
    self.driver.find_element(By.ID, "dcwj").click()
    self.driver.find_element(By.ID, "nl").click()
    self.driver.find_element(By.ID, "nl").send_keys("19")
    self.driver.find_element(By.ID, "lxdh").click()
    self.driver.find_element(By.ID, "lxdh").send_keys("17572693170")
    self.driver.find_element(By.CSS_SELECTOR, "#nextStep1 > .mui-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mui-input-row:nth-child(1) > .mui-input-row > .mui-radio:nth-child(2) > input").click()
    self.driver.find_element(By.ID, "address2").click()
    self.driver.find_element(By.ID, "address2").send_keys("江西农业大学")
    self.driver.find_element(By.ID, "fjjtgz2").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".mui-pciker-rule-ft").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mui-btn-blue").click()
    self.driver.find_element(By.ID, "fjczbc2").click()
    self.driver.find_element(By.ID, "fjczbc2").send_keys("T123")
    self.driver.find_element(By.CSS_SELECTOR, "#nextStep2 > .mui-btn").click()
    self.driver.find_element(By.ID, "jrtw").click()
    self.driver.find_element(By.ID, "jrtw").send_keys("37")
    self.driver.find_element(By.CSS_SELECTOR, "#submit3 > .mui-btn").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
