from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import pandas as pd

class Job_craw():
    def __init__(self, job_title, job_location):

        self.job_title = job_title
        self.job_location = job_location
        columns = ["title","date","company","company_link","location","type-salary","description"]
        self.df = pd.DataFrame(columns=columns)
        # self.df = pd.read_csv("job.csv")
        service = Service(executable_path='chromedriver.exe')
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--window-size=1920x1080")

        try:
            self.browser = Chrome(service=service, options=options)
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_popup(self):
        try:
            popup = self.browser.find_element(By.ID, "mosaic-desktopserpjapopup")
            if popup.is_displayed():
                close_button = self.browser.find_element(By.CLASS_NAME, "css-yi9ndv.e8ju0x51")
                close_button.click()
        except Exception as e:
            print(f"An error occurred while trying to close the popup: {e}")

    def Start_craw(self):
        
        print("Starting")
        n = 0
        self.browser.get("https://jobs.vn.indeed.com/jobs?q={}&l={}".format(self.job_title, self.job_location))
        
        wait = WebDriverWait(self.browser, 100)  

        while True:
            sleep(random.randint(1,3))
            try:
                cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job_seen_beacon')))
                date = self.browser.find_elements(By.CLASS_NAME, 'date')
                print(len(cards))
                for i,card in enumerate(cards):
                    cards[i].click()
                    title = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobsearch-JobInfoHeader-title')))[0].text
                    print(title)
                    try:
                        company = self.browser.find_element(By.CLASS_NAME, 'css-1cjkto6')
                        # print(company.text)
                        try:
                            company_link = company.find_element(By.TAG_NAME, 'a').get_attribute('href')
                            # print(company_link)

                        except: company_link = None
                    except: company=None

                    try:
                        location = self.browser.find_element(By.CLASS_NAME, 'css-ks9svk').text
                    except:
                        try:
                            location = self.browser.find_element(By.CLASS_NAME, 'css-9yl11a').text 
                        except:
                            try:
                                location = self.browser.find_element(By.CLASS_NAME, 'css-6z8o9s').text
                            except: location = None
                    # print(location)

                    try:
                        type = self.browser.find_element(By.CLASS_NAME, 'css-k5flys').text 
                    except:
                        type = None
                    description = self.browser.find_element(By.ID, 'jobDescriptionText').text 
                    # print(description)
                    sleep(random.randint(1,5))

                    data = [title, date[i].text, company.text, company_link, location, type, description]
                    new_row = pd.DataFrame([data], columns=self.df.columns)
                    self.df = pd.concat([self.df, new_row], ignore_index=True)
                try:
                    next_button = self.browser.find_element(By.XPATH, '//a[@aria-label="Next Page"]')
                    next_button.click()
                except Exception:   
                    self.browser.quit()
                    break
            except: 
                self.close_popup()
        print("================================")
        print("Save results")

        
        self.df.to_csv("job_{}_{}.csv".format(self.job_title, self.job_location))

        return
    
if __name__ == "__main__":
    job_title = "Your Job Title"
    job_location = "Your Location"
    job_crawler = Job_craw(job_title, job_location) 
    job_crawler.Start_craw()
