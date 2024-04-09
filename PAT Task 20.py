import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class cowin:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def fetch_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title

    def close(self):
        self.driver.close()
    def click_faq(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='FAQ']").click()
    def click_partner(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Partners']").click()



if __name__ == "__main__":
    Cowin = cowin("https://www.cowin.gov.in/")
    Cowin.start()
    print(Cowin.fetch_url())
    time.sleep(3)
    Cowin.click_faq()
    print(Cowin.title())
    time.sleep(3)
    Cowin.click_partner()
    time.sleep(3)
    print(Cowin.title())




