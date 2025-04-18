import os, pandas as pd
from pathlib import Path


def get_notice_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    excel_dir = os.path.join(base_dir, "..", "data", "excel")
    os.makedirs(excel_dir, exist_ok=True)
    return os.path.join(excel_dir, "RecruitmentNotice.xlsx")


def append_recruit_notice(rows):
    path = get_notice_path()
    new_df = pd.DataFrame(rows)
    if Path(path).exists():
        old_df = pd.read_excel(path)
        df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        df = new_df
    df.to_excel(path, index=False)
    print(f"✅ RecruitmentNotice.xlsx 업데이트 완료 ({len(rows)}건 추가)")
