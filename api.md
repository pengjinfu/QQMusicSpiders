# QQ音乐接口文档

做为一个音乐爱好者，我是支持付费的，本项目主要用于学习爬虫知识，逆向知识，用于研究，不作其它用图。

**免责声明：** 本项目仅供个人学习、研究使用，严禁用于商业用途。请用户在遵守相关法律法规的前提下使用本项目。



## 1.首页功能 

### 1.1 首页功能

 #### 1.1.1 首页链接

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=links

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=links`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "音乐馆": "https://y.qq.com/",
            "我的音乐": "https://y.qq.com/n/ryqq/profile",
            "客户端": "https://y.qq.com//y.qq.com/download/index.html",
            "开放平台": "https://y.qq.com//y.qq.com/artists",
            "VIP": "https://y.qq.com//y.qq.com/portal/vipportal/index.html",
            "首页": "https://y.qq.com/",
            "歌手": "https://y.qq.com/n/ryqq/singer_list",
            "新碟": "https://y.qq.com/n/ryqq/album",
            "排行榜": "https://y.qq.com/n/ryqq/toplist/4",
            "分类歌单": "https://y.qq.com/n/ryqq/category",
            "电台": "https://y.qq.com/n/ryqq/radio",
            "MV": "https://y.qq.com/n/ryqq/mvList",
            "数字专辑": "https://y.qq.com/n/ryqq/album_mall",
            "null": "https://y.qq.comhttp://y.qq.com/y/static/down/qplay.html?pgv_ref=qqmusic.y.topmenu",
            "车载互联": "https://y.qq.comhttp://y.qq.com/y/static/down/car_introduce.html",
            "QQ演出": "https://y.qq.comhttp://y.qq.com/yanchu/?pgv_ref=qqmusic.y.topmenu",
            "腾讯音乐": "https://y.qq.comhttps://www.tencentmusic.com/",
            "CJ ENM": "https://y.qq.com//y.qq.com/portal/company_detail.html?id=297",
            "腾讯视频": "https://y.qq.comhttp://v.qq.com/",
            "手机QQ空间": "https://y.qq.comhttp://z.qzone.com/",
            "最新版QQ": "https://y.qq.comhttp://im.qq.com/",
            "腾讯社交广告": "https://y.qq.comhttp://e.qq.com/index.shtml",
            "电脑管家": "https://y.qq.comhttp://guanjia.qq.com/",
            "QQ浏览器": "https://y.qq.comhttp://browser.qq.com/",
            "腾讯微云": "https://y.qq.comhttp://www.weiyun.com/",
            "腾讯云": "https://y.qq.comhttps://cloud.tencent.com/?fromSource=gwzcw.756433.756433.756433",
            "企鹅FM": "https://y.qq.comhttp://fm.qq.com/",
            "智能电视网": "https://y.qq.comhttp://www.znds.com/",
            "当贝市场": "https://y.qq.comhttp://www.dangbei.com/",
            "酷我音乐": "https://y.qq.comhttps://www.kuwo.cn/",
            "酷狗听书": "https://y.qq.comhttps://www.kugou.com/ts/"
        }
    }
    ```

    

#### 1.1.2  歌单推荐/热门歌单

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=hots

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=hots`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "1": {
                "title": "通勤好歌安利：地铁上的安静Time",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1088.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/8924937695"
            },
            "2": {
                "title": "抖音超热中文歌：越听越好听",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：3144.8万",
                "link": "https://y.qq.com/n/ryqq/playlist/9141033696"
            },
            "3": {
                "title": "周杰伦 · 翻开12月的回忆",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：61.9万",
                "link": "https://y.qq.com/n/ryqq/playlist/9094276126"
            },
            "4": {
                "title": "抖音热歌｜细数耳机里的流行旋律",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1836.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/9069454203"
            },
            "5": {
                "title": "抖音热歌榜",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1171.9万",
                "link": "https://y.qq.com/n/ryqq/playlist/9098894921"
            },
            "6": {
                "title": "NCT 127 | 三巡官方歌单福利",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：69.1万",
                "link": "https://y.qq.com/n/ryqq/playlist/9088609641"
            },
            "7": {
                "title": "繁花 电视剧原声",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1533.8万",
                "link": "https://y.qq.com/n/ryqq/playlist/9110204452"
            },
            "8": {
                "title": "听歌都会哭的人，又怎么会幸福呢",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1942.0万",
                "link": "https://y.qq.com/n/ryqq/playlist/9059132538"
            },
            "9": {
                "title": "天气每天都在变，更何况爱情呢？",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1314.0万",
                "link": "https://y.qq.com/n/ryqq/playlist/8923542913"
            },
            "10": {
                "title": "神仙打架！演绎1+1＞2的经典合作",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1016.1万",
                "link": "https://y.qq.com/n/ryqq/playlist/9056540606"
            },
            "11": {
                "title": "抖音热歌：单曲循环不切歌",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：4240.0万",
                "link": "https://y.qq.com/n/ryqq/playlist/8941334617"
            },
            "12": {
                "title": "高考战歌|不负年华纪念励志青春",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：5.4万",
                "link": "https://y.qq.com/n/ryqq/playlist/9235895506"
            },
            "13": {
                "title": "抖音热歌：全网循环超好听",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：7897.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/8967478774"
            },
            "14": {
                "title": "听多久emo多久，哭了也就过去了",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：2978.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/9044794022"
            },
            "15": {
                "title": "伤感emo片段：忍不住就红了眼眶",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：6590.8万",
                "link": "https://y.qq.com/n/ryqq/playlist/9004756725"
            },
            "16": {
                "title": "我从不质疑真心，但真心瞬息万变",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1134.9万",
                "link": "https://y.qq.com/n/ryqq/playlist/8980712583"
            },
            "17": {
                "title": "这些歌，光是听到就已经很遗憾了",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：2665.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/9068452841"
            },
            "18": {
                "title": "到点了该emo了，00后的听歌现状",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：3416.1万",
                "link": "https://y.qq.com/n/ryqq/playlist/9024058565"
            },
            "19": {
                "title": "抖音超热中文歌：一次听个够",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1201.9万",
                "link": "https://y.qq.com/n/ryqq/playlist/9020925470"
            },
            "20": {
                "title": "抖音最火热门歌曲（持续更新中）",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：2810.3万",
                "link": "https://y.qq.com/n/ryqq/playlist/9166337615"
            },
            "21": {
                "title": "抖音热歌：全网最火首首入心",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1.6亿",
                "link": "https://y.qq.com/n/ryqq/playlist/8914504917"
            },
            "22": {
                "title": "华语佳作200首↻让听歌成为享受",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：4449.2万",
                "link": "https://y.qq.com/n/ryqq/playlist/8911220082"
            },
            "23": {
                "title": "深夜emo神曲:哪首是你心中的No.1",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：2462.7万",
                "link": "https://y.qq.com/n/ryqq/playlist/8901625965"
            },
            "24": {
                "title": "Kpop元气女团：开启上班自嗨模式",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1250.1万",
                "link": "https://y.qq.com/n/ryqq/playlist/8888842434"
            },
            "25": {
                "title": "爆款戳这里：真爱就是循环一千遍",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "bfl": "播放量：1211.5万",
                "link": "https://y.qq.com/n/ryqq/playlist/8888225996"
            }
        }
    }
    ```

    

#### 1.1.3  新歌首发

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=new

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=new`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "1": {
                "title": "远方的花",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "time": "04:40",
                "link": "https://y.qq.com/n/ryqq/singer/004CAb4E2FRQVu",
                "signer": "雷佳"
            },
            "2": {
                "title": "《变身！》大张伟Feat.C2C (Kigga&鱼头killa4nia)",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "time": "03:40",
                "link": "https://y.qq.com/n/ryqq/singer/003ULldz24exLi",
                "signer": "大张伟"
            },
            ......
            "45": {
                "title": "三餐四季",
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAAAnOwc2AAAAD0lEQVR4AWM4bYwJh7QgANLSYzmZH3ISAAAAAElFTkSuQmCC",
                "time": "04:20",
                "link": "https://y.qq.com/n/ryqq/singer/002ncDrp0oMLbe",
                "signer": "TAKUMA THE GREAT"
            }
        }
    }
    ```

    

#### 1.1.4  精彩推荐

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=wonder

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=wonder`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": [
            {
                "jumptype": 10002,
                "id": "51673128",
                "subid": "0029jkkH2AdQAs",
                "title": "蔡徐坤新歌《Afterglow》上线",
                "cover": "https://y.qq.com/music/common/upload/MUSIC_FOCUS/6599411.jpg",
                "tjreport": "1_1_53436_1_10002_51673128",
                "CfgID": "53436",
                "focusid": "53436",
                "tag": "首发",
                "scheme": "qqmusic://qq.com/ui/album?p=%7B%22id%22%3A%2251673128%22%7D"
            },
            {
                "jumptype": 3001,
                "id": "https://i2.y.qq.com/n3/cm/pages/vip/singercard/index.html?sonic_remain_params=actid&extraid=NLhqzGKjRc4StRFmkCQ+kg==&actid=34&_miniplayer=1&_hidehd=1&ADTAG=hz_faneconomy_YQQ&openinqqmusic=1&keep_cid=1",
                "subid": "",
                "title": "aespa绝美星光开启，即刻捕捉>>",
                "cover": "https://y.qq.com/music/common/upload/MUSIC_FOCUS/6593669.jpg",
                "tjreport": "1_1_53431_2_3001_https://i2.y.qq.com/n3/cm/pages/vip/singercard/index.html?sonic%5Fremain%5Fparams=actid&extraid=NLhqzGKjRc4StRFmkCQ+kg==&actid=34&%5Fminiplayer=1&%5Fhidehd=1&ADTAG=hz%5Ffaneconomy%5FYQQ&openinqqmusic=1&keep%5Fcid=1",
                "CfgID": "53431",
                "focusid": "53431",
                "tag": "商城",
                "scheme": "qqmusic://qq.com/ui/openUrl?p=%7B%22url%22%3A%22https%3A%2F%2Fi2.y.qq.com%2Fn3%2Fcm%2Fpages%2Fvip%2Fsingercard%2Findex.html%3Fsonic_remain_params%3Dactid%26extraid%3DNLhqzGKjRc4StRFmkCQ%2Bkg%3D%3D%26actid%3D34%26_miniplayer%3D1%26_hidehd%3D1%26ADTAG%3Dhz_faneconomy_YQQ%26openinqqmusic%3D1%26keep_cid%3D1%22%2C%22need_check_domain%22%3A%22no%22%7D"
            },
            {
                "jumptype": 10002,
                "id": "51408050",
                "subid": "002aYcdI13DcFj",
                "title": "周深《风吹过的晨曦》唱出爱的纯粹",
                "cover": "https://y.qq.com/music/common/upload/MUSIC_FOCUS/6595199.jpg",
                "tjreport": "1_1_53417_3_10002_51408050",
                "CfgID": "53417",
                "focusid": "53417",
                "tag": "影视",
                "scheme": "qqmusic://qq.com/ui/album?p=%7B%22id%22%3A%2251408050%22%7D"
            },
            {
                "jumptype": 10002,
                "id": "51544828",
                "subid": "002VcNSS2CRnMN",
                "title": "双笙全新单曲《不是绿洲》上线",
                "cover": "https://y.qq.com/music/common/upload/ocs/c29ae254830b512539917e0782547879.png",
                "tjreport": "1_1_53397_4_10002_51544828",
                "CfgID": "53397",
                "focusid": "53397",
                "tag": "国风",
                "scheme": "qqmusic://qq.com/ui/album?p=%7B%22id%22%3A%2251544828%22%7D"
            }
        ]
    }
    ```

    

####  1.1.5 新碟首发

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=albums

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=albums`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": [
            {
                "id": 51408404,
                "mid": "0028NBT10taF5x",
                "name": "Something Worth Saving (爱依然存在)",
                "trans_name": "",
                "singers": [
                    {
                        "id": 162964,
                        "mid": "004ZINJh11aFcu",
                        "name": "孟佳",
                        "foreign_name": "",
                        "type": 0,
                        "genre": 0,
                        "area": 0,
                        "company": {
                            "id": 0,
                            "name": "",
                            "ex": {
                                "desc": "",
                                "company_photo": 0
                            }
                        },
                        "grade": 0,
                        "origin": 0,
                        "enter": 0,
                        "country": 0,
                        "identity": 0,
                        "birthday": "",
                        "instrument": 0,
                        "ex": {
                            "desc": "",
                            "wiki": "",
                            "tag": "",
                            "ex_status": 0,
                            "ex_identity": 0,
                            "info_name": "",
                            "name_spell": "",
                            "band": "",
                            "dieDate": "",
                            "force_show": 0,
                            "auth_status": 0,
                            "control": 0
                        },
                        "photo": {
                            "has_photo": 0,
                            "photo_cnt": 0,
                            "big_photo_flag": "",
                            "magic_rgb": 0,
                            "pic1_flag": 0,
                            "pic2_flag": 0,
                            "pic_mid": ""
                        },
                        "opt_grade": 0,
                        "status": 0,
                        "opt_grade_new": 0,
                        "vertical_type": "",
                        "singer_wiki": "",
                        "index": "",
                        "is_classical": 0
                    }
                ],
                ....
                "head_magic_color": ""
            }
        ]
    }
    ```

    

#### 1.1.6 排行榜

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=ranks

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=ranks`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": [
            {
                "groupId": 0,
                "groupName": "巅峰榜",
                "toplist": [
                    {
                        "topId": 62,
                        "recType": 10005,
                        "topType": 0,
                        "updateType": 1,
                        "title": "飙升榜",
                        "titleDetail": "飙升榜 第162天",
                        "titleShare": "飙升榜 2024年第162天",
                        "titleSub": "",
                        "intro": "1. 榜单定义：QQ音乐站内播放热度飙升最快的前100首歌曲。<br>2. 更新频率：每日更新。 <br>3. 排序依据：根据歌曲在QQ音乐移动端登陆用户中产生的完整播放日环比增长率进行排序。",
                        "cornerMark": 0,
                        "period": "2024-06-10",
                        "updateTime": "2024-06-10",
                        "history": {
                            "year": [],
                            "subPeriod": []
                        },
                        "listenNum": 18633712,
                        "totalNum": 100,
                        "song": [
                            {
                                "rank": 1,
                                "rankType": 6,
                                "rankValue": "223%",
                                "recType": 0,
                                "songId": 494518168,
                                "vid": "",
                                "albumMid": "0029jkkH2AdQAs",
                                "title": "Afterglow",
                                "singerName": "蔡徐坤",
                                "singerMid": "002nXp292LIOGV",
                                "songType": 0,
                                "uuidCnt": 0,
                                "cover": "http://y.gtimg.cn/music/photo_new/T002R300x300M0000029jkkH2AdQAs_1.jpg",
                                "mvid": 0
                            },
                            {
                                "rank": 2,
                                "rankType": 6,
                                "rankValue": "25%",
                                "recType": 0,
                                "songId": 494423709,
                                "vid": "",
                                "albumMid": "000dHkbu33fn2z",
                                "title": "玛丽亚 (Live)",
                                "singerName": "杨和苏KeyNG/李外LilWine",
                                "singerMid": "0041TJCF4IpZoU",
                                "songType": 0,
                                "uuidCnt": 0,
                                "cover": "http://y.gtimg.cn/music/photo_new/T002R300x300M000000dHkbu33fn2z_1.jpg",
                                "mvid": 0
                            },
                            
                        "musichallTitle": "台湾地区榜",
                        "musichallSubtitle": "",
                        "musichallPicUrl": "http://y.gtimg.cn/music/photo_new/T002R300x300M000003GLtZm09BdNc_1.jpg",
                        "specialScheme": "",
                        "mbFrontLogoUrl": "https://y.gtimg.cn/music/photo_new/T052R300x300M000002NVHPg2F28Cw.jpg",
                        "mbHeadLogoUrl": "http://y.gtimg.cn/music/common/upload/test_order_channel_hitlist_con/3415643.png",
                        "cityName": "",
                        "magicColor": {
                            "r": 112,
                            "g": 45,
                            "b": 8
                        },
                        "topAlbumURL": "http://y.gtimg.cn/music/photo_new/T002R300x300M000003GLtZm09BdNc_1.jpg",
                        "groupType": 1,
                        "icon": 0,
                        "adID": 0,
                        "mbIntroWebUrl": "",
                        "mbLogoUrl": ""
                    },
                    {
                        "topId": 3,
                        "recType": 10005,
                        "topType": 0,
                        "updateType": 0,
                        "title": "欧美榜",
                        "titleDetail": "欧美榜 第23周",
                        "titleShare": "欧美榜 2024年第23周",
                        "titleSub": "",
                        "intro": "QQ音乐每周播放热度最高的欧美地区歌曲TOP 100，发行期为30天内。",
                        "cornerMark": 0,
                        "period": "2024_23",
                        "updateTime": "2024-06-06",
                        .....
                    }
            }
            ]
    }
    ```

    

#### 1.1.7 mv

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=mv

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=mv`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "list": [
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 221,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 2047,
                    "mvid": 2156259,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M000000jlLSF2Sf254.jpg",
                    "playcnt": 22738,
                    "pubdate": 1717948800,
                    "score": 0,
                    "singers": [
                        {
                            "id": 199509,
                            "mid": "003fA5G40k6hKc",
                            "name": "周深",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000003fA5G40k6hKc_6.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "风吹过的晨曦",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "0025IM2j3t05Sl"
                },
                ......
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 171,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 1903,
                    "mvid": 2151195,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M101003YItoP3SJXmx.jpg",
                    "playcnt": 37406,
                    "pubdate": 1715788800,
                    "score": 0,
                    "singers": [
                        {
                            "id": 11446,
                            "mid": "002PZBgg1S9xPX",
                            "name": "陈楚生",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000002PZBgg1S9xPX_4.jpg"
                        },
                        {
                            "id": 11451,
                            "mid": "000b7B7h1fXzaM",
                            "name": "苏醒AllenSu",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000000b7B7h1fXzaM_3.jpg"
                        },
                        {
                            "id": 11450,
                            "mid": "000TprbQ0R4aGb",
                            "name": "王栎鑫",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000000TprbQ0R4aGb_3.jpg"
                        },
                        {
                            "id": 11455,
                            "mid": "004PjYVG2cjyBK",
                            "name": "张远",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000004PjYVG2cjyBK_6.jpg"
                        },
                        {
                            "id": 11447,
                            "mid": "001iaSfi07zuSE",
                            "name": "王铮亮",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000001iaSfi07zuSE_6.jpg"
                        },
                        {
                            "id": 11449,
                            "mid": "004gbMvP356XaI",
                            "name": "陆虎",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000004gbMvP356XaI_6.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "相信光",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "003YItoP3SJXmx"
                },
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 182,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 2047,
                    "mvid": 2151228,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M101003Wluay1v51Ui.jpg",
                    "playcnt": 27077,
                    "pubdate": 1715788800,
                    "score": 0,
                    "singers": [
                        {
                            "id": 1265025,
                            "mid": "001z67i41jyW3d",
                            "name": "MARK",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000001z67i41jyW3d_28.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "MARK《200》MV",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "003Wluay1v51Ui"
                },
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 210,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 2047,
                    "mvid": 2150931,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M000003I9fmn06Neev.jpg",
                    "playcnt": 621,
                    "pubdate": 1715788800,
                    "score": 0,
                    "singers": [
                        {
                            "id": 1266099,
                            "mid": "000QeJVk445LYW",
                            "name": "Luke Combs",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000000QeJVk445LYW_2.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "Ain't No Love In Oklahoma(From Twisters: The Album)",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "004WH7lq15xnKB"
                },
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 217,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 2047,
                    "mvid": 2150820,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M101000GeTP44Mnbvj.jpg",
                    "playcnt": 112594,
                    "pubdate": 1715616000,
                    "score": 0,
                    "singers": [
                        {
                            "id": 2241311,
                            "mid": "001Iu4Dv1NzRCD",
                            "name": "摩登兄弟刘宇宁",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000001Iu4Dv1NzRCD_3.jpg"
                        },
                        {
                            "id": 2174230,
                            "mid": "002ug9Ha2zYM1y",
                            "name": "单依纯",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000002ug9Ha2zYM1y_7.jpg"
                        },
                        {
                            "id": 1339126,
                            "mid": "002KASw53FQbTK",
                            "name": "王者荣耀",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000002KASw53FQbTK_4.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "未完待续",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "000GeTP44Mnbvj"
                },
                {
                    "comment_cnt": 0,
                    "diff": 0,
                    "duration": 181,
                    "has_fav": 0,
                    "has_star": 0,
                    "mv_switch": 2047,
                    "mvid": 2150783,
                    "picurl": "http://y.gtimg.cn/music/photo_new/T015R640x360M101002yKdjR0FQo49.jpg",
                    "playcnt": 22306,
                    "pubdate": 1715616000,
                    "score": 0,
                    "singers": [
                        {
                            "id": 112,
                            "mid": "000hNnWC3kko2c",
                            "name": "蔡健雅",
                            "picurl": "http://y.gtimg.cn/music/photo_new/T001R150x150M000000hNnWC3kko2c_6.jpg"
                        }
                    ],
                    "star_cnt": 0,
                    "subtitle": "",
                    "title": "Hey Hey You",
                    "uploader": {
                        "enc_uin": "",
                        "headurl": "",
                        "nick": ""
                    },
                    "vid": "002yKdjR0FQo49"
                }
            ],
            "total": 50
        }
    }
    ```

    

#### 1.1.8 搜索排行榜

* 地址：http://127.0.0.1:5000/index

* 请求方式：GET

* 请求参数：type=srank

* 请求示例：

  * 完整地址：`http://127.0.0.1:5000/index?type=srank`

  * 请求响应：

    ```json
    {
        "ip": "127.0.0.1",
        "infos": [
            {
                "cover_pic_url": "http://y.gtimg.cn/music/photo_new/T002R180x180M000000v9LOL2ezYMP_1.jpg",
                "track_id": "465608024",
                "description": "正在热搜",
                "direct_id": 465608024,
                "hotkey_id": "3.2.2:若月亮没来",
                "query": "若月亮没来",
                "score": "10305820",
                "source": 2,
                "title": "若月亮没来",
                "type": 3
            },
            ......
        ]
    }
    ```

    

### 1.2 搜索功能

- 不登录

#### 1.2.1  搜索任意歌曲（可模糊，精确搜索）

- 地址：http://127.0.0.1:5000/search

- 请求方式：GET

- 请求参数：type=song&song=我会好好的&mode=normal

  

  - |  mode  | 说明                                  |
    | :----: | ------------------------------------- |
    | normal | 返回song信息                          |
    | album  | 专辑                                  |
    |   mv   | mv                                    |
    |  all   | 返回所有信息：album，mv，song其它信息 |

    

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/search?type=song&song=我会好好的&mode=normal`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "count": 4,
            "itemlist": [
                {
                    "docid": "487354860",
                    "id": "487354860",
                    "mid": "000Vsz6x4YhS2r",
                    "name": "我会好好的",
                    "singer": "杨宗纬/姚晓棠"
                },
                {
                    "docid": "104116356",
                    "id": "104116356",
                    "mid": "001e1WQu3wiE5C",
                    "name": "我会好好的",
                    "singer": "王心凌"
                },
                {
                    "docid": "105693960",
                    "id": "105693960",
                    "mid": "003vsifF2KmR4N",
                    "name": "我会好好的",
                    "singer": "印子月"
                },
                {
                    "docid": "649511",
                    "id": "649511",
                    "mid": "0033d0am0B4Q7a",
                    "name": "我会好好的",
                    "singer": "伍佰 & China Blue"
                }
            ],
            "name": "单曲",
            "order": 0,
            "type": 1
        }
    }
    ```

    

#### **1.2.2**  搜索任意歌手（可模糊，精确搜索）

- 地址：http://127.0.0.1:5000/search

- 请求方式：GET

- 请求参数：type=singer&singer=周杰伦&mode=normal

  

  - |  mode  | 说明                |
    | :----: | ------------------- |
    | normal | 返回singer信息      |
    |  all   | 返回所有信息：album |

    

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/search?type=singer&singer=周杰伦&mode=normal'`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "docid": "4558",
            "id": "4558",
            "mid": "0025NhlN2yWrP4",
            "name": "周杰伦",
            "pic": "http://y.gtimg.cn/music/photo_new/T001R150x150M0000025NhlN2yWrP4_8.jpg",
            "singer": "周杰伦"
        }
    }
    ```

    

#### **1.2.3**  搜索歌曲详细信息（歌曲文件，歌词）

- 地址：http://127.0.0.1:5000/search

- 请求方式：GET

- 请求参数：type=detail?&song=我会好好的

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/search?type=detail?&song=我会好好的`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "total": 1,
            "songs": [
                {
                    "docid": "487354860",
                    "id": "487354860",
                    "mid": "000Vsz6x4YhS2r",
                    "name": "我会好好的",
                    "singer": "杨宗纬/姚晓棠",
                    "lyric": "W3RpOuaIkeS8muWlveWlveeahCAoTGl2ZSldClthcjrmnajlrpfnuqwv5aea5pmT5qOgXQpbYWw65aSp6LWQ55qE5aOw6Z+z56ys5LqU5a2jIOesrDLmnJ9dCltieTpdCltvZmZzZXQ6MF0KWzAwOjAwLjExXeaIkeS8muWlveWlveeahCAoTGl2ZSkgLSDmnajlrpfnuqwv5aea5pmT5qOgClswMDowMy4zMl3ljp/llLHvvJrnjovlv4Plh4wKWzAwOjA0LjcwXeivje+8muS8jeS9sApbMDA6MDUuMjRd5puy77ya5LyN5L2wClswMDowNS43N13nvJbmm7LvvJrpnqDojZBA6ICz6IKG5bGx55m9ClswMDowNi42Nl3liLbkvZzkurrvvJrliJjljZNA57u05Ly06Z+z5LmQClswMDowNi45Nl3pn7PkuZDmgLvnm5HvvJrliJjljZNA57u05Ly06Z+z5LmQClswMDowNy45MV3pn7Plk43mgLvnm5HvvJrkvZXpo5oKWzAwOjA4LjExXemfs+S5kOa3t+mfs++8muael+aipua0iwpbMDA6MDguMzRd6byT77ya5Y2i54KcQOe7tOS8tOmfs+S5kApbMDA6MDguNTdd5omT5Ye75LmQ77ya5YiY5pWI5p2+QOe7tOS8tOmfs+S5kApbMDA6MDguOTBd6LSd5pav77ya5p2O5Lmd5ZCbQOe7tOS8tOmfs+S5kApbMDA6MDkuMjBd5ZCJ5LuW77ya6YeR5aSpQOe7tOS8tOmfs+S5kC/ltJTkuIflubNA57u05Ly06Z+z5LmQClswMDowOS43Nl3pkqLnkLTvvJrlgoXkuIDls6VA57u05Ly06Z+z5LmQClswMDoxMC4wNV3plK7nm5jvvJrmnY7mtbfpg6FA57u05Ly06Z+z5LmQClswMDoxMC45N11Qcm9ncmFt77ya6YOO5qKT5pyUQOe7tOS8tOmfs+S5kApbMDA6MTEuMjRd5ZKM6Z+z57yW5YaZL+a8lOWUseiuvuiuoe+8muefs+ihjEDnu7TkvLTpn7PkuZAKWzAwOjExLjcwXeWQiOmfs++8muefs+ihjEDnu7TkvLTpn7PkuZAv6ams5oCd6I65QOe7tOS8tOmfs+S5kC/pgqLmmY/kvqhA57u05Ly06Z+z5LmQClswMDoxMy4xMl3lvZXpn7PvvJrpu4Tlj6/niLFA57u05Ly06Z+z5LmQClswMDoxNC4xMV3kuZDpmJ/nu5/nrbnvvJrlvKDkvIrnhLZA57u05Ly06Z+z5LmQClswMDoyMS42Ml3miJHkvJrlpb3lpb3nmoQg6Iqx6L+Y6aaZ6aaZ55qEClswMDoyOS4wMl3ml7bpl7TkuIDnm7Tljrsg5Zue5b+G55yf576O5Li9ClswMDozNi44NF3miJHmmK/mg7PnnYDkvaAg5LiA55u05oOz552A5L2gClswMDo0NC4yNl3kvaDlnKjmiJHlv4PlupXlj5jmiJDkuobnp5jlr4YKWzAxOjA5Ljc1XeS4jeimgeivtOS9oOeIseaIkSDkvaDmg7PmiJEKWzAxOjEzLjc3XeWmguaenOS9oOeahOW/g+mHjCDmsqHmnInov5nkuYjlgZoKWzAxOjE3Ljg3XeWPquaYr+WLieW8uuWcsOaVt+ihjeaIkQpbMDE6MjEuMzRd5oiR55+l6YGT5LqG5Lya5b6I6Zq+5Y+XClswMToyNC42M13miJHopoHkvaDpu5jpu5jotbDkuI3lm57lpLQKWzAxOjI4LjM5XeaIkeS8mua4healmuaYjueZveS9oOimgeeahOaYr+S7gOS5iApbMDE6MzIuNDhd5peg6aG75YuJ5by65Zyw5a6J5oWw5oiRClswMTozNS43Nl3or7TlpYfmgKrnmoTnkIbnlLEKWzAxOjQwLjQzXeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDE6NDUuMTVd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswMTo0OC42OV3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzAxOjUyLjE4XeaIkeefpemBk+Wug+iLpuiLpueahApbMDI6MTAuMjJd5LiN6KaB6K+05L2g54ix5oiR5L2g5oOz5oiRClswMjoxNC4yNl3lpoLmnpzkvaDnmoTlv4Pph4zmsqHmnInov5nkuYjlgZoKWzAyOjE4LjIwXeWPquaYr+WLieW8uuWcsOaVt+ihjeaIkQpbMDI6MjEuNjFd5oiR55+l6YGT5LqG5Lya5b6I6Zq+5Y+XClswMjoyNS4wMF3miJHopoHkvaDpu5jpu5jotbDkuI3lm57lpLQKWzAyOjI4LjkwXeaIkeS8mua4healmuaYjueZveS9oOimgeeahOaYr+S7gOS5iApbMDI6MzIuODVd5peg6aG75YuJ5by65Zyw5a6J5oWw5oiRClswMjozNi4yNl3or7TlpYfmgKrnmoTnkIbnlLEKWzAyOjQwLjgzXeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDI6NDUuNDhd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswMjo0OS4xNl3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzAyOjUyLjcxXeaIkeefpemBk+Wug+iLpuiLpueahApbMDI6NTUuNjJd5Yiw546w5Zyo6L+Y5piv5rex5rex5Zyw5rex5rex5Zyw54ix552A5L2gClswMzowMC4xN13mmK/niLHmg4XnmoTlj4vmg4XnmoTpg73lj6/ku6UKWzAzOjAzLjkxXemCo+aYr+aIkeW/g+S4reeahOW5uOemjwpbMDM6MDcuMzFd5oiR55+l6YGT5a6D6Ium6Ium55qEClswMzoxNS4xMF3miJHkvJrlpb3lpb3nmoQg6Iqx6L+Y6aaZ6aaZ55qEClswMzoyMi4yM13ml7bpl7TkuIDnm7Tljrsg5Zue5b+G55yf576O5Li9ClswMzoyOS44Ml3miJHmmK/mg7PnnYDkvaAg5LiA55u05oOz552A5L2gClswMzozNi43M13kvaDlnKjmiJHlv4PlupUg5Y+Y5oiQ5LqG56eY5a+GClswMzo0Ni44M13liLDnjrDlnKjov5jmmK/mt7Hmt7HlnLDmt7Hmt7HlnLDniLHnnYDkvaAKWzAzOjUxLjUwXeaYr+eIseaDheeahOWPi+aDheeahOmDveWPr+S7pQpbMDM6NTUuMTFd6YKj5piv5oiR5b+D5Lit55qE5bm456aPClswMzo1OC41OF3miJHnn6XpgZPlroPoi6boi6bnmoQKWzA0OjAxLjU3XeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDQ6MDYuMDVd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswNDowOS44OV3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzA0OjEzLjIyXeaIkeefpemBk+Wug+iLpuiLpueahA==",
                    "file_1": "http://ws.stream.qqmusic.qq.com/C400000Vsz6x4YhS2r.m4a?guid=7949132111&vkey=E0208DA142D395DBF1157712552C9053E3D828C0CC912E67AE13844F464FC2F48DF1D3412F0A30835051C87F86639A92407AF5E2EF68F101&uin=&fromtag=120032&src=C400001GsKQ13FwFZL.m4a",
                    "file_2": "http://isure.stream.qqmusic.qq.com/C400000Vsz6x4YhS2r.m4a?guid=7949132111&vkey=E0208DA142D395DBF1157712552C9053E3D828C0CC912E67AE13844F464FC2F48DF1D3412F0A30835051C87F86639A92407AF5E2EF68F101&uin=&fromtag=120032&src=C400001GsKQ13FwFZL.m4a"
                }
            ]
        }
    }
    ```

    * file_1:歌曲文件

    * lyric：base64歌词

#### 1.2.4  搜索歌曲歌曲评论信息

- 地址：http://127.0.0.1:5000/search

- 请求方式：GET

- 请求参数：type=comment?&song=我会好好的

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/search?type=comment?&song=我会好好的`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "total": 4,
            "comments": [
                {
                    "docid": "487354860",
                    "id": "487354860",
                    "mid": "000Vsz6x4YhS2r",
                    "name": "我会好好的",
                    "singer": "杨宗纬/姚晓棠",
                    "data": {
                        "AllowComment": 1,
                        "AllowInsertSong": 0,
                        "IsAuthor": 0,
                        "IsBlacked": 0,
                        "IsAdmin": 0,
                        "NoCopyRight": 0,
                        "ShowMusicianTip": 0,
                        "CommentTip": "",
                        "SubCode": 0,
                        "Msg": "",
                        "TaogeTopicName": "",
                        "CommentList": {
                            "Comments": [
                                {
                                    "Avatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/8Cv5ia6gLcc6yKAZSJALEmnj3CMcybrCbdcQKMCBYzhUglLrAYepme47ianoIn8jKNia38xqic3sKMMne1Mrkia4Leg/132",
                                    "CmId": "1!XP3xIfHWrYmC-KhkO1HCXiQq5HIEqHBkXmtROYHvlalN1-GT3rie65sjLqt.yaUw",
                                    "IdentityPic": "",
                                    "IdentityType": 0,
                                    "State": 1,
                                    "IsPraised": 0,
                                    "Nick": "亚亚",
                                    "PraiseNum": 1,
                                    "PubTime": 1718079153,
                                    "EncryptUin": "oK6kowEAoK4z7ecq7eol7ics7c**",
                                    "VipIcon": "",
                                    "Content": "我是想着你，一直想着你。",
                                    ......
    ```



- 登录

#### **1.2.5**   搜索任意歌曲（可模糊，精确搜索）

- 地址：http://127.0.0.1:5000/ls

- 请求方式：GET

- 请求参数：type=song&song=我会好好的

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/ls?type=song&song=我会好好的`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "song": {
                "list": [
                    {
                        "act": 3,
                        "action": {
                            "alert": 2,
                            "icon2": 0,
                            "icons": 12992510,
                            "msgdown": 0,
                            "msgfav": 0,
                            "msgid": 13,
                            "msgpay": 6,
                            "msgshare": 0,
                            "switch": 16897793,
                            "switch2": 0
                        },
                        "album": {
                            "id": 8389,
                            "mid": "004N0piM0n3kyj",
                            "name": "Cyndi With U",
                            "pmid": "004N0piM0n3kyj_2",
                            "subtitle": "",
                            "time_public": "",
                            "title": "Cyndi With U"
                        },
                        "bpm": 65,
                        "content": "",
                        "desc": "",
                        "desc_hilight": "",
                        "docid": "17898854400176345773",
                        "eq": 0,
                        "es": "",
                        "file": {
                            "b_30s": 3968,
                            "e_30s": 63968,
                            "hires_bitdepth": 0,
                            "hires_sample": 0,
                            "media_mid": "001Yfq5i07HHKg",
                            "size_128mp3": 4329855,
                            "size_192aac": 6525880,
                            "size_192ogg": 6472504,
                            "size_24aac": 0,
                            "size_320mp3": 10824314,
                            "size_360ra": [],
                            "size_48aac": 1637275,
                            "size_96aac": 3299198,
                            "size_96ogg": 3233231,
                            "size_ape": 0,
                            "size_dolby": 0,
                            "size_dts": 0,
                            "size_flac": 31482073,
                            "size_hires": 0,
                            "size_new": [
                                199298020,
                                30897812,
                                79836378,
                                10897699,
                                0,
                                22901697
                            ],
                            "size_try": 960887,
                            "try_begin": 76026,
                            "try_end": 106864,
                            "url": ""
                        },
                        "fnote": 4009,
                        "genre": 0,
                        "grp": [
                            {
                                "act": 3,
                                "action": {
                                    "alert": 2,
                                    "icon2": 0,
                                    "icons": 12992510,
                                    "msgdown": 0,
                                    "msgfav": 0,
                                    "msgid": 13,
                                    "msgpay": 6,
                                    "msgshare": 0,
                                    "switch": 16897793,
                                    "switch2": 0
                                },
                                "album": {
                                    "id": 33921,
                                    "mid": "003e21cr139KMr",
                                    "name": "Red Cyndi 2008新歌+精选",
                                    "pmid": "003e21cr139KMr_1",
                                    "subtitle": "",
                                    "time_public": "",
                                    "title": "Red Cyndi 2008新歌+精选"
                                },
                                "bpm": 65,
                                "content": "",
                                "desc": "",
                                "desc_hilight": "",
                                "docid": "16846885922259582575",
                                "eq": 2,
                                "es": "",
                                "file": {
                                    "b_30s": 0,
                                    "e_30s": 30000,
                                    "hires_bitdepth": 0,
                                    "hires_sample": 0,
                                    "media_mid": "004bNCx73DnQuo",
                                    "size_128mp3": 4333630,
                                    "size_192aac": 6524819,
                                    "size_192ogg": 6473746,
                                    "size_24aac": 0,
                                    "size_320mp3": 10833732,
                                    "size_360ra": [],
                                    "size_48aac": 1636173,
                                    "size_96aac": 3300147,
                                    "size_96ogg": 3232760,
                                    "size_ape": 0,
                                    "size_dolby": 0,
                                    "size_dts": 0,
                                    "size_flac": 31372571,
                                    "size_hires": 0,
                                    "size_new": [
                                        199329655,
                                        31449388,
                                        79301864,
                                        10886597,
                                        0,
                                        22840989
                                    ],
                                    "size_try": 481070,
                                    "try_begin": 76017,
                                    "try_end": 106872,
                                    "url": ""
                                },
                                "fnote": 4009,
                                "genre": 0,
                                "grp": [],
                                "hotness": {
                                    "desc": "",
                                    "icon_url": "",
                                    "jump_type": 0,
                                    "jump_url": ""
                                },
                                "href3": "",
                                "id": 875125,
                                "index_album": 12,
                                "index_cd": 0,
                                "interval": 270,
                                "isonly": 0,
                                "ksong": {
                                    "id": 591,
                                    "mid": "004GUfs63wcels"
                                },
                                "label": "0",
                                "language": 0,
                                "lyric": "",
                                "lyric_hilight": "",
                                "mid": "001Aqgko0SOsmf",
                                "mv": {
                                    "id": 27801,
                                    "name": "",
                                    "title": "",
                                    "vid": "Z0090nXwBaj",
                                    "vt": 0
                                },
                                "name": "我会好好的",
                                "newStatus": 2,
                                "ov": 0,
                                "pay": {
                                    "pay_down": 1,
                                    "pay_month": 1,
                                    "pay_play": 1,
                                    "pay_status": 0,
                                    "price_album": 0,
                                    "price_track": 200,
                                    "time_free": 0
                                },
                                "protect": 0,
                                "sa": 1024,
                                "singer": [
                                    {
                                        "id": 4367,
                                        "mid": "003RVAdJ1YT5AI",
                                        "name": "王心凌",
                                        "pmid": "",
                                        "title": "王心凌",
                                        "type": 1,
                                        "uin": 0
                                    }
                                ],
                                "status": 0,
                                "subtitle": "",
                                "tag": 0,
                                "tid": 0,
                                "time_public": "2008-02-29",
                                "title": "我会好好的",
                                "title_hilight": "<em>我会好好的</em>",
                                "type": 0,
                                "url": "",
                                "version": 0,
                                "vf": [
                                    -9.48868179321289,
                                    0.9999690055847168,
                                    7.58847713470459
                                ],
                                "vi": [
                                    9
                                ],
                                "volume": {
                                    "gain": -9.567999839782715,
                                    "lra": 7.638999938964844,
                                    "peak": 0.9760000109672546
                                },
                                "vs": [
                                    "0638jS3w2CxQU0",
                                    "",
                                    "",
                                    "000EmZvY1ZLVMS",
                                    "001LB9BO3sa3Pm",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "001AotDR3ZQLsp",
                                    ""
                                ]
                            },
                            ....
                        ]
                    }
                ]
            },
            "zhida": {
                "list": [
                    {
                        "album_list": {
                            "items": [
                                {
                                    "id": 51751138,
                                    "mid": "003AoFSd0ZnhS6",
                                    "name": "墨雨云间 影视剧原声带"
                                },
                                {
                                    "id": 49961964,
                                    "mid": "001j6WeT3h02ol",
                                    "name": "不完全自救手册"
                                },
                                {
                                    "id": 44656085,
                                    "mid": "0032v4O53DwrhG",
                                    "name": "星愿"
                                },
                                {
                                    "id": 41382506,
                                    "mid": "001Hkaml3xtsgv",
                                    "name": "BITE BACK"
                                },
                                {
                                    "id": 39532644,
                                    "mid": "004GivMp1JU11o",
                                    "name": "像我们从前"
                                },
                                {
                                    "id": 34631345,
                                    "mid": "004FPNCa1VVGdN",
                                    "name": "中国梦·我的梦"
                                }
                            ]
                        },
                        "custom_info": {
                            "album_num": "31",
                            "extra_desc": "231.8万人关注",
                            "from": "track",
                            "grade": "2",
                            "icon_type": "1",
                            "icon_type2": "8",
                            "icon_type2_schema": "qqmusic://qq.com/ui/openQuickListenSubPage?p=%7B%22Singerid%22%3A4367%2C%22ExtraInfo%22%3A%7B%22from%22%3A%222006%22%7D%7D",
                            "ifpicurl": "https://y.qq.com/music/common/upload/t_cm3_photo_publish/2312628.png",
                            "is_follow": "0",
                            "mid": "003RVAdJ1YT5AI",
                            "mv_num": "880",
                            "one_line_desc": "232万粉丝",
                            "parent_ids": "4367",
                            "pos": "0",
                            "song_num": "337",
                            "tab_id": "song"
                        },
                        "desciption": "歌曲:337 专辑:31 视频:880",
                        "docid": "1:4367",
                        "id": "4367",
                        "jumpurl": "",
                        "mid": "",
                        "pic": "http://y.gtimg.cn/music/photo_new/T001R150x150M000003RVAdJ1YT5AI_5.jpg",
                        "publish_date": "",
                        "title": "王心凌",
                        "track_list": {
                            "items": [
                                {
                                    "id": 95306,
                                    "mid": "0003FhfU2GR1tu",
                                    "name": "爱你"
                                },
                                {
                                    "id": 95312,
                                    "mid": "0037FflR2Za2vs",
                                    "name": "第一次爱的人"
                                },
                                {
                                    "id": 224278998,
                                    "mid": "0004Fq5m1or8Sq",
                                    "name": "大眠"
                                },
                                {
                                    "id": 104116356,
                                    "mid": "001e1WQu3wiE5C",
                                    "name": "我会好好的"
                                },
                                {
                                    "id": 100229,
                                    "mid": "001SU8wX02axe6",
                                    "name": "梦的光点"
                                },
                                {
                                    "id": 103659,
                                    "mid": "002DuNM10g6DnM",
                                    "name": "当你"
                                },
                                {
                                    "id": 144637,
                                    "mid": "0027MbC60rdJwE",
                                    "name": "Da Da Da"
                                },
                                {
                                    "id": 277974768,
                                    "mid": "002bGdwf2KfIFd",
                                    "name": "彩虹的微笑"
                                },
                                {
                                    "id": 100220,
                                    "mid": "004I4kuC30dm5K",
                                    "name": "睫毛弯弯"
                                },
                                {
                                    "id": 95296,
                                    "mid": "002y4hzA2vD6Kl",
                                    "name": "Honey"
                                },
                                {
                                    "id": 4829337,
                                    "mid": "001JisF72vElDo",
                                    "name": "不哭"
                                },
                                {
                                    "id": 390661,
                                    "mid": "004WygSk23dq7M",
                                    "name": "那年夏天宁静的海"
                                },
                                {
                                    "id": 471040594,
                                    "mid": "004KrMkl3saUAI",
                                    "name": "我爱你中国"
                                },
                                {
                                    "id": 392717890,
                                    "mid": "000C7fp50DnK1U",
                                    "name": "中国梦·我的梦"
                                },
                                {
                                    "id": 277974773,
                                    "mid": "000BrbeX02M5qj",
                                    "name": "花的嫁纱"
                                },
                                {
                                    "id": 95315,
                                    "mid": "002oIC7I3EmDxm",
                                    "name": "羽毛"
                                }
                            ]
                        },
                        "type": 1,
                        "vid": "",
                        "video_type": 0
                    }
                ]
            }
        }
    }
    ```



####  **1.2.6**  搜索任意歌手（可模糊，精确搜索）

- 地址：http://127.0.0.1:5000/ls
- 请求方式：GET
- 请求参数：type=singer&singer=周杰伦
- 请求示例：
  - 完整地址：`http://127.0.0.1:5000/ls?type=singer&singer=周杰伦`
  - 请求响应：同上

#### **1.2.7**   搜索歌曲详细信息（歌曲文件，歌词）

- 地址：http://127.0.0.1:5000/ls

- 请求方式：GET

- 请求参数：type=detail?&song=我会好好的

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/ls?type=detail?&song=我会好好的`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "total": 2,
            "song": [
                {
                    "singer": [
                        {
                            "id": 11608,
                            "mid": "003tMm0y0TuewY",
                            "name": "杨宗纬",
                            "pmid": "",
                            "title": "杨宗纬",
                            "type": 0,
                            "uin": 0
                        },
                        {
                            "id": 3521900,
                            "mid": "003lEStu1DXNtz",
                            "name": "姚晓棠",
                            "pmid": "",
                            "title": "姚晓棠",
                            "type": 1,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的 (Live)",
                    "time_public": "2024-05-03",
                    "mv": "https://y.qq.com/n/ryqq/mv/004EKSyH0r5kJG",
                    "lyric": "W3RpOuaIkeS8muWlveWlveeahCAoTGl2ZSldClthcjrmnajlrpfnuqwv5aea5pmT5qOgXQpbYWw65aSp6LWQ55qE5aOw6Z+z56ys5LqU5a2jIOesrDLmnJ9dCltieTpdCltvZmZzZXQ6MF0KWzAwOjAwLjExXeaIkeS8muWlveWlveeahCAoTGl2ZSkgLSDmnajlrpfnuqwv5aea5pmT5qOgClswMDowMy4zMl3ljp/llLHvvJrnjovlv4Plh4wKWzAwOjA0LjcwXeivje+8muS8jeS9sApbMDA6MDUuMjRd5puy77ya5LyN5L2wClswMDowNS43N13nvJbmm7LvvJrpnqDojZBA6ICz6IKG5bGx55m9ClswMDowNi42Nl3liLbkvZzkurrvvJrliJjljZNA57u05Ly06Z+z5LmQClswMDowNi45Nl3pn7PkuZDmgLvnm5HvvJrliJjljZNA57u05Ly06Z+z5LmQClswMDowNy45MV3pn7Plk43mgLvnm5HvvJrkvZXpo5oKWzAwOjA4LjExXemfs+S5kOa3t+mfs++8muael+aipua0iwpbMDA6MDguMzRd6byT77ya5Y2i54KcQOe7tOS8tOmfs+S5kApbMDA6MDguNTdd5omT5Ye75LmQ77ya5YiY5pWI5p2+QOe7tOS8tOmfs+S5kApbMDA6MDguOTBd6LSd5pav77ya5p2O5Lmd5ZCbQOe7tOS8tOmfs+S5kApbMDA6MDkuMjBd5ZCJ5LuW77ya6YeR5aSpQOe7tOS8tOmfs+S5kC/ltJTkuIflubNA57u05Ly06Z+z5LmQClswMDowOS43Nl3pkqLnkLTvvJrlgoXkuIDls6VA57u05Ly06Z+z5LmQClswMDoxMC4wNV3plK7nm5jvvJrmnY7mtbfpg6FA57u05Ly06Z+z5LmQClswMDoxMC45N11Qcm9ncmFt77ya6YOO5qKT5pyUQOe7tOS8tOmfs+S5kApbMDA6MTEuMjRd5ZKM6Z+z57yW5YaZL+a8lOWUseiuvuiuoe+8muefs+ihjEDnu7TkvLTpn7PkuZAKWzAwOjExLjcwXeWQiOmfs++8muefs+ihjEDnu7TkvLTpn7PkuZAv6ams5oCd6I65QOe7tOS8tOmfs+S5kC/pgqLmmY/kvqhA57u05Ly06Z+z5LmQClswMDoxMy4xMl3lvZXpn7PvvJrpu4Tlj6/niLFA57u05Ly06Z+z5LmQClswMDoxNC4xMV3kuZDpmJ/nu5/nrbnvvJrlvKDkvIrnhLZA57u05Ly06Z+z5LmQClswMDoyMS42Ml3miJHkvJrlpb3lpb3nmoQg6Iqx6L+Y6aaZ6aaZ55qEClswMDoyOS4wMl3ml7bpl7TkuIDnm7Tljrsg5Zue5b+G55yf576O5Li9ClswMDozNi44NF3miJHmmK/mg7PnnYDkvaAg5LiA55u05oOz552A5L2gClswMDo0NC4yNl3kvaDlnKjmiJHlv4PlupXlj5jmiJDkuobnp5jlr4YKWzAxOjA5Ljc1XeS4jeimgeivtOS9oOeIseaIkSDkvaDmg7PmiJEKWzAxOjEzLjc3XeWmguaenOS9oOeahOW/g+mHjCDmsqHmnInov5nkuYjlgZoKWzAxOjE3Ljg3XeWPquaYr+WLieW8uuWcsOaVt+ihjeaIkQpbMDE6MjEuMzRd5oiR55+l6YGT5LqG5Lya5b6I6Zq+5Y+XClswMToyNC42M13miJHopoHkvaDpu5jpu5jotbDkuI3lm57lpLQKWzAxOjI4LjM5XeaIkeS8mua4healmuaYjueZveS9oOimgeeahOaYr+S7gOS5iApbMDE6MzIuNDhd5peg6aG75YuJ5by65Zyw5a6J5oWw5oiRClswMTozNS43Nl3or7TlpYfmgKrnmoTnkIbnlLEKWzAxOjQwLjQzXeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDE6NDUuMTVd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswMTo0OC42OV3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzAxOjUyLjE4XeaIkeefpemBk+Wug+iLpuiLpueahApbMDI6MTAuMjJd5LiN6KaB6K+05L2g54ix5oiR5L2g5oOz5oiRClswMjoxNC4yNl3lpoLmnpzkvaDnmoTlv4Pph4zmsqHmnInov5nkuYjlgZoKWzAyOjE4LjIwXeWPquaYr+WLieW8uuWcsOaVt+ihjeaIkQpbMDI6MjEuNjFd5oiR55+l6YGT5LqG5Lya5b6I6Zq+5Y+XClswMjoyNS4wMF3miJHopoHkvaDpu5jpu5jotbDkuI3lm57lpLQKWzAyOjI4LjkwXeaIkeS8mua4healmuaYjueZveS9oOimgeeahOaYr+S7gOS5iApbMDI6MzIuODVd5peg6aG75YuJ5by65Zyw5a6J5oWw5oiRClswMjozNi4yNl3or7TlpYfmgKrnmoTnkIbnlLEKWzAyOjQwLjgzXeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDI6NDUuNDhd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswMjo0OS4xNl3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzAyOjUyLjcxXeaIkeefpemBk+Wug+iLpuiLpueahApbMDI6NTUuNjJd5Yiw546w5Zyo6L+Y5piv5rex5rex5Zyw5rex5rex5Zyw54ix552A5L2gClswMzowMC4xN13mmK/niLHmg4XnmoTlj4vmg4XnmoTpg73lj6/ku6UKWzAzOjAzLjkxXemCo+aYr+aIkeW/g+S4reeahOW5uOemjwpbMDM6MDcuMzFd5oiR55+l6YGT5a6D6Ium6Ium55qEClswMzoxNS4xMF3miJHkvJrlpb3lpb3nmoQg6Iqx6L+Y6aaZ6aaZ55qEClswMzoyMi4yM13ml7bpl7TkuIDnm7Tljrsg5Zue5b+G55yf576O5Li9ClswMzoyOS44Ml3miJHmmK/mg7PnnYDkvaAg5LiA55u05oOz552A5L2gClswMzozNi43M13kvaDlnKjmiJHlv4PlupUg5Y+Y5oiQ5LqG56eY5a+GClswMzo0Ni44M13liLDnjrDlnKjov5jmmK/mt7Hmt7HlnLDmt7Hmt7HlnLDniLHnnYDkvaAKWzAzOjUxLjUwXeaYr+eIseaDheeahOWPi+aDheeahOmDveWPr+S7pQpbMDM6NTUuMTFd6YKj5piv5oiR5b+D5Lit55qE5bm456aPClswMzo1OC41OF3miJHnn6XpgZPlroPoi6boi6bnmoQKWzA0OjAxLjU3XeWIsOeOsOWcqOi/mOaYr+a3sea3seWcsOa3sea3seWcsOeIseedgOS9oApbMDQ6MDYuMDVd5piv54ix5oOF55qE5Y+L5oOF55qE6YO95Y+v5LulClswNDowOS44OV3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzA0OjEzLjIyXeaIkeefpemBk+Wug+iLpuiLpueahA==",
                    "file_1": "http://ws.stream.qqmusic.qq.com/C400000Vsz6x4YhS2r.m4a?guid=4874713108&vkey=E8D442E311DEBFF93F8FEB76774791D337BCD94E79F6FA734B8E412B3432C236A179A1B318A4BEED531855152811EBCD470ACFCC01E06FF6&uin=1152921505285173556&fromtag=120032&src=C400001GsKQ13FwFZL.m4a",
                    "file_2": "http://isure.stream.qqmusic.qq.com/C400000Vsz6x4YhS2r.m4a?guid=4874713108&vkey=E8D442E311DEBFF93F8FEB76774791D337BCD94E79F6FA734B8E412B3432C236A179A1B318A4BEED531855152811EBCD470ACFCC01E06FF6&uin=1152921505285173556&fromtag=120032&src=C400001GsKQ13FwFZL.m4a"
                },
                {
                    "singer": [
                        {
                            "id": 1340104,
                            "mid": "003HO2tE2ibu0A",
                            "name": "彭思亮",
                            "pmid": "",
                            "title": "彭思亮",
                            "type": 0,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的 (Live)",
                    "time_public": "",
                    "mv": "https://y.qq.com/n/ryqq/mv/",
                    "lyric": "W3RpOuaIkeS8muWlveWlveeahCAoTGl2ZSldClthcjrlva3mgJ3kuq5dClthbDpdCltieTpdCltvZmZzZXQ6MF0KWzAwOjAwLjAwXeaIkeS8muWlveWlveeahCAoTGl2ZSkgLSDlva3mgJ3kuq4KWzAwOjAwLjA1Xeivje+8muS8jeS9sApbMDA6MDAuMTFd5puy77ya5LyN5L2wClswMDowMC4xN13ljp/llLHvvJrnjovlv4Plh4wKWzAwOjAwLjIzXeaIkeimgeS9oOm7mOm7mOi1sApbMDA6MDIuMTFdClswMDowMi42NV3kuI3lm57lpLQKWzAwOjA0LjA4XeaIkeS8mua4healmuaYjueZveS9oOimgeeahOaYr+S7gOS5iApbMDA6MDguNTNd5LiN6K645YuJ5by655qE5a6J5oWw5oiRClswMDoxMi4yMV3or7TlpYfmgKrnmoTnkIbnlLEKWzAwOjE1LjIyXeWIsOeOsOWcqOi/mOaYrwpbMDA6MTYuMzdd5rex5rex55qE5rex5rex55qE54ix552A5L2gClswMDoxOS40MF0KWzAwOjIwLjAzXeaYr+eIseaDheeahOWPi+aDheeahOmDveWPr+S7pQpbMDA6MjMuNDJdClswMDoyNC4wMV3pgqPmmK/miJHlv4PkuK3nmoTlubjnpo8KWzAwOjI3LjcxXeaIkeefpemBk+S7luiLpuiLpueahA==",
                    "file_1": "http://ws.stream.qqmusic.qq.com/C40000140OL43mjx9H.m4a?guid=4874713108&vkey=F19E4E0327B4C8A2C9DCEFAC3EEA64774688E2AD17D538AD8B46C5E5E016521C2A23A5C631426DAD15DAA938514CE3A5C06F71D059C2240D&uin=1152921505285173556&fromtag=120032",
                    "file_2": "http://isure.stream.qqmusic.qq.com/C40000140OL43mjx9H.m4a?guid=4874713108&vkey=F19E4E0327B4C8A2C9DCEFAC3EEA64774688E2AD17D538AD8B46C5E5E016521C2A23A5C631426DAD15DAA938514CE3A5C06F71D059C2240D&uin=1152921505285173556&fromtag=120032"
                }
            ]
        }
    }
    ```

    * file_1:歌曲文件

    * lyric：base64歌词

#### 1.2.8   搜索歌曲歌评论曲信息

- 地址：http://127.0.0.1:5000/ls
- 请求方式：GET
- 请求参数：type=comment?&song=我会好好的
- 请求示例：
  - 完整地址：`http://127.0.0.1:5000/ls?type=comment?&song=我会好好的`
  - 请求响应：

#### **1.2.9**   搜索任意歌曲MV（可模糊，精确搜索，mp4文件）

- 地址：http://127.0.0.1:5000/ls

- 请求方式：GET

- 请求参数：type=mv?&song=我会好好的

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/ls?type=mv?&song=我会好好的`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": {
            "total": 4,
            "mv": [
                {
                    "singer": [
                        {
                            "id": 4367,
                            "mid": "003RVAdJ1YT5AI",
                            "name": "王心凌",
                            "pmid": "",
                            "title": "王心凌",
                            "type": 1,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的",
                    "time_public": "2005-12-27",
                    "url": [
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/2BB5736C0FEA93EA7339572FC58C2602265E2023F9ED7B529711C21A915431907A4E58FF4E7F2A7035087577C88B60AAZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9814.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9814.mp4",
                                "https://mv.music.tc.qq.com/2BB5736C0FEA93EA7339572FC58C2602265E2023F9ED7B529711C21A915431907A4E58FF4E7F2A7035087577C88B60AAZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9814.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9814.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9814.mp4",
                            "vkey": "2BB5736C0FEA93EA7339572FC58C2602265E2023F9ED7B529711C21A915431907A4E58FF4E7F2A7035087577C88B60AAZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 10,
                            "m3u8": "",
                            "newFileType": 9814,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 12235532
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/5CFD08B6A4314F49AA6325A188E031966CE68518C87BBA809B01B067B0F6CFD047951D3F5DF6B6385A76DD2EA5535566ZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9824.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9824.mp4",
                                "https://mv.music.tc.qq.com/5CFD08B6A4314F49AA6325A188E031966CE68518C87BBA809B01B067B0F6CFD047951D3F5DF6B6385A76DD2EA5535566ZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9824.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9824.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9824.mp4",
                            "vkey": "5CFD08B6A4314F49AA6325A188E031966CE68518C87BBA809B01B067B0F6CFD047951D3F5DF6B6385A76DD2EA5535566ZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 20,
                            "m3u8": "",
                            "newFileType": 9824,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 22947039
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/4B231A493F789B5C7CA3437D7152AF8625044EB3750FF08C725D0747CDB1F76B2678D36498CFF3D643C5E6C154F1E579ZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9834.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9834.mp4",
                                "https://mv.music.tc.qq.com/4B231A493F789B5C7CA3437D7152AF8625044EB3750FF08C725D0747CDB1F76B2678D36498CFF3D643C5E6C154F1E579ZZqqmusic_default/qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9834.mp4?fname=qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9834.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53xyaaoaaamyak6ol6yvrvjpqaa67aab2a.f9834.mp4",
                            "vkey": "4B231A493F789B5C7CA3437D7152AF8625044EB3750FF08C725D0747CDB1F76B2678D36498CFF3D643C5E6C154F1E579ZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 30,
                            "m3u8": "",
                            "newFileType": 9834,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 40060599
                        }
                    ]
                },
                {
                    "singer": [
                        {
                            "id": 72148,
                            "mid": "004ALksm29seAk",
                            "name": "印子月",
                            "pmid": "",
                            "title": "印子月",
                            "type": 1,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的",
                    "time_public": "2016-03-16",
                    "url": [
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/1A12E33902628CC37435B5CABD4979F038E729EF25054240A23A38811137CD820FA22871FA904E081BABE84EB9B5AEBDZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9814.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9814.mp4",
                                "https://mv.music.tc.qq.com/1A12E33902628CC37435B5CABD4979F038E729EF25054240A23A38811137CD820FA22871FA904E081BABE84EB9B5AEBDZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9814.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9814.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9814.mp4",
                            "vkey": "1A12E33902628CC37435B5CABD4979F038E729EF25054240A23A38811137CD820FA22871FA904E081BABE84EB9B5AEBDZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 10,
                            "m3u8": "",
                            "newFileType": 9814,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 12011416
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/62913D3D878642FDC9CF6015DC912C1653F68956CA57FDBA12F9BD995588162D7B5247019FD29FB2176084CBAEC6B69FZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9824.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9824.mp4",
                                "https://mv.music.tc.qq.com/62913D3D878642FDC9CF6015DC912C1653F68956CA57FDBA12F9BD995588162D7B5247019FD29FB2176084CBAEC6B69FZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9824.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9824.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9824.mp4",
                            "vkey": "62913D3D878642FDC9CF6015DC912C1653F68956CA57FDBA12F9BD995588162D7B5247019FD29FB2176084CBAEC6B69FZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 20,
                            "m3u8": "",
                            "newFileType": 9824,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 32067679
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/187DADB4DBD67BEF1CFDDD0FF4603A9BC5FA5465F43416E1B98F9E5820A73C4A861C3A9B459094874A952C247DAB2074ZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9834.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9834.mp4",
                                "https://mv.music.tc.qq.com/187DADB4DBD67BEF1CFDDD0FF4603A9BC5FA5465F43416E1B98F9E5820A73C4A861C3A9B459094874A952C247DAB2074ZZqqmusic_default/qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9834.mp4?fname=qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9834.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0a6bkuwjbeavcsqmaehqedafaedfhu4f3mwlogvfiydq4bypb4bq.f9834.mp4",
                            "vkey": "187DADB4DBD67BEF1CFDDD0FF4603A9BC5FA5465F43416E1B98F9E5820A73C4A861C3A9B459094874A952C247DAB2074ZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 30,
                            "m3u8": "",
                            "newFileType": 9834,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 73555895
                        }
                    ]
                },
                {
                    "singer": [
                        {
                            "id": 11608,
                            "mid": "003tMm0y0TuewY",
                            "name": "杨宗纬",
                            "pmid": "",
                            "title": "杨宗纬",
                            "type": 0,
                            "uin": 0
                        },
                        {
                            "id": 3521900,
                            "mid": "003lEStu1DXNtz",
                            "name": "姚晓棠",
                            "pmid": "",
                            "title": "姚晓棠",
                            "type": 1,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的 (Live)",
                    "time_public": "2024-05-03",
                    "url": [
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/F00D57C9BEFBAC7AB9798BA05C40EDF1893687628E26D97504CF6ABB25A2DE4EDEC001E23D77B702732B9E83DE174D8DZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9814.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9814.mp4",
                                "https://mv.music.tc.qq.com/F00D57C9BEFBAC7AB9798BA05C40EDF1893687628E26D97504CF6ABB25A2DE4EDEC001E23D77B702732B9E83DE174D8DZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9814.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9814.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9814.mp4",
                            "vkey": "F00D57C9BEFBAC7AB9798BA05C40EDF1893687628E26D97504CF6ABB25A2DE4EDEC001E23D77B702732B9E83DE174D8DZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 10,
                            "m3u8": "",
                            "newFileType": 9814,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 4974513
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/9D082B515A099F86DDC204A2E8F2A906C2B7E1853C7BD7E368859FDA1A175C53A05A1F76C4BDE386BACF55F19AA97D35ZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9824.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9824.mp4",
                                "https://mv.music.tc.qq.com/9D082B515A099F86DDC204A2E8F2A906C2B7E1853C7BD7E368859FDA1A175C53A05A1F76C4BDE386BACF55F19AA97D35ZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9824.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9824.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9824.mp4",
                            "vkey": "9D082B515A099F86DDC204A2E8F2A906C2B7E1853C7BD7E368859FDA1A175C53A05A1F76C4BDE386BACF55F19AA97D35ZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 20,
                            "m3u8": "",
                            "newFileType": 9824,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 10730701
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/D76480EA6640C2AE45D82216E65847656258DC21BE2F011959BA56E382FBC6996BEBAFB7F1BA5A88DFE4CEA54F589680ZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9834.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9834.mp4",
                                "https://mv.music.tc.qq.com/D76480EA6640C2AE45D82216E65847656258DC21BE2F011959BA56E382FBC6996BEBAFB7F1BA5A88DFE4CEA54F589680ZZqqmusic_default/qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9834.mp4?fname=qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9834.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0b53auaikaaaoeais2zv65tfibiaqucqbbka.f9834.mp4",
                            "vkey": "D76480EA6640C2AE45D82216E65847656258DC21BE2F011959BA56E382FBC6996BEBAFB7F1BA5A88DFE4CEA54F589680ZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 30,
                            "m3u8": "",
                            "newFileType": 9834,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 17393176
                        }
                    ]
                },
                {
                    "singer": [
                        {
                            "id": 5943,
                            "mid": "004OTPJW1frR0y",
                            "name": "伍佰 & China Blue",
                            "pmid": "",
                            "title": "伍佰 & China Blue",
                            "type": 2,
                            "uin": 0
                        }
                    ],
                    "title": "我会好好的",
                    "time_public": "2009-12-18",
                    "url": [
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/4B198B6282B6D77ADF89171A6B767D56C8C24CAD212EE3DF7C30557B7205084AC89ED10C8FB9C4F24E3AB735073E0A8CZZqqmusic_default/qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9814.mp4?fname=qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9814.mp4",
                                "https://mv.music.tc.qq.com/4B198B6282B6D77ADF89171A6B767D56C8C24CAD212EE3DF7C30557B7205084AC89ED10C8FB9C4F24E3AB735073E0A8CZZqqmusic_default/qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9814.mp4?fname=qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9814.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9814.mp4",
                            "vkey": "4B198B6282B6D77ADF89171A6B767D56C8C24CAD212EE3DF7C30557B7205084AC89ED10C8FB9C4F24E3AB735073E0A8CZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 10,
                            "m3u8": "",
                            "newFileType": 9814,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 14214214
                        },
                        {
                            "url": [
                                "https://mv6.music.tc.qq.com/",
                                "https://mv.music.tc.qq.com/"
                            ],
                            "freeflow_url": [
                                "https://mv6.music.tc.qq.com/7BB1074F35E9CF4D2568C08E9733E3749591D9C1CBADD993CBE7339CE6C879A89FFD08C2A1A166434F0BABBE283F390DZZqqmusic_default/qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9824.mp4?fname=qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9824.mp4",
                                "https://mv.music.tc.qq.com/7BB1074F35E9CF4D2568C08E9733E3749591D9C1CBADD993CBE7339CE6C879A89FFD08C2A1A166434F0BABBE283F390DZZqqmusic_default/qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9824.mp4?fname=qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9824.mp4"
                            ],
                            "comm_url": [],
                            "cn": "qmmv_0a6bui67a4efgribbehqgayeaqbvzu3svltolhxliucqadymbifq.f9824.mp4",
                            "vkey": "7BB1074F35E9CF4D2568C08E9733E3749591D9C1CBADD993CBE7339CE6C879A89FFD08C2A1A166434F0BABBE283F390DZZqqmusic_default",
                            "expire": 86400,
                            "code": 0,
                            "filetype": 20,
                            "m3u8": "",
                            "newFileType": 9824,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 58775627
                        },
                        {
                            "url": [],
                            "freeflow_url": [],
                            "comm_url": [],
                            "cn": "",
                            "vkey": "",
                            "expire": 86400,
                            "code": 2000,
                            "filetype": 30,
                            "m3u8": "",
                            "newFileType": 30,
                            "format": 264,
                            "testCdn": 0,
                            "urlPath": "",
                            "videoType": 0,
                            "hlsFileFormat": "",
                            "fileSize": 0
                        }
                    ]
                }
            ]
        }
    }
    ```

  - freeflow_url:mp4文件

### 1.3 歌手

-  分类歌手（可分类，分页）

- 地址：http://127.0.0.1:5000/singer

- 请求方式：GET

- 请求参数：type='all'&category=&page=1

  - type:只有all,area,genre,index,sex四种，当为all时，其它三个不管，即全部不分类

    

  - ```python
    {
        "area": [
            {
                "id": -100,
                "name": "全部"
            },
            {
                "id": 200,
                "name": "内地"
            },
            {
                "id": 2,
                "name": "港台"
            },
            {
                "id": 5,
                "name": "欧美"
            },
            {
                "id": 4,
                "name": "日本"
            },
            {
                "id": 3,
                "name": "韩国"
            }
        ],
        "genre": [
            {
                "id": -100,
                "name": "全部"
            },
            {
                "id": 7,
                "name": "流行"
            },
            {
                "id": 3,
                "name": "说唱"
            },
            {
                "id": 19,
                "name": "国风"
            },
            {
                "id": 4,
                "name": "摇滚"
            },
            {
                "id": 2,
                "name": "电子"
            },
            {
                "id": 8,
                "name": "民谣"
            },
            {
                "id": 11,
                "name": "R\u0026B"
            },
            {
                "id": 37,
                "name": "民族乐"
            },
            {
                "id": 93,
                "name": "轻音乐"
            },
            {
                "id": 14,
                "name": "爵士"
            },
            {
                "id": 33,
                "name": "古典"
            },
            {
                "id": 13,
                "name": "乡村"
            },
            {
                "id": 10,
                "name": "蓝调"
            }
        ],
        "index": [
            {
                "id": -100,
                "name": "全部"
            },
            {
                "id": 1,
                "name": "A"
            },
            {
                "id": 2,
                "name": "B"
            },
            {
                "id": 3,
                "name": "C"
            },
            {
                "id": 4,
                "name": "D"
            },
            {
                "id": 5,
                "name": "E"
            },
            {
                "id": 6,
                "name": "F"
            },
            {
                "id": 7,
                "name": "G"
            },
            {
                "id": 8,
                "name": "H"
            },
            {
                "id": 9,
                "name": "I"
            },
            {
                "id": 10,
                "name": "J"
            },
            {
                "id": 11,
                "name": "K"
            },
            {
                "id": 12,
                "name": "L"
            },
            {
                "id": 13,
                "name": "M"
            },
            {
                "id": 14,
                "name": "N"
            },
            {
                "id": 15,
                "name": "O"
            },
            {
                "id": 16,
                "name": "P"
            },
            {
                "id": 17,
                "name": "Q"
            },
            {
                "id": 18,
                "name": "R"
            },
            {
                "id": 19,
                "name": "S"
            },
            {
                "id": 20,
                "name": "T"
            },
            {
                "id": 21,
                "name": "U"
            },
            {
                "id": 22,
                "name": "V"
            },
            {
                "id": 23,
                "name": "W"
            },
            {
                "id": 24,
                "name": "X"
            },
            {
                "id": 25,
                "name": "Y"
            },
            {
                "id": 26,
                "name": "Z"
            },
            {
                "id": 27,
                "name": "#"
            }
        ],
        "sex": [
            {
                "id": -100,
                "name": "全部"
            },
            {
                "id": 0,
                "name": "男"
            },
            {
                "id": 1,
                "name": "女"
            },
            {
                "id": 2,
                "name": "组合"
            }
        ]
    }
    ```

    

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/singer?type=all&category=''&page=1`

  - 请求响应：

  - ```json
    {
        "ip": "127.0.0.1",
        "infos": [
            {
                "area_id": 1,
                "singer_id": 204664,
                "country_id": 0,
                "singer_name": "鹿晗",
                "country": "",
                "other_name": "",
                "singer_mid": "001SqkF53OEhdO",
                "spell": "luhan",
                "trend": 0,
                "singer_pmid": "",
                "concernNum": 0,
                "singer_pic": "http://y.gtimg.cn/music/photo_new/T001R300x300M000001SqkF53OEhdO.webp"
            },
            {
                "area_id": 0,
                "singer_id": 235,
                "country_id": 0,
                "singer_name": "李克勤",
                "country": "",
                "other_name": "Hacken Lee",
                "singer_mid": "003nS2v740Lxcw",
                "spell": "likeqin",
                "trend": 0,
                "singer_pmid": "",
                "concernNum": 0,
                "singer_pic": "http://y.gtimg.cn/music/photo_new/T001R300x300M000003nS2v740Lxcw.webp"
            },
            {
                "area_id": 1,
                "singer_id": 19624,
                "country_id": 0,
                "singer_name": "郁可唯",
                "country": "",
                "other_name": "Yisa Yu",
                "singer_mid": "000NUoMp2WAEpO",
                "spell": "yukewei",
                "trend": 0,
                "singer_pmid": "",
                "concernNum": 0,
                "singer_pic": "http://y.gtimg.cn/music/photo_new/T001R300x300M000000NUoMp2WAEpO.webp"
            },
            
            ......
            {
                "area_id": 1,
                "singer_id": 1518533,
                "country_id": 0,
                "singer_name": "希林娜依高",
                "country": "",
                "other_name": "Curley G",
                "singer_mid": "000PJRig3WnHYX",
                "spell": "xilinnayi·gao",
                "trend": 0,
                "singer_pmid": "",
                "concernNum": 0,
                "singer_pic": "http://y.gtimg.cn/music/photo_new/T001R300x300M000000PJRig3WnHYX.webp"
            }
        ]
    }
    ```

* 其它：
  * http://127.0.0.1:5000/singer?type=area&category=内地&page=1

### 1.4 歌曲排行榜

-  分类排行榜歌曲（可分类，分页）

- 地址：http://127.0.0.1:5000/ranks

- 请求方式：GET

- 请求参数：keyword=流行指数榜

  - ```python
    {3: '欧美榜', 4: '流行指数榜', 5: '内地榜', 6: '港台榜', 16: '韩国榜', 17: '日本榜',
    23: '畅销专辑', 26: '热歌榜', 27: '新歌榜', 28: '网络歌曲榜', 29: '影视金曲榜', 36: 'K歌金曲榜',
    52: '腾讯音乐人原创榜', 53: '机车', 57: '电音榜', 58: '说唱榜', 59: '香港地区榜', 60: '抖快榜',
    61: '台湾地区榜', 62: '飙升榜', 63: 'DJ舞曲榜', 64: '综艺新歌榜', 65: '国风热歌榜', 66: 'ACG新歌榜',
    67: '听歌识曲榜', 70: '达人音乐榜', 71: '', 72: '动漫音乐榜', 73: '游戏音乐榜',
    74: 'Q音快手榜', 75: '有声榜', 76: '音乐巅峰榜', 77: '扑通指数榜', 78: '国乐榜',
    82: '达人音乐榜', 103: '台湾Hito中文榜', 105: '日本公信榜', 106: '韩国Mnet榜', 107: '英国UK榜',
    108: '美国公告牌榜', 113: '香港电台榜', 114: '香港商台榜', 121: '美国公告牌榜', 122: '美国公告牌榜',
    123: '美国热门音乐榜', 126: 'JOOX本地热播榜', 127: '台湾KKBOX榜', 128: 'YouTube音乐排行榜',
    129: '韩国Melon榜', 130: '香港TVB劲歌金榜', 131: '校园音乐人排行榜', 132: 'indie图鉴榜',
    133: '音乐指数榜', 134: '畅销实体专辑', 135: '巅峰潮流榜'}
    ```

    

- 请求示例：

  - 完整地址：`http://127.0.0.1:5000/ranks?keyword=流行指数榜`
  - 请求响应：

### 1.5 歌曲

-  分类歌曲（可分类，分页）

- 地址：http://127.0.0.1:5000/song

- 请求方式：GET

- 请求参数：keyword=治愈

  - ```python
    {'官方歌单': 3317, '音乐人在听': 1069, '达人心选': 3900, '': 199, '国语': 1, '粤语': 146, '英语': 3,
    '韩语': 4,
    '日语': 5, '小语种': 6, '治愈': 124, '快乐': 8, '寂寞': 9, '思念': 119, '活力塑形': 11, '伤感': 74,
    '安静': 13,
    '精选': 62, '超级猩猩': 15, '励志': 109, '宣泄': 17, '获奖原声': 18, '有氧燃脂': 19, '甜蜜': 167,
    '历年经典': 21, '体能突破': 22, '在路上': 23, '工作': 24, '身心焕活': 25, '睡前': 27, '减压': 28,
    '运动': 133,
    '烛光': 30, '学习': 31, '夜店': 32, '派对': 33, '散步': 34, '约会': 35, '旅行': 99, '阅读': 37,
    '打游戏': 38,
    '校园': 39, '流行': 40, '摇滚': 41, '说唱': 42, 'R&B': 43, '乡村': 44, '电子': 45, '爵士': 46,
    '古典': 148,
    '民谣': 48, '轻音乐': 49, '舞曲': 50, '布鲁斯': 51, '拉丁': 52, '新世纪': 53, '中文儿歌': 54,
    '高考专区': 55,
    '慢摇舞曲': 56, 'Playlist by': 57, '广场舞': 58, '经典老歌': 59, 'MC喊麦': 60, '古风': 61,
    '儿歌精选': 63,
    'KTV金曲': 138, '革命歌曲': 145, '小清新': 106, '今晚蹦迪': 81, '中国风': 68, '米兰': 69, '里约': 70,
    '情歌': 71, '胎教': 129, '游戏': 73, '下午茶': 75, '洗脑神曲': 76, '街舞': 77, '导演万岁': 79,
    '经典': 80,
    '我是歌手4': 83, '中国好歌曲': 85, '电音舞曲': 86, '阿卡贝拉': 87, '格莱美': 89, '情人节': 91,
    '奥斯卡': 92,
    '城市': 93, '巅峰榜': 94, '现场音乐': 95, '毕业季': 104, '音乐调频': 98, '欧美综艺': 100,
    '内地综艺': 101,
    '韩国综艺': 102, '日本综艺': 103, '致青春': 105, '背景音乐': 107, '搞笑音乐': 108, '经典番剧': 112,
    '同人音乐': 111, '闽南语': 113, '浩室舞曲': 114, '氛围音乐': 115, '世界杯': 116, '感性': 118,
    '儿童故事': 120,
    '翻唱': 121, '对唱': 122, '音乐节': 123, '熬夜': 128, '编程': 127, '独家金曲': 130, '五月推荐': 131,
    '圣诞节': 135, '人气音乐节': 136, '艺人推荐': 137, '英文儿歌': 139, '70年代': 140, '80年代': 156,
    '90年代': 157,
    '六十年代': 143, '00年代': 144, '粤语精选': 147, '法语': 149, '德语': 150, '意大利语': 151, '购物': 152,
    '足球': 153, '新年好': 154, 'Blue Note': 155, '钢琴': 158, '小提琴': 159, '吉他': 160, '萨克斯': 161,
    '古筝': 162, '笛子': 163, '独立原创': 164, '四月推荐': 165, '华语民谣': 166}
    ```



- 请求示例：
  - 完整地址：`http://127.0.0.1:5000/song?keyword=治愈`
  - 请求响应：

