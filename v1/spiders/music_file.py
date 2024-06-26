import time

import requests
import json
from v1.spiders.sign import sign as Sign


def get_music_file(song="000Vsz6x4YhS2r"):
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
        "fqm_sessionid": "cf2dfa2e-af7e-4d8d-96d9-39dcf033c18b",
        "pgv_info": "ssid=s241344748",
        "_qpsvr_localtk": "0.2193967508504444",
        "login_type": "2",
        "ts_last": "y.qq.com/n/ryqq/player"
    }
    url = "https://u6.y.qq.com/cgi-bin/musics.fcg"

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
            "module": "music.musicasset.SongFavRead",
            "method": "IsSongFanByMid",
            "param": {
                "v_songMid": [
                    "000Vsz6x4YhS2r"
                ]
            }
        },
        "req_2": {
            "module": "music.musichallSong.PlayLyricInfo",
            "method": "GetPlayLyricInfo",
            "param": {
                "songMID": "000Vsz6x4YhS2r",
                "songID": 492250888
            }
        },
        "req_3": {
            "method": "GetCommentCount",
            "module": "music.globalComment.GlobalCommentRead",
            "param": {
                "request_list": [
                    {
                        "biz_type": 1,
                        "biz_id": "492250888",
                        "biz_sub_type": 0
                    }
                ]
            }
        },
        "req_4": {
            "module": "music.musichallAlbum.AlbumInfoServer",
            "method": "GetAlbumDetail",
            "param": {
                "albumMid": "001P2mQj32hV2z"
            }
        },
        "req_5": {
            "module": "vkey.GetVkeyServer",
            "method": "CgiGetVkey",
            "param": {
                "guid": "7388177047",
                "songmid": [
                    "000Vsz6x4YhS2r"
                ],
                "songtype": [
                    0
                ],
                "uin": "0",
                "loginflag": 1,
                "platform": "20"
            }
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    params = {
        "_": str(int(time.time() * 1000)),
        "sign": Sign(data)
    }
    print(params)
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    if response.status_code == 200:
        return response.json()


if __name__ == '__main__':
    info = get_music_file('000KL9de0YaLIR')
    print(info)
