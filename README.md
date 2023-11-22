# Indeed_crawler

This repository contains a Python script designed for web scraping job data from Indeed. The code allows users to specify their search criteria by providing the desired Job title and Location.

## System Requirements
    
```python
Google Chrome: 119.0.6045.160 (64 bit) (cohort: Stable)
ChromeDriver: 119.0.6045.105 
```

👉 Find Chrome driver 119 [here](https://googlechromelabs.github.io/chrome-for-testing/).

**Note:** It is essential to use a Chrome Driver version that matches your Google Chrome browser. To check your browser version, navigate to `chrome://version` in your browser. Ensure compatibility by downloading the appropriate Chrome Driver version [here](https://chromedriver.chromium.org/downloads).

## How to Use

1. Clone this repository to your computer
```
git clone https://github.com/ThanhHung2112/Indeed_crawler
```
2. Move to the Folder
```
cd Indeed_crawler
```
3. Install denpendencie
```
pip install -r requirements.txt
```
4. Change `Job` and `Location` in this script, then run the code
```
if __name__ == "__main__":
    job_title = "Job"
    job_location = "Location"
    job_crawler = Job_craw(job_title, job_location) 
    job_crawler.Start_craw()
```
 Replace "Job" and "Location" with the desired job title and location in the script before running the code.
