import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd

# # Function to scrape job details from a single job page
# def scrape_job_details(job_url):
#     try:
#         response = requests.get(job_url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extracting job details
#         job_title = soup.find('h3', class_='title').text.strip()
#         job_description = soup.find('div', class_='description').text.strip()
#         task_include = soup.find('div', class_='task-include').text.strip()
#         nec_code = soup.find('div', class_='nec-code').text.strip()
#         noss_code = soup.find('div', class_='noss-code').text.strip()
#         specific_skills = soup.find('div', class_='specific-skills').text.strip()
#         knowledge_interest = soup.find('div', class_='knowledge-interest').text.strip()
        
#         return {
#             'Job Title': job_title,
#             'Description': job_description,
#             'Task Include': task_include,
#             'NEC Code': nec_code,
#             'NOSS Code': noss_code,
#             'Specific Skills': specific_skills,
#             'Knowledge and Interest': knowledge_interest
#         }
#     except Exception as e:
#         print(f"Error scraping {job_url}: {e}")
#         return None

# # Function to scrape job codes and redirection URLs from the main page
# def scrape_job_urls(url):
#     try:
#         response = requests.get(url)
#         print(response)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         soup = BeautifulSoup(response.content,"html.parser")
#         print("soup :",soup)
        
#         # Extracting job codes and redirection URLs
#         job_codes = soup.p["class"]
#         print("job codes :",job_codes)
#         job_urls = ['https://emasco.mohr.gov.my/masco/' + job_code.text.strip() for job_code in job_codes]
        
#         return job_urls
#     except Exception as e:
#         print(f"Error scraping job URLs from {url}: {e}")
#         return []

# # Main function to execute the scraping and saving to Excel
# def main():
#     url = "https://emasco.mohr.gov.my/stem"
#     job_urls = scrape_job_urls(url)
    
#     # Scraping job details for each job URL
#     job_details = []
#     for job_url in job_urls:
#         job_detail = scrape_job_details(job_url)
#         if job_detail:
#             job_details.append(job_detail)
    
#     if job_details:
#         # Convert data to DataFrame
#         df = pd.DataFrame(job_details)
        
#         # Save to Excel
#         df.to_excel('job_details.xlsx', index=False)
#         print("Job details saved successfully to job_details.xlsx")
#     else:
#         print("No job details were scraped.")


# main()
driver = webdriver.Firefox()
url = "https://emasco.mohr.gov.my/stem"
driver.get(url)
html = driver.page_source
print(html)
