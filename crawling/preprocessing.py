import pandas as pd
from job_list import (
    FRONT_ALL_STACK_LIST, BACK_ALL_STACK_LIST, IOS_ALL_STACK_LIST,
    CROSS_ALL_STACK_LIST, ANDROID_ALL_STACK_LIST, GAME_ALL_STACK_LIST,
    SECURITY_ALL_STACK_LIST, CLOUD_ALL_STACK_LIST
)

# 엑셀 파일 불러오기
df = pd.read_excel("data/excel/RecruitmentNotice.xlsx")

# 소문자로 통일된 텍스트 기준으로 매칭
df["text"] = df["text"].fillna("").str.lower()

# job 컬럼 초기화
df["job"] = ""

# 분류 기준 리스트 딕셔너리로 정리
category_map = {
    "FRONTEND": FRONT_ALL_STACK_LIST,
    "BACKEND": BACK_ALL_STACK_LIST,
    "IOS": IOS_ALL_STACK_LIST,
    "CROSS": CROSS_ALL_STACK_LIST,
    "ANDROID": ANDROID_ALL_STACK_LIST,
    "GAME": GAME_ALL_STACK_LIST,
    "SECURITY": SECURITY_ALL_STACK_LIST,
    "CLOUD": CLOUD_ALL_STACK_LIST
}

# 각 row마다 어떤 카테고리 스택이 포함돼 있는지 확인


def classify_job(text):
    matched_categories = []
    for category, stack_list in category_map.items():
        if any(stack in text for stack in stack_list):
            matched_categories.append(category)
    return ", ".join(matched_categories)


# job 컬럼 채우기
df["job"] = df["text"].apply(classify_job)

# 엑셀 덮어쓰기 저장
df.to_excel("RecruitmentNotice_1.xlsx", index=False)
