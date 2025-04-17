from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re
from bs4 import BeautifulSoup
import time


def get_jobplanet_recruitment_text(obj: dict) -> list:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    url = f"https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D={obj["id"]}"

    print(url)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select("p.recruitment-detail__txt")

    data = {"companyName": obj["company_name"], "title": obj["title"],
            "recruitUrl": url, "annual": obj["annual_text"]}

    # {회사 이름, 링크, 신입/경력, 텍스트}
    # {comapnyName:string,recruitUrl:string,annual:string,text:list}
    if elements:
        flat_page_texts = [
            word.lower()
            for elem in elements
            for word in re.findall(r'\b[a-zA-Z0-9]+\b', elem.text)
        ]
        data["text"] = flat_page_texts
        driver.quit()
        return data
    else:
        print("텍스트가 존재하지 않습니다.")
        return


def get_saramin_recruitment_text(url: str) -> list:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.select_one("iframe#iframe_content_0")

    src = img["src"]

    if src:
        driver.get(f"https://www.saramin.co.kr{src}")
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        elements = soup.select("td")

        flat_page_texts = [
            word.lower()
            for elem in elements
            for word in re.findall(r'\b[\w가-힣]+\b', elem.text)
        ]
    else:
        pass

    driver.quit()
    return flat_page_texts
