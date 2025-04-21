import os
import time
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 1) .env 파일 로드
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise RuntimeError("⚠️ GITHUB_TOKEN 환경변수를 설정해주세요")


# 2) 엑셀 저장 경로
def get_excel_path():
    base = os.path.dirname(os.path.abspath(__file__))
    d = os.path.join(base, "..", "data", "excel")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "GithubInterviewRepos_Filtered.xlsx")


# 3) GitHub 검색 함수 (키워드 하나씩)
def search_repos_single(keyword, per_page=30):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    params = {
        "q": f"{keyword} in:readme,description",
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
    }
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        return r.json().get("items", [])
    else:
        print(f"❌ '{keyword}' 검색 실패: {r.status_code}")
        return []


# 4) 분야별 검색 키워드 (영문 인기 레포 + 한글 키워드)
primary_keywords = {
    "Front-end": [
        "프론트엔드 면접 질문",
        "리액트 면접 질문",
        "자바스크립트 면접 질문",
        "HTML 면접 질문",
        "CSS 면접 질문",
        "Vue 면접 질문",
        "웹 개발 면접",
        "프론트엔드 개발자 면접",
        "React 면접 준비",
        "프론트엔드 취업 면접",
    ],
    "Back-end": [
        "백엔드 면접 질문",
        "스프링 면접 질문",
        "자바 면접 질문",
        "Node.js 면접 질문",
        "REST API 면접",
        "DB 면접 질문",
        "백엔드 개발자 면접",
        "서버 개발 면접",
        "백엔드 코딩 테스트",
        "웹 서버 면접",
    ],
    "iOS": [
        "iOS 면접 질문",
        "스위프트 면접 질문",
        "SwiftUI 면접",
        "iOS 개발자 면접",
        "애플 개발 면접",
        "iOS 앱 면접",
        "iOS 인터뷰",
    ],
    "Android": [
        "안드로이드 면접 질문",
        "코틀린 면접 질문",
        "Kotlin Android 면접",
        "Android 개발자 면접",
        "모바일 개발 면접",
        "안드로이드 앱 면접",
        "Android 인터뷰",
    ],
    "Cross-platform": [
        "크로스 플랫폼 면접",
        "리액트 네이티브 면접 질문",
        "플러터 면접 질문",
        "하이브리드 앱 면접",
        "모바일 크로스 플랫폼 면접",
        "React Native 면접",
        "Flutter 면접 준비",
    ],
    "Game": [
        "게임 개발 면접",
        "유니티 면접 질문",
        "언리얼 엔진 면접 질문",
        "게임 클라이언트 면접",
        "게임 서버 면접",
        "게임 프로그래머 면접",
    ],
    "Security": [
        "정보보안 면접 질문",
        "보안 면접",
        "해킹 면접",
        "모의해킹 면접",
        "보안 취업 면접",
        "사이버보안 면접",
    ],
    "Cloud/DevOps": [
        "클라우드 면접 질문",
        "DevOps 면접 질문",
        "AWS 면접 질문",
        "도커 면접 질문",
        "쿠버네티스 면접 질문",
        "CI/CD 면접",
    ],
}

# 5) 분야별 Fallback 키워드 (Broad English terms)
fallback_keywords = {
    "Front-end": [
        "frontend interview questions",
        "javascript interview questions",
        "css interview questions",
    ],
    "Back-end": [
        "backend interview questions",
        "rest api interview questions",
        "database interview questions",
    ],
    "iOS": [
        "ios interview questions",
        "swiftui interview questions",
    ],
    "Android": [
        "android developer interview questions",
        "mobile interview questions",
    ],
    "Cross-platform": [
        "mobile cross-platform interview questions",
        "hybrid mobile interview questions",
    ],
    "Game": [
        "game development interview questions",
        "game programming interview questions",
    ],
    "Security": [
        "security interview questions",
        "penetration testing interview questions",
        "owasp interview questions",
    ],
    "Cloud/DevOps": [
        "클라우드 면접 질문",
        "AWS 면접",
        "DevOps 면접 질문",
        "GCP 면접 질문",
    ],
}

# 6) 최소 star 필터
MIN_STARS = 1

# 7) 수집 & 병합 로직
all_rows = []
for stack in primary_keywords:
    print(f"\n🔍 [{stack}] 수집 시작")
    repos_map = {}

    # 7.1) 1차 키워드
    for kw in primary_keywords[stack]:
        print(f"  • 기본키워드: {kw}")
        for repo in search_repos_single(kw):
            url = repo["html_url"]
            if url in repos_map:
                continue
            if repo["stargazers_count"] < MIN_STARS:
                continue
            desc = (repo.get("description") or "").lower()
            if len(desc) < 20 or "interview" not in desc:
                continue
            repos_map[url] = repo
        time.sleep(1)

    # 7.2) 부족할 경우 Fallback
    if len(repos_map) < 10:
        for kw in fallback_keywords[stack]:
            print(f"  • Fallback키워드: {kw}")
            for repo in search_repos_single(kw):
                url = repo["html_url"]
                if url in repos_map:
                    continue
                if repo["stargazers_count"] < MIN_STARS:
                    continue
                desc = (repo.get("description") or "").lower()
                if len(desc) < 20 or "interview" not in desc:
                    continue
                repos_map[url] = repo
            time.sleep(1)
            if len(repos_map) >= 10:
                break

    # 7.3) star 순 정렬 & 상위 10개 취합
    sorted_top10 = sorted(
        repos_map.values(), key=lambda r: r["stargazers_count"], reverse=True
    )[:10]

    for repo in sorted_top10:
        updated = datetime.fromisoformat(repo["updated_at"].rstrip("Z"))
        all_rows.append(
            {
                "스택": stack,
                "레포": repo["full_name"],
                "Stars": repo["stargazers_count"],
                "최종업데이트": updated.date(),
                "설명": repo.get("description") or "",
                "URL": repo["html_url"],
            }
        )

    print(f"✅ [{stack}] – {len(sorted_top10)}개 확보 완료")

# 8) 엑셀 저장
df = pd.DataFrame(all_rows)
df.to_excel(get_excel_path(), index=False)
print(f"\n🎉 총 {len(df)}개 레포가 저장되었습니다: {get_excel_path()}")
