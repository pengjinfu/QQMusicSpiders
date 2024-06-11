import requests


def search(keyword):
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
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
        "fqm_sessionid": "cf2dfa2e-af7e-4d8d-96d9-39dcf033c18b",
        "pgv_info": "ssid=s241344748",
        "_qpsvr_localtk": "0.2193967508504444",
        "qm_keyst": "W_X_63B0am5LToR9Hdk8_Y4h9Ill0i2G3yKVxXwd16hRNEz6GlvbJA5nDQy-YI_VsTZE0GU6JngxGYfOQ7eY",
        "psrf_qqunionid": "",
        "wxopenid": "opCFJwyZFOVUmN-I3CXmTBjbBGC8",
        "qqmusic_key": "W_X_63B0am5LToR9Hdk8_Y4h9Ill0i2G3yKVxXwd16hRNEz6GlvbJA5nDQy-YI_VsTZE0GU6JngxGYfOQ7eY",
        "wxuin": "1152921505285173556",
        "psrf_qqopenid": "",
        "wxunionid": "oqFLxsrrW6fR8NTx-YKijNxrhp6w",
        "psrf_qqrefresh_token": "",
        "euin": "oK6kowEAoK4z7K-F7K6loi4k7c**",
        "psrf_qqaccess_token": "",
        "wxrefresh_token": "81_Hm9fS1jRFa7ICw-wlP31VtC1qPXmv1YldPPJeXk8OfW8Khl5ENFlEI9y8dmRkITN0vw6nzSoDtcpjAQcK9LrApA9UA8ygoK-zaMqX5WyC4o",
        "tmeLoginType": "1",
        "login_type": "2",
        "ts_last": "y.qq.com/n/ryqq/songDetail/000Vsz6x4YhS2r"
    }
    url = "https://c6.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    params = {
        "_": "1717651292331",
        "cv": "4747474",
        "ct": "24",
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "1",
        "uin": "1152921505285173556",
        "g_tk_new_20200303": "1894091738",
        "g_tk": "1894091738",
        "hostUin": "0",
        "is_xml": "0",
        "key": keyword
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    if response.status_code == 200:
        return response.json()['data']


if __name__ == '__main__':
    songs = search('我会好好的')
    print(songs)
