def get_text_in_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "referer":url
    }

    res=requests.get(url,headers=headers)

    print(res)


get_text_in_url(
    "https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1280679")
