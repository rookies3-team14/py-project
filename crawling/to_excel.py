import os
import job_list
import pandas as pd
from pathlib import Path 

front_list = job_list.FRONT_STACK_LIST
back_list =job_list.BACK_STACK_LIST
ios_list = job_list.IOS_STACK_LIST
cross_list = job_list.CROSS_STACK_LIST
android_list = job_list.ANDROID_STACK_LIST
game_list =job_list.GAME_STACK_LIST
security_list = job_list.SECURITY_STACK_LIST
cloud_list = job_list.CLOUD_STACK_LIST

entire_list = [front_list, back_list, ios_list, cross_list, android_list, game_list, security_list, cloud_list]


def count_data(data_list, elist, count_total, stack_names):
    count_s = {}
    data = data_list['text']
    for d in data:
        for e in elist:  
            if d.strip() == e.strip():
                if d not in count_s:
                    count_s[d] = 1
                    stack_names.append(d)
    
    count_total.append(count_s)
  


 # 파일 존재 여부를 체크하기 위한 모듈

def write_excel(data_list):
    count_total = list()
    stack_names = list()

    for e in entire_list:
        count_data(data_list, e, count_total, stack_names)
    print(count_total)
    print(stack_names)
    write_excel2(data_list, stack_names)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    excel_dir = os.path.join(BASE_DIR, '..', 'data', 'excel')
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, 'StackList.xlsx')
  
    sheet_names = ['FRONT_STACK_LIST','BACK_STACK_LIST','IOS_STACK_LIST', 'CROSS_STACK_LIST', 'ANDROID_STACK_LIST', 'GAME_STACK_LIST', 
                'SECURITY_STACK_LIST', 'CLOUD_STACK_LIST']
    df_list = list()
    for i in range(len(sheet_names)):
        df = pd.DataFrame(list(count_total[i].items()), columns= ['stack', 'count'])
        df.set_index('stack', inplace=True)  # stack을 인덱스로 설정
        df_list.append(df)

    total_df_list = list()
    if Path(save_path).exists():
        try:
            for i in range(len(sheet_names)):
                old_df = pd.read_excel(save_path, sheet_name=sheet_names[i], index_col=0)
                total_df_list.append(old_df.add(df_list[i], fill_value=0))
        except:
            # 시트가 엑셀 파일 안에 없을 때
            total_df_list = df_list
    #엑셀 파일 없을 때
    else:
        total_df_list = df_list

    if Path(save_path).exists():
        with pd.ExcelWriter(save_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            for sheet, df in zip(sheet_names, total_df_list):
                df.to_excel(writer, sheet_name=sheet)
    else:
        with pd.ExcelWriter(save_path, engine='openpyxl', mode='w') as writer:
            for sheet, df in zip(sheet_names, total_df_list):
                df.to_excel(writer, sheet_name=sheet)


def write_excel2(data, stack_names):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    excel_dir = os.path.join(BASE_DIR, '..', 'data', 'excel')
    
    os.makedirs(excel_dir, exist_ok=True)
    save_path = os.path.join(excel_dir, 'RecruitmentNotice.xlsx')


    data['text'] = ','.join(stack_names) 
    df = pd.DataFrame([data])
    
    if Path(save_path).exists():
        old_df = pd.read_excel(save_path) 
        total_df = pd.concat([old_df, df], ignore_index=True)
        total_df.to_excel(save_path, index=False) 
    else:
        df.to_excel(save_path, index = False)

data = [{'companyName': '(주)디셈버앤컴퍼니', 'title': '핀트(fint) 프론트엔드(front-end) 개발자', 'recruitUrl': 'https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1290918', 'annual': '경력', 'text': ['december', 'company', 'fint', 'it', 'togetherness', 'invest', 'together', 'build', 'together', 'grow', 'together', 'change', 'together', 'playground', 'caring', 'attitude', 'meta', 'cognition', '1', '2', '3', '4', '5', '6', 'irp', 'seo', 'crm', 'preface', 'react', 'typescript', 'next', 'js', 'react', 'query', 'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'react', 'vue', 'angular', 'spa', 'html', 'css', 'git', 'asana', 'confluence', 'slack', 'figma', 'react', 'typescript', 'next', 'js', 'react', 'query', 'jotai', 'emotion', 'yarn', 'berry', 'pnpm', 'turborepo', 'webpack', 'esbuild', 'swc', 'babel', 'ci', 'cd', 'gitlab', 'ci', 'cd', 'typescript', 'ssr', 'ui', 'webpack', '1', '2', '3', '4', '5', '231', 'west']}
,{'companyName': '(주)버즈빌', 'title': '[광고 추천팀] 백엔드 개발자 (Engineering Manager, Team Lead)', 'recruitUrl': 'https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1288726', 'annual': '경력', 'text': ['saas', 'sk', 'cj', 'ai', 'saas', '4', 'dsp', 'demand', 'side', 'platform', 'a', 'https', 'www', 'buzzvil', 'com', 'career', 'jwcvgiva7dxl7mrbcsknf', 'https', 'www', 'youtube', 'com', 'watch', 'v', '4txlnymetis', 'https', 'www', 'buzzvil', 'com', 'x', 'ceo', 'https', 'www', 'youtube', 'com', 'watch', 'v', '3rtwwkg8cw8', 'https', 'www', 'youtube', 'com', 'watch', 'v', 'cmduwbm3kkc', 'a', 'b', 'ml', 'go', 'python', 'mysql', 'dynamodb', 'redis', 'elasticsearch', 'kafka', 'kubernetes', 'grpc', 'rest', 'api', 'github', 'action', 'spinnaker', 'jira', 'confluence', 'slack', 'github', 'datadog', 'grafana', 'prometheus', 'loki', 'aws', 'cloudwatch', 'aws', 'gcp', 'python', 'golang', 'apache', 'kafka', 'ceo', '1', '1', '2', '3', '4', 'gloria', 'lee', 'buzzvil', 'com', 'x', '272', '2', '3', '4']}

]
for d in data:
    write_excel(d)
    print("생성함")
        
