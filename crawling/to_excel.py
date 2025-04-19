import os
import job_list
import pandas as pd
import seperate_jobplanet_excel
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

sheet_names = ['FRONT_STACK_LIST', 'BACK_STACK_LIST', 'IOS_STACK_LIST', 'CROSS_STACK_LIST', 'ANDROID_STACK_LIST', 
               'GAME_STACK_LIST', 'SECURITY_STACK_LIST', 'CLOUD_STACK_LIST']
all_stack_list = []
for e in entire_list:
    all_stack_list.append([item for sublist in e.values() for item in sublist])

# 텍스트 데이터들 읽은 후 몇 번 키워드 등장했는지 키워드 세기(all_counts)
# 텍스트 안 스택 키워드 name
def count_data(data_list):
    # 결과를 담을 리스트
    all_counts = [] # [[{},{},{},{},{},{},{},{}], [{},{},{},{},{},{},{},{}]]
    all_keywords = []  # 각 data의 스택 리스트 모음

    for data in data_list:
        keywords = []
        count_list = []

        if not data:
            all_keywords.append(keywords)
            continue

        for stack_list in all_stack_list:
            count_stack = {}

            for keyword in data:
                for stack in stack_list:    
                    if keyword == stack.strip():
                        if stack not in keywords:
                            keywords.append(stack)
                        count_stack[stack] = count_stack.get(stack, 0) + 1
                            
            count_list.append(count_stack)
        all_counts.append(count_list)
        all_keywords.append(keywords)

    return all_counts, all_keywords

#엑셀 파일 읽어오기
def read_data(path):
    df = pd.read_excel(path)
    df.columns = ['companyName', 'title', 'recruitUrl', 'annual', 'text']
    return df

#데이터프레임 중 text column 데이터에서 불필요한 데이터 정리 후 리스트 반환
#total_list는 [[], [], []] 형태
def clear_data(df_list):
    total_list = list()
    text_list = df_list.iloc[:, -1].tolist() #text column(마지막 열) 리스트로 추출
    
    for text in text_list:
    #숫자, 중복 제거 위함
        if  pd.isna(text) or text == '':
            total_list.append([])
        
        if isinstance(text, str): 
            t_list = text.split(',')
            clear = list()
            for t in t_list:
                t = t.strip()
                if not t.isdigit() and t not in clear:
                    clear.append(t)
            total_list.append(clear)
    return total_list

# 8개의 dict(category 8개임) 포함된 리스트 하나 return
def merge_counts(all_counts):
    merge_list = [{} for _ in range(len(entire_list))]
    for count_list in all_counts: #데이터 하나 관련 리스트, 8개의 딕셔너리 포함
        for idx, count in enumerate(count_list):
            for key, value in count.items():
                merge_list[idx][key] = merge_list[idx].get(key, 0) + value

    return merge_list

# 읽은 키워드를 카테고리 별로 분리 후 엑셀 파일에 작성(StackList.xlsx)   
def write_excel(merge_list):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    excel_dir = os.path.join(BASE_DIR, 'data', 'excel')
    
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, 'StackList.xlsx')

    df_list = []
    new_df_list = []
    for merge in merge_list: 
        #리스트 안에 8개의 df가 들어감감
        df_list.append(pd.DataFrame(list(merge.items()), columns=["stack", "count"]))

    for e, sheet_name, stack_df in zip(entire_list, sheet_names, df_list):
        new_df = seperate_jobplanet_excel.seperate_category(stack_df, e)
        new_df_list.append((sheet_name, new_df))
   

    with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
        for sheet_name, new_df in new_df_list:
            new_df.to_excel(writer, index=False, sheet_name=sheet_name)
            # print("생성됨")
            
#마지막 text column을 읽은 뒤 job_list에 포함되어 있는 키워드만 정리해서 다시 해당 column에 덮어씌우기
def write_excel2(all_keywords, path):
    df= read_data(path)
    col = df.columns[-1]

    new_col = []
    for keyword in all_keywords:
        if keyword:
            new_col.append(",".join(keyword))
        else:
            new_col.append("")

    if len(df) != len(new_col):
        print(len(df), len(new_col))
        print("DataFrame 행 수와 all_keywords 길이가 다릅니다!")
    else:
        df[col] = new_col
        df.to_excel(path, index=False)

def total_StackList():
    file1 = "data/excel/StackList.xlsx"  # 첫 번째 엑셀 파일
    file2 = "data/excel/StackList_Transformed.xlsx"  # 두 번째 엑셀 파일

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    excel_dir = os.path.join(BASE_DIR, 'data', 'excel')
    
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, 'Total_StackList.xlsx')

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
            # print("생성됨")
    print("새로운 파일이 저장되었습니다")

#main 실행 시키기 위함
def main(path):
    df_list = read_data(path)   
    total_list = clear_data(df_list)
    all_counts, all_keywords = count_data(total_list) 

    merge_list = merge_counts(all_counts)
    write_excel(merge_list)
    write_excel2(all_keywords, path)

# main(path = "data/excel/stack_candidate.xlsx")
total_StackList()