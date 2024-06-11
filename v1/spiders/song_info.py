import time

import requests
import json
from v1.spiders.sign import sign as Sign

info = {"官方歌单": 3317, "音乐人在听": 1069, "达人心选": 3900}
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
    "ts_refer": "cn.bing.com/",
    "pgv_pvid": "948151655",
    "ts_uid": "2644563480",
    "fqm_pvqid": "e8d702ed-b079-48d7-b559-2b5b23ee1518",
    "fqm_sessionid": "e2c29963-b386-4f70-abbb-bab2f3bb8ae6",
    "pgv_info": "ssid=s1979152243",
    "_qpsvr_localtk": "0.9098933149682831",
    "ts_last": "y.qq.com/n/ryqq/category"
}
url = "https://u6.y.qq.com/cgi-bin/musics.fcg"

for i in range(200):
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
            "param": {
                "caller": "0",
                "category_id": i,
                "size": 20,
                "page": 0,
                "use_page": 1
            },
            "method": "get_category_content",
            "module": "music.playlist.PlayListCategory"
        },
        "req_2": {
            "method": "get_category_basic",
            "module": "playlist.PlayListCategoryServer",
            "param": {
                "caller": "0",
                "category_id": i
            }
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    sign = Sign(data)
    params = {
        "_": str(int(time.time() * 1000)),
        "sign": sign
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    if response.status_code == 200:
        data = response.json()
        if 'req_2' in str(data):
            info[data['req_2']['data']['category']['name']] = i
            print(data)
            time.sleep(10)

if __name__ == '__main__':
    print(info)
