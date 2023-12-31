# Indeed_crawler

This repository contains a Python script designed for web scraping job data from Indeed. The code allows users to specify their search criteria by providing the desired Job title and Location.

👉 You can find my datasets on [Kaggle](https://kaggle.com/datasets/leewanhung/indeed-job).

## System Requirements
    
```python
Google Chrome: 119.0.6045.160 (64 bit) (cohort: Stable)
ChromeDriver: 119.0.6045.105 
```

👉 Find Chrome driver 119 [here](https://googlechromelabs.github.io/chrome-for-testing/).

**Note:** It is essential to use a Chrome Driver version that matches your Google Chrome browser. To check your browser version, navigate to `chrome://version` in your browser. Ensure compatibility by downloading the appropriate Chrome Driver version [here](https://chromedriver.chromium.org/downloads).

## What Information Can You Retrieve?

The script retrieves the following information for each job posting:

- **Title:** The job title.
- **Date:** The date when the job was posted.
- **Company:** The name of the hiring company.
- **Company Link:** The link to the hiring company's page on Indeed (if available).
- **Location:** The job location.
- **Type/Salary:** Additional information such as job type or salary details.
- **Description:** A detailed description of the job.
  
![Alt Text](https://github.com/ThanhHung2112/Indeed_crawler/raw/main/assets/Craw.png)

## How to Use

1. **Clone the Repository to Your Computer**
    ```bash
    git clone https://github.com/ThanhHung2112/Indeed_crawler
    ```

2. **Navigate to the Repository Folder**
    ```bash
    cd Indeed_crawler
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Modify Job Search Criteria**
   
   Open the Python script `job_craw.py` and replace the placeholders with your desired job title and location.
    ```python
    if __name__ == "__main__":
        job_title = "Your Job Title"
        job_location = "Your Location"
        job_crawler = Job_craw(job_title, job_location) 
        job_crawler.Start_craw()
    ```
    Replace "Your Job Title" and "Your Location" with the specific job title and location you are interested in then execute the Python script `job_craw.py` to start the job data crawling process.

   
   
