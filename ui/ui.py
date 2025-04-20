import streamlit as st
import pandas as pd
import os

st.title("채용 정보 시스템")


@st.cache_data
def load_recruit_data(name):
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, "../data/excel/RecruitmentNotice.xlsx")
    df = pd.read_excel(file_path)
    return df


# 버튼 생성
categories = ["FRONTEND", "BACKEND", "IOS", "ANDROID", "GAME", "CLOUD"]
cols = st.columns(len(categories), gap="small")

selected = None
for col, name in zip(cols, categories):
    with col:
        if st.button(name, use_container_width=True, help="카테고리 필터", key=name):
            selected = name

# 선택된 카테고리에 대한 채용 정보 렌더링
if selected:
    df = load_recruit_data(selected)

    # title을 하이퍼링크로 변환
    df["title"] = df.apply(
        lambda row: f'<a href="{row["recruitUrl"]}" target="_blank">{row["title"]}</a>', axis=1
    )

    st.markdown(f"### {selected} 관련 채용 공고")

    for _, row in df.iterrows():
        st.markdown(
            f"""
            <div style="font-size:14px; line-height:1.5">
                🔹 <b>회사명</b>: {row['companyName']}<br>
                🔗 <b>공고 제목</b>: <a href="{row["recruitUrl"]}" target="_blank">{row["title"]}</a><br>
                📆 <b>경력</b>: {row['annual']}<br>
                🛠️ <b>기술 스택</b>: {row['text']}
            </div>
            <hr>
            """,
            unsafe_allow_html=True
        )
