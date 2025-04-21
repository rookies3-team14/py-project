import os
import job_list
import pandas as pd
import seperate_jobplanet_excel
import filter_data

entire_list = job_list.entire_list
sheet_names = job_list.sheet_names


def get_path(filename):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    excel_dir = os.path.join(BASE_DIR, 'data', 'excel')

    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, filename)

    return save_path

# 읽은 키워드를 카테고리 별로 분리 후 엑셀 파일에 작성(StackList.xlsx)


def write_excel(merge_list):
    save_path = get_path('StackList.xlsx')
    df_list = []
    new_df_list = []
    for merge in merge_list:
        # 리스트 안에 8개의 df가 들어감
        df_list.append(pd.DataFrame(
            list(merge.items()), columns=["stack", "count"]))

    for e, sheet_name, stack_df in zip(entire_list, sheet_names, df_list):
        new_df = seperate_jobplanet_excel.seperate_category(stack_df, e)
        new_df_list.append((sheet_name, new_df))

    with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
        for sheet_name, new_df in new_df_list:
            new_df.to_excel(writer, index=False, sheet_name=sheet_name)

# 마지막 text column을 읽은 뒤 job_list에 포함되어 있는 키워드만 정리해서 다시 해당 column에 덮어씌우기


def write_excel2(all_keywords, df, path):
    col = df.columns[-1]

    new_col = []
    for keyword in all_keywords:
        if keyword:
            new_col.append(",".join(keyword))
        else:
            new_col.append("")

    if len(df) != len(new_col):
        print("DataFrame 행 수와 all_keywords 길이가 다릅니다")
    else:
        df[col] = new_col
        df.to_excel(path, index=False)

# 사람인 엑셀 데이터, 잡플래닛 엑셀 데이터 합치기


def total_StackList(file1, file2):
    save_path = get_path('Total_StackList.xlsx')

    merge_sheets = {}
    for sheet in sheet_names:
        df1 = pd.read_excel(file1, sheet_name=sheet)
        df2 = pd.read_excel(file2, sheet_name=sheet)

        df1.set_index(['category', 'stack'], inplace=True)
        df2.set_index(['category', 'stack'], inplace=True)

        total_df = df1.add(df2, fill_value=0)
        total_df.reset_index(inplace=True)
        merge_sheets[sheet] = total_df
    total_df.to_excel(save_path, index=False)

    with pd.ExcelWriter(save_path) as writer:
        for sheet_name, m_df in merge_sheets.items():
            m_df.to_excel(writer, index=False, sheet_name=sheet_name)
