from job_planet_scraper import crawl_jobs
from get_recruitment_text import get_jobplanet_recruitment_text
from to_excel import write_excel
import json

# if __name__ == "__main__":
#     all_jobs = []

#     for i in range(1, 2):  # 테스트용으로 2페이지만
#         url = f"https://www.jobplanet.co.kr/api/v3/job/postings?occupation_level1=&occupation_level2=11905,11907,11904,11906,11610,11911,11609&years_of_experience=&review_score=&job_type=&city=&education_level_id=&order_by=aggressive&page={i}&page_size=8"
#         jobs = crawl_jobs(url)
#         all_jobs.extend(jobs)

#     print(all_jobs)
#     for job in all_jobs:
#         data = get_jobplanet_recruitment_text(job)
#         print(data)
#         if len(data["text"]) > 0:
#             write_excel2(data)

# if all_jobs:
#     print("✅ 수집된 공고 수:", len(all_jobs))
#     print("🎯 예시 공고:", json.dumps(all_jobs[:5], ensure_ascii=False, indent=2))
# else:
#     print("❌ 공고를 수집하지 못했습니다.")

write_excel({'companyName': '(주)버즈빌', 'title': '[광고 운영 플랫폼팀] 프론트 엔드 개발자 (경력 3년 이상)', 'recruitUrl': 'https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1287613', 'annual': '경력', 'text': ['b2b', 'ai', 'ai', 'ai', 'ai', 'saas', '4', 'https', 'www', 'buzzvil', 'com', 'career', 'jwcvgiva7dxl7mrbcsknf', 'https', 'www', 'youtube', 'com', 'watch', 'v', '4txlnymetis', 'https', 'www', 'buzzvil', 'com', 'x', 'ceo', 'https', 'www', 'youtube', 'com', 'watch', 'v', '3rtwwkg8cw8', 'https', 'www', 'youtube', 'com', 'watch', 'v', 'cmduwbm3kkc', 'a', 'k', 'a', 'dash', 'self', 'serve', 'self',
            'serve', 'self', 'serve', 'self', 'serve', 'self', 'serve', 'ui', 'vue', 'js', 'vue', 'js', 'a', 'b', 'automation', 'rule', 'react', 'typescript', 'vue', 'js', 'jest', 'node', 'js', 'github', 'action', 'argocd', 'jira', 'confluence', 'slack', 'github', 'figma', 'datadog', 'grafana', 'prometheus', 'loki', 'sentry', 'react', 'vue', 'angular', 'b2b', 'llm', 'job', 'fit', 'culture', 'fit', 'ceo', '1', '1', '2', '3', '4', 'gloria', 'lee', 'buzzvil', 'com', 'self', 'serve', 'self', 'serve', 'self', 'serve', 'ui', 'ux', 'a', 'b', 'self', 'serve', 'kubernetes', 'x', '272', '2', '3', '4']})
