from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import argparse
import time

class Report(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
    def login(self):
        #enter the page
        self.driver.get("https://weixine.ustc.edu.cn/2020/home")
        self.driver.find_element_by_class_name("btn").click()
        #login
        self.driver.implicitly_wait(10) # wait 10 seconds
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("login").click()
        WebDriverWait(driver=self.driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        
    def autoreport(self):
        self.login()
        # self.driver.find_element_by_id("report-submit-btn-a24").click() 
        #change the page
        self.driver.implicitly_wait(10) # wait 10 seconds
        self.driver.get("https://weixine.ustc.edu.cn/2020/apply/daliy")
        # self.driver.find_element_by_css_selector("input[type='radio'][value='3']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@type="checkbox"]').click()
        self.driver.get("https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3")
        # self.driver.find_element_by_id("report-submit-btn").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="daliy-report"]/form/div/div[4]/div/label[1]/i').click()
        self.driver.find_element_by_xpath('//*[@id="daliy-report"]/form/div/div[4]/div/label[2]/i').click()
        self.driver.find_element_by_xpath('//*[@id="daliy-report"]/form/div/div[4]/div/label[5]/i').click()
        self.driver.find_element_by_id("report-submit-btn").click()
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='URC nCov auto report script.')
    parser.add_argument('username', help='your username', type=str)
    parser.add_argument('password', help='your CAS password', type=str)
    args = parser.parse_args()
    reporter = Report(username=args.username, password=args.password)
    count = 5
    while count != 0:
        ret = reporter.autoreport()
        if ret != False:
            break
        print("Report Failed, retry...")
        count = count - 1
    if count != 0:
        exit(0)
    else:
        exit(-1)





