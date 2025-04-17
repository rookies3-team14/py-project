from job_planet_scraper import crawl_jobs
from get_recruitment_text import get_jobplanet_recruitment_text
from to_excel import write_excel2
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

write_excel2({'companyName': '(주)디셈버앤컴퍼니', 'title': '핀트(fint) 프론트엔드(front-end) 개발자', 'recruitUrl': 'https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1290918', 'annual': '경력', 'text': ['december', 'company', 'fint', 'it', 'togetherness', 'invest', 'together', 'build', 'together', 'grow', 'together', 'change', 'together', 'playground', 'caring', 'attitude', 'meta', 'cognition', '1', '2', '3', '4', '5', '6', 'irp', 'seo', 'crm', 'preface', 'react', 'typescript', 'next', 'js', 'react', 'query',
             'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'react', 'vue', 'angular', 'spa', 'html', 'css', 'git', 'asana', 'confluence', 'slack', 'figma', 'react', 'typescript', 'next', 'js', 'react', 'query', 'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'typescript', 'ssr', 'ui', 'webpack', '1', '2', '3', '4', '5', '231', 'west']})
write_excel2({'companyName': '(주)디셈버앤컴퍼니', 'title': '핀트(fint) 프론트엔드(front-end) 개발자', 'recruitUrl': 'https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1290918', 'annual': '경력', 'text': ['december', 'company', 'fint', 'it', 'togetherness', 'invest', 'together', 'build', 'together', 'grow', 'together', 'change', 'together', 'playground', 'caring', 'attitude', 'meta', 'cognition', '1', '2', '3', '4', '5', '6', 'irp', 'seo', 'crm', 'preface', 'react', 'typescript', 'next', 'js', 'react', 'query',
             'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'react', 'vue', 'angular', 'spa', 'html', 'css', 'git', 'asana', 'confluence', 'slack', 'figma', 'react', 'typescript', 'next', 'js', 'react', 'query', 'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'typescript', 'ssr', 'ui', 'webpack', '1', '2', '3', '4', '5', '231', 'west']})
