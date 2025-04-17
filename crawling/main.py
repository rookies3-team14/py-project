from job_planet_scraper import crawl_jobs
from get_recruitment_text import get_jobplanet_recruitment_text
from to_excel import write_excel
import json
from job_list import SAMPLE_LIST

if __name__ == "__main__":
    # all_jobs = []

    # for i in range(13, 36):  # 테스트용으로 2페이지만
    #     li=[]
    #     url = f"https://www.jobplanet.co.kr/api/v3/job/postings?occupation_level1=&occupation_level2=11905,11907,11904,11906,11610,11911,11609&years_of_experience=&review_score=&job_type=&city=&education_level_id=&order_by=aggressive&page={i}&page_size=8"
    #     jobs = crawl_jobs(url)
    #     all_jobs.extend(jobs)
    #     li.extend(jobs)
    #     print(li)

    for job in SAMPLE_LIST:
        data = get_jobplanet_recruitment_text(job)
        if data and data.get("text") and len(data["text"]) > 0:
            write_excel(data)
        else:
            print(f"❌ 공고를 수집하지 못했습니다: {job}")


# if all_jobs:
#     print("✅ 수집된 공고 수:", len(all_jobs))
#     print("🎯 예시 공고:", json.dumps(all_jobs[:5], ensure_ascii=False, indent=2))
# else:
#     print("❌ 공고를 수집하지 못했습니다.")
