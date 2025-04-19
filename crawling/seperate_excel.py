import pandas as pd
import os
import job_list

front_list = job_list.FRONT_STACK_LIST
back_list = job_list.BACK_STACK_LIST
ios_list = job_list.IOS_STACK_LIST
cross_list = job_list.CROSS_STACK_LIST
android_list = job_list.ANDROID_STACK_LIST
game_list = job_list.GAME_STACK_LIST
security_list = job_list.SECURITY_STACK_LIST
cloud_list = job_list.CLOUD_STACK_LIST

entire_list = [front_list, back_list, ios_list, cross_list,
               android_list, game_list, security_list, cloud_list]

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

def save_change():
    stack_path ='data/excel/StackList.xlsx'
    sheet_names = pd.ExcelFile(stack_path).sheet_names
    stack_df_list = [pd.read_excel(stack_path, sheet_name=sheet) for sheet in sheet_names]

    new_dataframes = []
    for e, sheet_name, stack_df in zip(entire_list, sheet_names, stack_df_list):
        new_df = seperate_category(stack_df, e)
        new_dataframes.append((sheet_name, new_df))

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    excel_dir = os.path.join(BASE_DIR, '..', 'data', 'excel')
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, 'StackList_Transformed.xlsx')
    with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
        for sheet_name, new_df in new_dataframes:
            new_df.to_excel(writer, index=False, sheet_name=sheet_name)
            print("생성됨")

# save_change()