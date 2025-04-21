import job_list
import pandas as pd

entire_list = job_list.entire_list
all_stack_list = job_list.all_stack_list

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
