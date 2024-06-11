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
        "login_type": "2",
        "qqmusic_key": "W_X_63B0aX7iUImLW-2sRSMrUGERgDbJ8cO05XmJGoDY2zdztDbu5pWKluXkDVTZbmLn6sFmhDIKJZRySgBI",
        "wxopenid": "opCFJwyZFOVUmN-I3CXmTBjbBGC8",
        "qm_keyst": "W_X_63B0aX7iUImLW-2sRSMrUGERgDbJ8cO05XmJGoDY2zdztDbu5pWKluXkDVTZbmLn6sFmhDIKJZRySgBI",
        "wxunionid": "oqFLxsrrW6fR8NTx-YKijNxrhp6w",
        "wxuin": "1152921505285173556",
        "euin": "oK6kowEAoK4z7K-F7K6loi4k7c**",
        "wxrefresh_token": "81_yVtXsXMLzlBw6M1cujwlsAw1wjvzWA9lC_UPHQNdtWbNfzHSSheTRhgDIKlrPTKCkCRcYJwBRJbnm0M8wh-aOVfaGJFWZjcdS9kfpmxwEks",
        "psrf_qqunionid": "",
        "psrf_qqopenid": "",
        "tmeLoginType": "1",
        "psrf_qqaccess_token": "",
        "psrf_qqrefresh_token": "",
        "ts_last": "y.qq.com/n/ryqq/singer/003tMm0y0TuewY"
    }
    url = "https://c6.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    params = {
        "_": "1717655961279",
        "cv": "4747474",
        "ct": "24",
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "1",
        "uin": "1152921505285173556",
        "g_tk_new_20200303": "1534435690",
        "g_tk": "1534435690",
        "hostUin": "0",
        "is_xml": "0",
        "key": keyword
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    if response.status_code == 200:
        return response.json()['data']


if __name__ == '__main__':
    singer = search('杨宗纬')
    print(singer)
