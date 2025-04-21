import pandas as pd
import os
import config.stack_list as stack_list

entire_list = stack_list.entire_list


def get_path(filename):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    excel_dir = os.path.join(BASE_DIR, "data", "excel")
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, filename)

    return save_path


# 총 stack을 category 별로 다시 나누기
def seperate_category(stack_df, categories):
    categorized_data = []
    count_dict = dict(zip(stack_df["stack"], stack_df["count"]))

    for category, stacks in categories.items():
        for stack in stacks:
            if stack in count_dict:
                count = count_dict[stack]
            else:
                count = 0
            categorized_data.append([category, stack, count])

    new_df = pd.DataFrame(categorized_data, columns=["category", "stack", "count"])
    return new_df


# 세분화 한 데이터 엑셀파일에 덮어씌우기
def save_change(stack_path):
    sheet_names = pd.ExcelFile(stack_path).sheet_names
    stack_df_list = [
        pd.read_excel(stack_path, sheet_name=sheet) for sheet in sheet_names
    ]
    save_path = get_path("StackList_Transformed.xlsx")

    new_dataframes = []
    for e, sheet_name, stack_df in zip(entire_list, sheet_names, stack_df_list):
        new_df = seperate_category(stack_df, e)
        new_dataframes.append((sheet_name, new_df))

    with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
        for sheet_name, new_df in new_dataframes:
            new_df.to_excel(writer, index=False, sheet_name=sheet_name)
