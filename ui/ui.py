import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib

# 한글 깨짐 방지 설정
# Mac 사용자용 (윈도우는 'Malgun Gothic')
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

st.set_page_config(layout="wide")
st.title("채용 정보 시스템")

# ========== 데이터 로드 함수 ==========


@st.cache_data
def load_recruit_data():
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, "../data/excel/RecruitmentNotice.xlsx")
    return pd.read_excel(file_path)


@st.cache_data
def load_stack_data_all_sheets():
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, "../data/excel/Total_StackList.xlsx")
    excel_file = pd.ExcelFile(file_path)
    return {sheet: excel_file.parse(sheet).assign(sheet=sheet) for sheet in excel_file.sheet_names}


@st.cache_data
def load_github_interview_repos():
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(
        path, "../data/excel/GithubInterviewRepos_Filtered.xlsx")
    df = pd.read_excel(file_path)
    df = df.rename(columns={"스택": "stack", "레포": "repo", "Stars": "stars",
                            "최종업데이트": "updated", "설명": "desc", "URL": "url"})
    df["updated"] = pd.to_datetime(df["updated"])
    return df.sort_values(by="stars", ascending=False)

# ========== 렌더 함수 ==========


def render_stack(text):
    if pd.isna(text):
        return ""
    stacks = [s.strip() for s in text.split(",")]
    return " ".join([
        f'<span style="background:#e0f7fa; padding:4px 8px; border-radius:8px; margin:2px; display:inline-block;">{s}</span>'
        for s in stacks
    ])


# ========== 설정 ==========
categories = ["FRONTEND", "BACKEND", "IOS",
              "ANDROID", "CROSS", "SECURITY", "GAME", "CLOUD"]
SHEET_NAME_MAP = {
    "FRONTEND": "FRONT_STACK_LIST",
    "BACKEND": "BACK_STACK_LIST",
    "IOS": "IOS_STACK_LIST",
    "ANDROID": "ANDROID_STACK_LIST",
    "CROSS": "CROSS_STACK_LIST",
    "SECURITY": "SECURITY_STACK_LIST",
    "GAME": "GAME_STACK_LIST",
    "CLOUD": "CLOUD_STACK_LIST"
}

if "limit" not in st.session_state:
    st.session_state["limit"] = 10
if "selected" not in st.session_state:
    st.session_state["selected"] = "FRONTEND"

# ========== 버튼 렌더링 ==========
cols = st.columns(len(categories), gap="small")
for col, name in zip(cols, categories):
    with col:
        if st.button(name, use_container_width=True, key=name):
            st.session_state["selected"] = name
            st.session_state["limit"] = 10
            st.rerun()

selected = st.session_state["selected"]

if selected:
    selected_sheet_name = SHEET_NAME_MAP.get(selected)
    all_stack_data = load_stack_data_all_sheets()

    # 🔥 기술 스택 시각화
    st.markdown(f"### {selected} 분야 기술 스택 분포 (카테고리별)")
    if selected_sheet_name in all_stack_data:
        stack_df = all_stack_data[selected_sheet_name].dropna(
            subset=["category", "stack", "count"])
        stack_df["count"] = stack_df["count"].astype(int)

        categories_in_sheet = stack_df["category"].unique()
        chart_rows = [categories_in_sheet[i:i+4]
                      for i in range(0, len(categories_in_sheet), 4)]

        for row_categories in chart_rows:
            row_cols = st.columns(4)
            for i in range(4):
                if i < len(row_categories):
                    category = row_categories[i]
                    cat_df = stack_df[(stack_df["category"] == category) & (
                        stack_df["count"] > 0)]
                    if not cat_df.empty:
                        with row_cols[i]:
                            st.markdown(f"**{category.capitalize()}**")
                            fig, ax = plt.subplots(figsize=(3.5, 3.5))
                            ax.pie(cat_df["count"], labels=cat_df["stack"], autopct="%1.1f%%",
                                   startangle=140, textprops={'fontsize': 8})
                            ax.axis("equal")
                            fig.tight_layout()
                            st.pyplot(fig)
                else:
                    with row_cols[i]:
                        st.write("")
    else:
        st.warning(
            f"{selected}에 해당하는 시트 ({selected_sheet_name})가 Total_StackList.xlsx에 없습니다.")

    # 📄 채용 공고 출력
    df = load_recruit_data()
    df = df[df["job"].str.contains(selected, case=False, na=False)].copy()
    df["title"] = df.apply(
        lambda row: f'<a href="{row["recruitUrl"]}" target="_blank">{row["title"]}</a>', axis=1)

    st.markdown(f"### {selected} 관련 채용 공고")
    limited_df = df.head(st.session_state["limit"])
    for _, row in limited_df.iterrows():
        st.markdown(f"""
        <div style="font-size:14px; line-height:1.8">
            🔹 <b>회사명</b>: {row['companyName']}<br>
            🔗 <b>공고 제목</b>: {row['title']}<br>
            📆 <b>경력</b>: {row['annual']}<br>
            🛠️ <b>기술 스택</b>: {render_stack(row['text'])}
        </div>
        <hr>
        """, unsafe_allow_html=True)

    if st.session_state["limit"] < len(df):
        if st.button("더보기"):
            st.session_state["limit"] += 10
            st.rerun()

    # 🧠 GitHub 인터뷰 레포 출력 (선택된 분야에 맞게 필터링)
    st.markdown("### 기술 스택별 GitHub 인터뷰 레포 (Top 10)")
    github_df = load_github_interview_repos()
    current_stack_df = github_df[github_df["stack"].str.strip(
    ).str.upper() == selected.upper()].head(10)

    rows = [current_stack_df.iloc[i:i+2]
            for i in range(0, len(current_stack_df), 2)]
    for row in rows:
        cols = st.columns(2)
        for col, (_, repo) in zip(cols, row.iterrows()):
            with col:
                st.markdown(f"""
                <div style="padding:10px; border-radius:10px; background-color:#f4f4f4; margin-bottom:10px;">
                    <b>📁 <a href="{repo['url']}" target="_blank">{repo['repo']}</a></b><br>
                    ⭐ {repo['stars']} stars | 🕒 {repo['updated'].date()}<br>
                    <span style="font-size:13px; color:#555;">{repo['desc'][:120]}...</span>
                </div>
                """, unsafe_allow_html=True)
