import pandas as pd


def save_to_excel(data, file_path):
    """
    크롤링한 데이터를 엑셀 파일로 저장하는 함수
    """
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)


def clean_data(data):
    """
    데이터 정리 함수
    필요에 따라 텍스트 처리, 공백 제거 등을 수행
    """
    cleaned_data = {
        key: value.strip() if isinstance(value, str) else value
        for key, value in data.items()
    }
    return cleaned_data
