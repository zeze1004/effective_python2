import time
import requests


class TimeOutException(Exception):
    pass


json_data = []


# 웹 호출시, 반환하는 데이터를 list에 저장
def crawling(url):
    r = requests.get(url, timeout=1)
    print(json_data)
    yield json_data.append(r.text)


# 0.5초간격으로 함수 호출, 타임아웃시 종료
while True:
    time.sleep(0.5)
    try:
        t = next(crawling('https://cataas.com/cat?json=true'))
    except requests.Timeout as e:
        print(e)
        break
