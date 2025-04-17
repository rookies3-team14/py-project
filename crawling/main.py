from job_planet_scraper import crawl_jobs
import json

if __name__ == "__main__":
    all_jobs = []

    for i in range(1, 3):  # 테스트용으로 2페이지만
        url = f"https://www.jobplanet.co.kr/api/v3/job/postings?occupation_level1=&occupation_level2=11905,11907,11904,11906,11610,11911,11609&years_of_experience=&review_score=&job_type=&city=&education_level_id=&order_by=aggressive&page={i}&page_size=8"
        jobs = crawl_jobs(url)
        all_jobs.extend(jobs)

    if all_jobs:
        print("✅ 수집된 공고 수:", len(all_jobs))
        print("🎯 예시 공고:", json.dumps(all_jobs[:5], ensure_ascii=False, indent=2))
    else:
        print("❌ 공고를 수집하지 못했습니다.")
