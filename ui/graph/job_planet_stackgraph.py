# subplots() 함수를 사용하여 axes 객체를 생성하기
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import pandas as pd

font_path = 'C:\\windows\\Fonts\\malgun.ttf'
font_prop = fm.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_prop)

stack_path ='data/excel/StackList.xlsx'



# print(stack_df[0].head())

# for index, df in enumerate(stack_df):  # 총 8개의 figure 반복
#     fig, ax = plt.subplots(figsize=(16, 4))  # 개별 figure와 axes 생성 (4x4 크기)
    
#     # Pie plot 생성
#     ax.pie(
#         df['percentages'],
#         labels= df['stack'],
#         autopct='%1.1f%%',  # 퍼센트 표시 형식
#         startangle=90,  # 시작 각도
#         colors=['skyblue', 'lightcoral']  # 색상 지정
#     )
    
#     # 제목 설정
#     ax.set_title('기술 스택 별 퍼센티지')
    
#     # Figure 렌더링
#     plt.show()

# fig, axs = plt.subplots(2, 4, figsize=(16, 8))  # 2행 4열 배치, 전체 Figure 크기 설정

# # 데이터를 각 서브플롯에 배치
# for idx, (df, ax) in enumerate(zip(stack_df, axs.flat)):  # `zip`으로 데이터와 각 subplot 연결
#     ax.pie(
#         df['percentages'],
#         labels= df['stack'],
#         autopct='%1.1f%%',  # 퍼센트 표시 형식
#         startangle=90,  # 시작 각도
#         colors=['skyblue', 'lightcoral'],  # 색상 지정
#         textprops={'fontsize': 8}, # 텍스트(라벨 및 퍼센티지) 글씨 크기 설정
#         radius = 1.2,
#         labeldistance=1.03
#     )

#     ax.set_title(f'{sheet_names[idx]}기술 스택 별 퍼센티지')  # 각 서브플롯 제목 추가

# # 레이아웃 정리 (간격 조정)
# plt.tight_layout()

# # 그래프 화면에 출력
# plt.show()

stack_path = "data/excel/StackList_Transformed.xlsx"
sheet_names = pd.ExcelFile(stack_path).sheet_names
stack_df = [pd.read_excel(stack_path, sheet_name=sheet) for sheet in sheet_names]

categories = stack_df["category"].unique()
category_data = {category: stack_df[stack_df["category"] == category] for category in categories}

fig, axes = plt.subplots(1, len(categories), figsize=(len(categories) * 5, 5))

for ax, (category, data) in zip(axes, category_data.items()):
    stacks = data["stack"].tolist()
    counts = data["count"].tolist()

    ax.pie(counts, labels=stacks, autopct='%1.1f%%', startangle=90)
    ax.set_title(category, fontsize=12)

# Step 4: 전체 레이아웃 조정 및 출력
plt.tight_layout()
plt.show()