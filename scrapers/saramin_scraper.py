import time, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.saramin_to_excel import append_recruit_notice


def init_driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=opts
    )
    drv.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": "Object.defineProperty(navigator, 'webdriver', {get:() => undefined})"
        },
    )
    return drv


def fetch_html(driver, url):
    driver.get(url)
    time.sleep(random.uniform(2, 3.5))
    return driver.page_source


def crawl_pages(base_url, start=1, end=3):
    drv, pages = init_driver(), []
    try:
        for p in range(start, end + 1):
            print(f"📄 Page {p} 크롤링 중...")
            html = fetch_html(drv, f"{base_url}&page={p}")
            if html:
                pages.append(html)
            time.sleep(random.uniform(2, 4))
    finally:
        drv.quit()
    return pages


def parse_minimal(html):
    soup, out = BeautifulSoup(html, "html.parser"), []
    for card in soup.select("div.list_item"):
        try:
            comp = card.select_one("div.company_nm a.str_tit").text.strip()
            ttag = card.select_one("div.notification_info a.str_tit")
            title = ttag.get_text(strip=True)
            url = "https://www.saramin.co.kr" + ttag["href"]
            annual = card.select_one("p.career").text.strip()
            out.append(
                {
                    "companyName": comp,
                    "title": title,
                    "recruitUrl": url,
                    "annual": annual,
                }
            )
        except:
            continue
    return out


def run_scraper(base, start=1, end=3):
    all_data = []
    for i, html in enumerate(crawl_pages(base, start, end), start):
        print(f"🔍 Page {i} 파싱 중...")
        all_data += parse_minimal(html)
        time.sleep(random.uniform(1, 2))
    append_recruit_notice(all_data)


if __name__ == "__main__":
    BASE_URL = (
        "https://www.saramin.co.kr/zf_user/jobs/list/job-category"
        "?cat_kewd=84%2C80%2C86%2C104%2C92%2C100"
        "&search_optional_item=n&search_done=y&panel_count=y"
        "&preview=y&isAjaxRequest=3&page_count=100"
        "&sort=RL&type=job-category&is_param=1"
    )
    run_scraper(BASE_URL, start=1, end=2)
