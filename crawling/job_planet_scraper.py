from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json


class JobPlanetCrawler:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(3)

    def get_html(self):
        # HTML 소스 가져오기
        self.driver.get(self.url)
        return self.driver.page_source

    def parse_json(self, html):
        # HTML에서 JSON 데이터를 파싱하여 반환
        soup = BeautifulSoup(html, "html.parser")
        json_text = soup.find("pre").text if soup.find("pre") else ""
        if json_text:
            return json.loads(json_text)
        else:
            print("❌ <pre> 태그를 찾을 수 없습니다.")
            return None

    def extract_job_data(self, data):
        # JSON 데이터에서 id,경력 값 추출
        jobs = [
            {
                "id": job.get("id"),
                "annual_text": job.get("annual", {}).get("text")
            }
            for job in data.get("data", {}).get("recruits", [])
        ]
        return jobs

    def crawl_jobs(self):
        # 크롤링 실행 후 결과를 반환
        html = self.get_html()
        data = self.parse_json(html)
        if data:
            jobs = self.extract_job_data(data)
            return jobs
        return []

    def quit(self):
        self.driver.quit()


# job_data = []
# # 사용 예시
# if __name__ == "__main__":
#     for i in range(1, 36):
#         url = f"https://www.jobplanet.co.kr/api/v3/job/postings?occupation_level1=&occupation_level2=11905,11907,11904,11906,11610,11911,11609&years_of_experience=&review_score=&job_type=&city=&education_level_id=&order_by=aggressive&page={i}&page_size=8"
#         crawler = JobPlanetCrawler(url)
#         job_data.extend(crawler.crawl_jobs())

#     # if job_data:
#     #     print(json.dumps(job_data, ensure_ascii=False, indent=2))

#     crawler.quit()

