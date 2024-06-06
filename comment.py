import time

import requests
import json
from sign import sign as Sign


def get_comment(song="000Vsz6x4YhS2r"):
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
            "uin": "1152921505285173556",
            "g_tk_new_20200303": 1894091738,
            "g_tk": 1894091738
        },
        "req_1": {
            "module": "music.musicsearch.HotkeyService",
            "method": "GetHotkeyForQQMusicMobile",
            "param": {
                "searchid": "21953897180297680",
                "remoteplace": "txt.yqq.top",
                "from": "yqqweb"
            }
        },
        "req_2": {
            "method": "GetCommentCount",
            "module": "music.globalComment.GlobalCommentRead",
            "param": {
                "request_list": [
                    {
                        "biz_type": 1,
                        "biz_id": "487354860",
                        "biz_sub_type": 0
                    }
                ]
            }
        },
        "req_3": {
            "module": "music.musicasset.SongFavRead",
            "method": "IsSongFanByMid",
            "param": {
                "v_songMid": [
                    song
                ]
            }
        },
        "req_4": {
            "module": "music.globalComment.CommentRead",
            "method": "GetNewCommentList",
            "param": {
                "BizType": 1,
                "BizId": "487354860",
                "LastCommentSeqNo": "",
                "PageSize": 25,
                "PageNum": 0,
                "FromCommentId": "",
                "WithHot": 1,
                "PicEnable": 1,
                "LastTotal": 0,
                "LastTotalVer": "0"
            }
        },
        "req_5": {
            "module": "music.globalComment.CommentRead",
            "method": "GetHotCommentList",
            "param": {
                "BizType": 1,
                "BizId": "487354860",
                "LastCommentSeqNo": "",
                "PageSize": 15,
                "PageNum": 0,
                "HotType": 2,
                "WithAirborne": 1,
                "PicEnable": 1
            }
        },
        "req_6": {
            "module": "music.globalComment.CommentAsset",
            "method": "GetCmBgCard",
            "param": {}
        },
        "req_7": {
            "module": "music.musichallSong.PlayLyricInfo",
            "method": "GetPlayLyricInfo",
            "param": {
                "songMID": song
            }
        },
        "req_8": {
            "module": "music.paycenterapi.LoginStateVerificationApi",
            "method": "GetChargeAccount",
            "param": {
                "appid": "mlive"
            }
        },
        "req_9": {
            "module": "userInfo.VipQueryServer",
            "method": "SRFVipQuery_V2",
            "param": {
                "uin_list": [
                    "1152921505285173556"
                ]
            }
        },
        "req_10": {
            "module": "userInfo.BaseUserInfoServer",
            "method": "get_user_baseinfo_v2",
            "param": {
                "vec_uin": [
                    "1152921505285173556"
                ]
            }
        },
        "req_11": {
            "module": "music.lvz.VipIconUiShowSvr",
            "method": "GetVipIconUiV2",
            "param": {
                "PID": 3
            }
        },
        "req_12": {
            "module": "MessageCenter.MessageCenterServer",
            "method": "GetMessage",
            "param": {
                "uin": "1152921505285173556",
                "red_dot": [
                    {
                        "msg_type": 1
                    }
                ]
            }
        },
        "req_13": {
            "module": "GlobalComment.GlobalCommentMessageReadServer",
            "method": "GetMessage",
            "param": {
                "uin": "1152921505285173556",
                "page_num": 0,
                "page_size": 1,
                "last_msg_id": "",
                "type": 0
            }
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    params = {
        "_": str(int(time.time() * 1000)),
        "sign": Sign(data)
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    if response.status_code == 200:
        return response.json()['req_4']['data']


if __name__ == '__main__':
    info = get_comment("000Vsz6x4YhS2r")
    print(info)
