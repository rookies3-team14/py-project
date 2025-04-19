# subplots() 함수를 사용하여 axes 객체를 생성하기
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
import numpy as np
import seaborn as sns
import pandas as pd

font_path = 'C:\\windows\\Fonts\\malgun.ttf'
font_prop = fm.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_prop)

stack_path = "data/excel/Total_StackList.xlsx"
sheet_names = pd.ExcelFile(stack_path).sheet_names

stack_df = [pd.read_excel(stack_path, sheet_name=sheet).fillna({"count": 0}) for sheet in sheet_names]

for df in stack_df:
    # 0%이면 빈 문자열 반환하고, 아니면 소수점 한자리까지 표기
    def custom_autopct(pct):
        return '' if pct<5 else f'{pct:.1f}%'

    # count 값의 합계가 0이 아닌 category만 선택
    valid_categories = [cat for cat in df["category"].unique()
                        if df.loc[df["category"] == cat, "count"].sum() != 0]
    if len(valid_categories) == 0:
        continue

    # 서브플롯 행, 열 계산 (한 행당 최대 4개의 차트)
    max_cols = 4
    ncols = min(len(valid_categories), max_cols)
    nrows = math.ceil(len(valid_categories) / ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 6, nrows * 6))
    # axes 객체가 배열인지 확인 후 평탄화
    if isinstance(axes, np.ndarray):
        axes = axes.flatten()
    else:
        axes = [axes]

    for idx, category in enumerate(valid_categories):
        cat_data = df[df["category"] == category]
        cat_data = cat_data[cat_data["count"] > 0]

        stacks = cat_data["stack"].tolist()
        counts = cat_data["count"].fillna(0)

        total = counts.sum()
        if total == 0:
            percentages = [0] * len(counts)
        else:
            percentages = counts / total * 100

        ax = axes[idx]
        ax.pie(percentages, labels=stacks,  autopct=custom_autopct, startangle=90, radius=0.8)
        ax.set_aspect("equal")
        ax.set_title(category, fontsize=12, pad = 5)

    # 빈 subplot은 제거하여 빈 축이 보이지 않도록 함
    for ax in axes[len(valid_categories):]:
        ax.remove()

    plt.tight_layout()
    plt.show()