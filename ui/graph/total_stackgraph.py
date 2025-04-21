import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
import numpy as np
import pandas as pd

# 5% 미만이면 빈 문자열 반환하고, 아니면 소수점 한자리까지 표기
def custom_autopct(pct):
    if pct<5:
        return ''
    else:
        return f'{pct:.1f}%'
    
def read_excelData(stack_path):
    sheet_names = pd.ExcelFile(stack_path).sheet_names
    stack_df = [pd.read_excel(stack_path, sheet_name=sheet).fillna({"count": 0}) for sheet in sheet_names]
    return sheet_names, stack_df

def make_graph():
    # "/System/Library/Fonts/Supplemental/AppleMyungjo.ttf"
    font_path = 'C:\\windows\\Fonts\\malgun.ttf'
    font_prop = fm.FontProperties(fname=font_path).get_name()
    matplotlib.rc('font', family=font_prop)
    
    sheet_names, stack_df = read_excelData("data/excel/Total_StackList.xlsx")

    for idx, df in enumerate(stack_df):
        # count 값의 합계가 0이 아닌 category만 선택
        valid_categories = []
        for cat in df["category"].unique():
            cat_rows = df[df["category"] == cat]
            total = cat_rows["count"].sum()
            if total != 0:
                valid_categories.append(cat)

        if len(valid_categories) == 0:
            continue

        # 서브플롯 행, 열 계산 (한 행당 최대 4개의 차트)
        max_cols = 4
        ncols = min(len(valid_categories), max_cols)
        nrows = math.ceil(len(valid_categories) / ncols)

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 6, nrows * 6))
        fig.suptitle(f"{sheet_names[idx]}", fontsize=16, y=0.05)  # 👈 여기 추가

        # axes 객체 배열을 평탄화
        axes = np.ravel(axes)

        for idx, category in enumerate(valid_categories):
            cat_data = df[df["category"] == category]
            cat_data = cat_data[cat_data["count"] > 0]

            stacks = cat_data["stack"].tolist()
            counts = cat_data["count"]
            
            percentages = counts / counts.sum() * 100
    
            ax = axes[idx]
            ax.pie(percentages, labels=stacks,  autopct=custom_autopct, startangle=90, radius=0.8)
            ax.set_aspect("equal")
            ax.set_title(category, fontsize=12, pad = 0)

        # 빈 subplot은 제거하여 빈 축이 보이지 않도록 함
        for ax in axes[len(valid_categories):]:
            ax.remove()

        plt.tight_layout()
        plt.show()

make_graph()