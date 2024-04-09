import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class Labour:

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

    def documents(self,driver):
        self.driver.ActionChains(driver)
        document = self.driver.find_element(By.XPATH, "(//a[@href='/annual-reports'])[1]")
        Reports = self.driver.find_element(By.XPATH, "//a[normalize-space()='Monthly Progress Report']")
        ActionChains(driver).move_to_element(document).perform()
        # ActionChains(driver).move_to_element(Reports).click()
        Reports.click()

if __name__ == "__main__":
    labour = Labour("https://labour.gov.in/")
    labour.start()
    time.sleep(10)
    labour.documents()
    time.sleep(5)

