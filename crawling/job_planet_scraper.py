from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time


def get_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    return driver


def get_html(driver, url):
    driver.get(url)
    time.sleep(1)  # 페이지 로딩 시간 확보
    return driver.page_source


def parse_json(html):
    soup = BeautifulSoup(html, "html.parser")
    json_text = soup.find("pre").text if soup.find("pre") else ""
    if json_text:
        return json.loads(json_text)
    else:
        print("❌ <pre> 태그를 찾을 수 없습니다.")
        return None


def extract_job_data(data):
    jobs = [
        {
            "id": job.get("id"),
            "title": job.get("title"),  # ✅ 직무명
            "company_name": job.get("company", {}).get("name"),  # ✅ 회사 이름
            "annual_text": job.get("annual", {}).get("text"),  # ✅ 연봉
        }
        for job in data.get("data", {}).get("recruits", [])
    ]
    return jobs


def crawl_jobs(url):
    driver = get_driver()
    html = get_html(driver, url)
    data = parse_json(html)
    driver.quit()

    if data:
        return extract_job_data(data)
    return []
