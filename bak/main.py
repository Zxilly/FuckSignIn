#Fuck Bureaucracy

import time

from selenium import webdriver

loginname = ''
password = ''
age = 19
phonenum = ''
address = ''
temp = 37

browser = webdriver.Chrome()

#载入页面
browser.get(url='http://yqjk.jgsu.edu.cn:8090/index')
time.sleep(1)

#登录
browser.find_element_by_css_selector('#loginName').send_keys(loginname)
browser.find_element_by_css_selector('#yzxx').send_keys(password)
browser.find_element_by_css_selector('#qdtj').click()
time.sleep(2)

#每日签到流程

browser.find_element_by_css_selector('#wyqd').click()
time.sleep(1)

browser.find_element_by_css_selector('#goToSigin').click()
time.sleep(1)

browser.execute_script('dzdwok();') #位置正确
time.sleep(1)
browser.execute_script("qd('0','');")
time.sleep(1)

#调查问卷流程
'''
browser.get(url='http://yqjk.jgsu.edu.cn:8090/public/qdwcIndex')
time.sleep(2)
#browser.find_element_by_css_selector('#dcwj').click
browser.execute_script('dcwjtbBb2();')
time.sleep(2)
browser.find_element_by_css_selector('#nl').send_keys(age)
browser.find_element_by_css_selector('#lxdh').send_keys(phonenum)
browser.find_element_by_css_selector('#nextStep1 > .mui-btn').click()
browser.find_element_by_css_selector('.mui-input-row:nth-child(1) > .mui-input-row > .mui-radio:nth-child(2) > input').click()
browser.find_element_by_css_selector('#address2').send_keys(address)
browser.find_element_by_css_selector('#fjjtgz2').click()
browser.execute_script('window.scrollTo(0,0)')
browser.find_element_by_xpath('//body/div[2]/div[2]/div/div/div').click()
time.sleep(2)
browser.find_element_by_css_selector('body > div.mui-poppicker.mui-active > div.mui-poppicker-header > button.mui-btn.mui-btn-blue.mui-poppicker-btn-ok').click()
browser.find_element_by_css_selector('#fjczbc2').send_keys('T123')
browser.find_element_by_css_selector('#nextStep2 > .mui-btn').click()
browser.find_element_by_css_selector('#jrtw').send_keys(temp)
browser.find_element_by_css_selector('#submit3 > .mui-btn').click()
'''





time.sleep(5)
browser.close()
