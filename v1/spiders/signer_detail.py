import requests
from lxml import etree
import time
import os


def detail(day, singer):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
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
        "ts_last": f"y.qq.com/n/ryqq/singer/{singer}/song"
    }
    url = f"https://y.qq.com/n/ryqq/singer/{singer}/song"
    response = requests.get(url, headers=headers, cookies=cookies)

    html = response.text
    with open(f'../src/html/singer_{singer}_{day}.html', 'w', encoding='utf-8') as file:
        file.write(html)


def handle_detail(day, singer):
    with open(f'../src/html/singer_{singer}_{day}.html', 'r', encoding='utf-8') as file:
        html = file.read()
        html = etree.HTML(html)

        infos = html.xpath('/html/script[1]/text()')[0]
        infos = infos.replace('\n', '').replace('  ', '0').replace('\r', '').replace('\t', '').replace('false',
                                                                                                       '0').replace(
            'true', '1').replace('null', '0').replace('\n\t', '').replace('undefined', '0')

        infos = infos.split('DATA__ =')[1]

        return infos


def main(singer='0025NhlN2yWrP4'):
    today = time.localtime()
    day = str(today.tm_year) + str(today.tm_mon) + str(today.tm_mday)
    files = os.listdir('../src/html')
    for file in files:
        if '.html' in file and '_' in file:
            code = file.split('_')[1].split('.')[0]
            if int(code) < int(day):
                os.remove(file)
    if os.path.exists(f'../src/html/singer_{singer}_{day}.html'):
        return handle_detail(day, singer)
    else:
        detail(day, singer)
    return handle_detail(day, singer)


if __name__ == '__main__':
    info = main('000xogLP35ayzS')
    print(info)
