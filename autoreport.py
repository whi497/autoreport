from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import zmail
import argparse
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
def my_mail(status):
    success_content = {
    'subject':'health report Success',#主题
    'content':'mail report from vlab',#邮件内容
    }
    fail_content = {
    'subject':'health report Fail',#主题
    'content':'mail fram vlab',#邮件内容
    }
    server = zmail.server('wh030917@163.com','DAREGCNILDMDCFWL')
    if status == True:
        server.send_mail('1624745389@qq.com',success_content)
    else:
        server.send_mail('1624745389@qq.com',fail_content)

class Report(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(options=chrome_options, executable_path="/usr/bin/chromedriver")
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
        count = 5;
        try:
            self.login()
            self.driver.find_element_by_id("report-submit-btn-a24").click() 
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
        except Exception as i:
            if count == 0:
                my_mail(False)
                exit(-1)
            else:
                i = self.autoreport()
            count -= 1
        my_mail(True)
        print('success!')
        self.driver.close()


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='URC nCov auto report script.')
        parser.add_argument('username', help='your username', type=str)
        parser.add_argument('password', help='your CAS password', type=str)
        args = parser.parse_args()
        reporter = Report(username=args.username, password=args.password)
        reporter.autoreport()
        exit(0)
    except Exception as i:
        my_mail(False)





