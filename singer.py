import time
import requests
import json
from sign import sign as Sign


def singer(page):
    try:
        page = int(page)
    except:
        return "请输入数字！"
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://y.qq.com",
        "pragma": "no-cache",
        "referer": "https://y.qq.com/",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }
    cookies = {

    }
    url = "https://u6.y.qq.com/cgi-bin/musics.fcg"
    if 0 < page < 89:
        data = {
            "comm": {
                "cv": 4747474,
                "ct": 24,
                "format": "json",
                "inCharset": "utf-8",
                "outCharset": "utf-8",
                "notice": 0,
                "platform": "yqq.json",
                "needNewCode": 1,
                "uin": 0,
                "g_tk_new_20200303": 5381,
                "g_tk": 5381
            },
            "req_1": {
                "module": "music.musichallSinger.SingerList",
                "method": "GetSingerListIndex",
                "param": {
                    "area": -100,
                    "sex": -100,
                    "genre": -100,
                    "index": -100,
                    "sin": page * 80,
                    "cur_page": page + 1
                }
            }
        }
        data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        sign = Sign(data)
        params = {
            "_": str(int(time.time() * 1000)),
            "sign": sign
        }
        response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

        if response.status_code == 200:
            return response.json()
        else:
            return "请求失败，请重试！"
    else:
        return '您输入的页数不正确！'


if __name__ == '__main__':
    print(singer(1))
