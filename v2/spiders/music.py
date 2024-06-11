import asyncio, os, time
import aiohttp
import json
from fake_useragent import UserAgent
from lxml import etree
import execjs


class QQMusic(object):
    """
    QQ音乐爬虫
    """

    def __init__(self):
        self.index = 'https://y.qq.com'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://cn.bing.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": UserAgent().random
        }

        self.cookies = {
            "pgv_pvid": "7211015108",
            "fqm_pvqid": "783e298c-2893-4d0c-87a0-6681acd57109",
            "fqm_sessionid": "53e07048-c3bc-4944-b84b-f81874b3e090",
            "pgv_info": "ssid=s9571182682",
            "ts_last": "y.qq.com/",
            "ts_refer": "cn.bing.com/",
            "ts_uid": "6589886720"
        }
        self.today = time.localtime()
        self.day = str(self.today.tm_year) + str(self.today.tm_mon) + str(self.today.tm_mday)
        self.yestoday = str(self.today.tm_year) + str(self.today.tm_mon) + str(self.today.tm_mday - 1)

    async def get_sign(self, data):
        """
        sign值逆向函数
        :param data:请求体参数
        :return: sign值
        """
        with open('../src/js/qq_music.js', 'r', encoding='utf-8') as file:
            js_code = file.read()

        if not data:
            print(f'参数不能为空，现在使用测试data')
            data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"28644833441163176","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_2":{"module":"music.paycenterapi.LoginStateVerificationApi","method":"GetChargeAccount","param":{"appid":"mlive"}}}'
        sign = execjs.compile(js_code).call('getSign', data)

        return sign

    async def handle_index_html(self):
        """
        处理首页HTML请求函数：此次使用静态化处理，即保存成html
        :return: None
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.index, headers=self.headers, cookies=self.cookies) as response:
                if response.status == 200:
                    html = await response.text()
                    with open(f'../src/html/index_{self.day}.html', 'w', encoding='utf-8') as file:
                        file.write(html)

    async def handle_index_html_file(self):
        """
        处理index_{day}.html文件
        :return: 解析后的HTML
        """
        if os.path.exists(f'../src/html/index_{self.yestoday}.html'):
            os.remove(f'../src/html/index_{self.yestoday}.html')
        if not os.path.exists(f'../src/html/index_{self.day}.html'):
            await self.handle_index_html()
        with open(f'../src/html/index_{self.day}.html', 'r', encoding='utf-8') as file:
            html = file.read()
            return etree.HTML(html)

    async def index_links(self):
        """
        首页链接
        :param html: 解析后的HTML
        :return: None
        """
        # 首页链接
        html = await self.handle_index_html_file()
        if html:
            links = {}
            navs = html.xpath(
                '//a[@class="top_nav__link top_nav__link--current" or @class="top_nav__link" or @class="top_subnav__link" or @class="js_other_link"]')
            for nav in navs:
                title = nav.text
                link = self.index + nav.attrib['href']
                links[title] = link
            return links

    async def index_hots(self):
        """
        歌单推荐
        :param html:解析后的HTML
        :return:None
        """
        html = await self.handle_index_html_file()
        if html:
            hots = {}
            infos = html.xpath('//img[@class="playlist__pic"]')
            bfs = html.xpath('//div[@class="playlist__other"]')
            links = html.xpath('//span[@class="playlist__title_txt"]/a/@href')
            i = 1
            for info, bf, link in zip(infos, bfs, links):
                hots[i] = {'title': info.xpath('./@alt')[0], 'image': info.xpath('./@src')[0],
                           'bfl': bf.xpath('./text()')[0], 'link': self.index + link}
                i += 1
            return hots

    async def index_new_songs(self):
        """
        新歌首发
        :param html:解析后的HTML
        :return:None
        """
        html = await self.handle_index_html_file()
        if html:
            new_songs = {}
            infos = html.xpath('//img[@class="debutlist__pic"]')
            times = html.xpath('//div[@class="debutlist__time c_tx_thin"]')
            links = html.xpath('//p[@class="debutlist__author"]/a/@href')
            signers = html.xpath('//p[@class="debutlist__author"]/a/text()')
            i = 1
            for info, time, link, singer in zip(infos, times, links, signers):
                new_songs[i] = {'title': info.xpath('./@alt')[0], 'image': info.xpath('./@src')[0],
                                'time': time.xpath('./text()')[0], 'link': self.index + link, 'signer': singer}
                i += 1
            return new_songs

    async def handle_index_other_infos(self):
        """
        首页其它信息处理函数，保存JSON数据到本地
        :return:None
        """

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
                "module": "music.musicsearch.HotkeyService",
                "method": "GetHotkeyForQQMusicMobile",
                "param": {
                    "searchid": "32779615639997617",
                    "remoteplace": "txt.yqq.top",
                    "from": "yqqweb"
                }
            },
            "req_2": {
                "module": "music.musicHall.MusicHallPlatformSvr",
                "method": "GetFocus",
                "param": {}
            },
            "req_3": {
                "module": "newalbum.NewAlbumServer",
                "method": "get_new_album_area",
                "param": {}
            },
            "req_4": {
                "module": "newalbum.NewAlbumServer",
                "method": "get_new_album_info",
                "param": {
                    "area": 1,
                    "sin": 0,
                    "num": 20
                }
            },
            "req_5": {
                "module": "musicToplist.ToplistInfoServer",
                "method": "GetAll",
                "param": {}
            },
            "req_6": {
                "module": "MvService.MvInfoProServer",
                "method": "GetNewMv",
                "param": {
                    "style": 0,
                    "tag": 0,
                    "start": 0,
                    "size": 40
                }
            },
            "req_7": {
                "module": "music.paycenterapi.LoginStateVerificationApi",
                "method": "GetChargeAccount",
                "param": {
                    "appid": "mlive"
                }
            }
        }
        data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        params = {
            "_": str(int(time.time() * 1000)),
            "sign": await self.get_sign(data)
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=self.headers, cookies=self.cookies, params=params,
                                    data=data) as response:
                if response.status == 200:
                    if response.headers.get('content-type') == 'application/json':
                        html = await response.json()
                    else:
                        html = await response.text()
                        html = eval(html.replace('null', '0').replace('\\/', '/'))

                    with open(f'../src/json/index_{self.day}.json', 'w', encoding='utf-8') as file:
                        file.write(json.dumps(html))

    async def handle_index_other_infos_file(self):
        """
        处理首页其它文件信息
        :return: JSON数据
        """
        if os.path.exists(f'../src/json/index_{self.yestoday}.json'):
            os.remove(f'../src/json/index_{self.yestoday}.json')
        if not os.path.exists(f'../src/json/index_{self.day}.json'):
            await self.handle_index_other_infos()
        with open(f'../src/json/index_{self.day}.json', 'r', encoding='utf-8') as file:
            html = file.read()
            return json.loads(html)

    async def index_wonder(self):
        """
        精彩推荐
        :return:
        """
        html = await self.handle_index_other_infos_file()
        if html:
            wonder = []
            infos = html['req_2']['data']['shelf']['v_niche'][0]
            infos = infos['v_card']
            for info in infos:
                wonder.append(
                    {'jumptype': info['jumptype'], 'id': info['id'], 'subid': info['subid'], 'title': info['title'],
                     'cover': info['cover'], 'tjreport': info['tjreport'], 'CfgID': info['miscellany']['CfgID'],
                     'focusid': info['miscellany']['focusid'], 'tag': info['miscellany']['tag'],
                     'scheme': info['scheme']})
            return wonder

    async def index_albums(self):
        """新碟首发"""
        html = await self.handle_index_other_infos_file()
        if html:
            albums = html['req_4']['data']['albums']
            return albums

    async def index_ranks(self):
        """歌曲排行榜"""
        html = await self.handle_index_other_infos_file()
        if html:
            ranks = html['req_5']['data']['group']
            return ranks

    async def index_mv(self):
        """mv"""
        html = await self.handle_index_other_infos_file()
        if html:
            mv = html['req_6']['data']
            return mv

    async def index_search_ranks(self):
        """搜索排行榜"""
        html = await self.handle_index_other_infos_file()
        if html:
            search = []
            infos = html['req_1']['data']['vec_hotkey']
            for info in infos:
                search.append({'cover_pic_url': info['cover_pic_url'], 'track_id': info['custom_param']['track_id'],
                               'description': info['description'], 'direct_id': info['direct_id'],
                               'hotkey_id': info['hotkey_id'], 'query': info['query'], 'score': info['score'],
                               'source': info['source'], 'title': info['title'], 'type': info['type']})
            return search

    async def handle_index_search_info(self, keyword):
        """
        首页搜索:支持歌曲，歌手，用户,MV搜索，全匹配和模糊匹配
        """
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
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers, cookies=cookies, params=params) as response:
                if response.status == 200:
                    if response.headers.get('content-type') == 'application/json':
                        html = await response.json()

                    else:
                        html = await response.text()
                        html = eval(html.replace('null', '0').replace('\\/', '/'))
                    info = html['data']
                    return info

    async def index_search_singer(self, singer, type='normal'):
        info = await self.handle_index_search_info(singer)
        if info:
            if type == 'all':
                return info
            else:
                return info['singer']['itemlist'][0]

    async def index_search_song(self, song, type='normal'):
        info = await self.handle_index_search_info(song)
        if info:
            if type == 'all':
                return info
            elif type == 'album':
                return info['album']
            elif type == 'mv':
                return info['mv']
            else:
                return info['song']

    async def song_detail(self, song):
        infos = await self.index_search_song(song, 'all')
        if infos:
            listitem = []
            detail = {}

            albums = infos['album']['itemlist']
            songs = infos['song']['itemlist']
            for song in songs:
                mid = song['mid']
                id = song['id']
                amid = ''
                for album in albums:
                    if song['singer'] == album['singer']:
                        amid = albums[0]['mid']
                    else:
                        amid = "003zV0ER0pAYTo"
                if not amid:
                    amid = "003zV0ER0pAYTo"
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
                                mid
                            ]
                        }
                    },
                    "req_2": {
                        "module": "music.musichallSong.PlayLyricInfo",
                        "method": "GetPlayLyricInfo",
                        "param": {
                            "songMID": mid,
                            "songID": int(id)
                        }
                    },
                    "req_3": {
                        "method": "GetCommentCount",
                        "module": "music.globalComment.GlobalCommentRead",
                        "param": {
                            "request_list": [
                                {
                                    "biz_type": 1,
                                    "biz_id": f"{id}",
                                    "biz_sub_type": 0
                                }
                            ]
                        }
                    },
                    "req_4": {
                        "module": "music.musichallAlbum.AlbumInfoServer",
                        "method": "GetAlbumDetail",
                        "param": {
                            "albumMid": amid
                        }
                    },
                    "req_5": {
                        "module": "vkey.GetVkeyServer",
                        "method": "CgiGetVkey",
                        "param": {
                            "guid": "7949132111",
                            "songmid": [
                                mid
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

                data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                params = {
                    "_": str(int(time.time() * 1000)),
                    "sign": await self.get_sign(data)
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                            data=data) as response:
                        if response.status == 200:
                            if response.headers.get('content-type') == 'application/json':
                                html = await response.json()
                            else:
                                html = await response.text()
                                html = eval(html.replace('null', '0').replace('\\/', '/'))

                            try:
                                song['lyric'] = html['req_2']['data']['lyric']
                            except:
                                song['lyric'] = ''

                            i = 1
                            for sip in html['req_5']['data']['sip']:
                                song[f'file_{i}'] = sip + html['req_5']['data']['midurlinfo'][0]['purl']
                                i += 1
                            if html['req_5']['data']['midurlinfo'][0]['purl']:
                                listitem.append(song)
            detail['total'] = len(listitem)
            detail['songs'] = listitem

            return detail

    async def song_comment(self, song, type='normal'):
        songs = []
        if type == 'normal':
            infos = await self.index_search_song(song)
            songs = infos['itemlist']
        elif type == 'lg':
            infos = await self.handle_login_search_info(song)
            songs = infos['song']['list']
        detail = {}
        comments = []
        if songs:
            for song in songs:
                mid = song['mid']
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
                                mid
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
                data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                params = {
                    "_": str(int(time.time() * 1000)),
                    "sign": await self.get_sign(data)
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                            data=data) as response:
                        if response.status == 200:
                            if response.headers.get('content-type') == 'application/json':
                                html = await response.json()
                            else:
                                html = await response.text()
                                html = eval(html.replace('null', '0').replace('\\/', '/'))

                            data = html['req_4']['data']
                            song['data'] = data
                            comments.append(song)
        detail['total'] = len(comments)
        detail['comments'] = comments
        return detail

    async def handle_singer_categpory(self, type='all', category='', page=1):
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
            "pgv_pvid": "7211015108",
            "fqm_pvqid": "783e298c-2893-4d0c-87a0-6681acd57109",
            "fqm_sessionid": "53e07048-c3bc-4944-b84b-f81874b3e090",
            "pgv_info": "ssid=s9571182682",
            "ts_uid": "6589886720",
            "_qpsvr_localtk": "0.9651124049304625",
            "music_ignore_pskey": "202306271436Hn@vBj",
            "ts_refer": "cn.bing.com/",
            "ts_last": "y.qq.com/n/ryqq/singer_list"
        }
        url = "https://u6.y.qq.com/cgi-bin/musics.fcg"
        if 0 <= page < 89:
            tags = {
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
            datas = []
            if type == 'all':
                datas = [{'area': -100, 'genre': -100, 'index': -100, 'sex': -100}]
            elif type == 'area':

                infos = tags['area']
                for info in infos[1:]:
                    data = {}
                    if category:
                        if info['name'] == category:
                            data['area'] = info['id']
                            data['genre'] = -100
                            data['index'] = -100
                            data['sex'] = -100
                            datas.append(data)
                            break
                    else:
                        data['area'] = info['id']
                        data['genre'] = -100
                        data['index'] = -100
                        data['sex'] = -100
                        datas.append(data)

            elif type == 'genre':
                datas.pop(0)
                infos = tags['genre']
                for info in infos[1:]:
                    data = {}
                    if category:
                        if info['name'] == category:
                            data['genre'] = info['id']
                            data['area'] = -100
                            data['index'] = -100
                            data['sex'] = -100
                            datas.append(data)
                            break
                    else:
                        data['genre'] = info['id']
                        data['area'] = -100
                        data['index'] = -100
                        data['sex'] = -100
                        datas.append(data)

            elif type == 'index':

                infos = tags['index']
                for info in infos[1:]:
                    data = {}
                    if category:
                        if info['name'] == category:
                            data['index'] = info['id']
                            data['area'] = -100
                            data['genre'] = -100
                            data['sex'] = -100
                            datas.append(data)
                            break
                    else:
                        data['index'] = info['id']
                        data['area'] = -100
                        data['genre'] = -100
                        data['sex'] = -100
                        datas.append(data)

            elif type == 'sex':

                infos = tags['sex']
                for info in infos[1:]:
                    data = {}
                    if category:
                        if info['name'] == category:
                            data['sex'] = info['id']
                            data['area'] = -100
                            data['genre'] = -100
                            data['index'] = -100
                            datas.append(data)
                            break
                    else:
                        data['sex'] = info['id']
                        data['area'] = -100
                        data['genre'] = -100
                        data['index'] = -100
                        datas.append(data)
            for data in datas:
                area = data['area']
                genre = data['genre']
                index = data['index']
                sex = data['sex']
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
                            "area": area,
                            "sex": sex,
                            "genre": genre,
                            "index": index,
                            "sin": page * 80,
                            "cur_page": page + 1
                        }
                    }
                }
                data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                params = {
                    "_": str(int(time.time() * 1000)),
                    "sign": await self.get_sign(data)
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                            data=data) as response:
                        if response.status == 200:
                            if response.headers.get('content-type') == 'application/json':
                                html = await response.json()
                            else:
                                html = await response.text()
                                html = eval(html.replace('null', '0').replace('\\/', '/'))
                            return html['req_1']['data']['singerlist']
                        else:
                            return "请求失败，请重试！"
        else:
            return '您输入的页数不正确！'

    async def handle_login_search_info(self, keyword):
        headers = {
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://y.qq.com",
            "Pragma": "no-cache",
            "Referer": "https://y.qq.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        cookies = {
            "eas_sid": "41n7I1F6t642h8o3C9a2m2v0g3",
            "pgv_pvid": "5788204336",
            "fqm_pvqid": "595f19aa-a599-4d7a-836c-8bb8d9ef63c9",
            "ts_uid": "5895747992",
            "fqm_sessionid": "4e3dfdcc-85c2-4e10-b9da-87ea5efae054",
            "pgv_info": "ssid=s2716925376",
            "_qpsvr_localtk": "0.682655934460251",
            "psrf_qqopenid": "",
            "wxopenid": "opCFJwyZFOVUmN-I3CXmTBjbBGC8",
            "wxuin": "1152921505285173556",
            "qm_keyst": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
            "psrf_qqaccess_token": "",
            "psrf_qqrefresh_token": "",
            "qqmusic_key": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
            "tmeLoginType": "1",
            "wxrefresh_token": "81_f_BCKpSA028OdvpmSjG5c2vlY-krhF9lp4ZmQcwUCNlbvKpqW7EMmcXjRp7YfwWVGOJUF5R_REqPLccJcCz8BAxxEOVMo3U6e8Zw5tOf28M",
            "psrf_qqunionid": "",
            "euin": "oK6kowEAoK4z7K-F7K6loi4k7c**",
            "wxunionid": "oqFLxsrrW6fR8NTx-YKijNxrhp6w",
            "login_type": "2",
            "ts_last": "y.qq.com/n/ryqq/search"
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
                "g_tk_new_20200303": 975243157,
                "g_tk": 975243157
            },
            "req_1": {
                "method": "DoSearchForQQMusicDesktop",
                "module": "music.search.SearchCgiService",
                "param": {
                    "remoteplace": "txt.yqq.top",
                    "searchid": "59937750457250010",
                    "search_type": 0,
                    "query": keyword,
                    "page_num": 1,
                    "num_per_page": 10
                }
            }
        }
        data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

        params = {
            "_": str(int(time.time() * 1000)),
            "sign": await self.get_sign(data)
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, cookies=cookies, params=params, data=data) as response:
                if response.status == 200:
                    if response.headers.get('content-type') == 'application/json':
                        html = await response.json()
                    else:
                        html = await response.text()
                        html = eval(html.replace('null', '0').replace('\\/', '/'))
                    song = html['req_1']['data']['body']['song']
                    zhida = html['req_1']['data']['body']['zhida']
                    return {'song': song, 'zhida': zhida}

    async def handle_login_song_detail(self, song):
        infos = await self.handle_login_search_info(song)
        infos = infos['song']['list']

        songs = []
        detail = {}

        for info in infos:
            song = {}
            amid = info['album']['mid']
            mid = info['mid']
            id = info['id']
            song['singer'] = info['singer']
            song['title'] = info['title']
            song['time_public'] = info['time_public']
            song['mv'] = 'https://y.qq.com/n/ryqq/mv/' + info['mv']['vid']
            headers = {
                "Accept": "application/json",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://y.qq.com",
                "Pragma": "no-cache",
                "Referer": "https://y.qq.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                "sec-ch-ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\""
            }
            cookies = {
                "eas_sid": "41n7I1F6t642h8o3C9a2m2v0g3",
                "pgv_pvid": "5788204336",
                "fqm_pvqid": "595f19aa-a599-4d7a-836c-8bb8d9ef63c9",
                "ts_uid": "5895747992",
                "fqm_sessionid": "4e3dfdcc-85c2-4e10-b9da-87ea5efae054",
                "pgv_info": "ssid=s2716925376",
                "_qpsvr_localtk": "0.682655934460251",
                "psrf_qqopenid": "",
                "wxopenid": "opCFJwyZFOVUmN-I3CXmTBjbBGC8",
                "wxuin": "1152921505285173556",
                "qm_keyst": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
                "psrf_qqaccess_token": "",
                "psrf_qqrefresh_token": "",
                "qqmusic_key": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
                "tmeLoginType": "1",
                "wxrefresh_token": "81_f_BCKpSA028OdvpmSjG5c2vlY-krhF9lp4ZmQcwUCNlbvKpqW7EMmcXjRp7YfwWVGOJUF5R_REqPLccJcCz8BAxxEOVMo3U6e8Zw5tOf28M",
                "psrf_qqunionid": "",
                "euin": "oK6kowEAoK4z7K-F7K6loi4k7c**",
                "wxunionid": "oqFLxsrrW6fR8NTx-YKijNxrhp6w",
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
                    "uin": "1152921505285173556",
                    "g_tk_new_20200303": 975243157,
                    "g_tk": 975243157
                },
                "req_1": {
                    "module": "userInfo.VipQueryServer",
                    "method": "SRFVipQuery_V2",
                    "param": {
                        "uin_list": [
                            "1152921505285173556"
                        ]
                    }
                },
                "req_2": {
                    "module": "userInfo.BaseUserInfoServer",
                    "method": "get_user_baseinfo_v2",
                    "param": {
                        "vec_uin": [
                            "1152921505285173556"
                        ]
                    }
                },
                "req_3": {
                    "module": "music.lvz.VipIconUiShowSvr",
                    "method": "GetVipIconUiV2",
                    "param": {
                        "PID": 3
                    }
                },
                "req_4": {
                    "module": "music.musicasset.SongFavRead",
                    "method": "IsSongFanByMid",
                    "param": {
                        "v_songMid": [
                            mid
                        ]
                    }
                },
                "req_5": {
                    "module": "music.musichallSong.PlayLyricInfo",
                    "method": "GetPlayLyricInfo",
                    "param": {
                        "songMID": mid,
                        "songID": int(id)
                    }
                },
                "req_6": {
                    "method": "GetCommentCount",
                    "module": "music.globalComment.GlobalCommentRead",
                    "param": {
                        "request_list": [
                            {
                                "biz_type": 1,
                                "biz_id": f"{id}",
                                "biz_sub_type": 0
                            }
                        ]
                    }
                },
                "req_7": {
                    "module": "music.musichallAlbum.AlbumInfoServer",
                    "method": "GetAlbumDetail",
                    "param": {
                        "albumMid": amid
                    }
                },
                "req_8": {
                    "module": "vkey.GetVkeyServer",
                    "method": "CgiGetVkey",
                    "param": {
                        "guid": "4874713108",
                        "songmid": [
                            mid
                        ],
                        "songtype": [
                            0
                        ],
                        "uin": "1152921505285173556",
                        "loginflag": 1,
                        "platform": "20"
                    }
                }
            }
            data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

            params = {
                "_": str(int(time.time() * 1000)),
                "sign": await self.get_sign(data)
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                        data=data) as response:
                    if response.status == 200:
                        if response.headers.get('content-type') == 'application/json':
                            html = await response.json()
                        else:
                            html = await response.text()
                            html = eval(
                                html.replace('null', '0').replace('False', '0').replace('false', '0').replace('True',
                                                                                                              '0').replace(
                                    'true', '0').replace('\\/', '/'))

                        try:
                            song['lyric'] = html['req_5']['data']['lyric']
                        except:
                            song['lyric'] = ''

                        i = 1
                        for sip in html['req_8']['data']['sip']:
                            song[f'file_{i}'] = sip + html['req_8']['data']['midurlinfo'][0]['purl']
                            print(f'file:{song[f'file_{i}']}')
                            i += 1
                        if html['req_8']['data']['midurlinfo'][0]['purl']:
                            songs.append(song)
        detail['total'] = len(songs)
        detail['song'] = songs
        return detail

    async def handle_login_search_mv(self, song):
        """
        获取搜索MV详细信息
        """
        infos = await self.handle_login_search_info(song)
        infos = infos['song']['list']
        songs = []
        detail = {}
        for info in infos:
            song = {}
            mv = info['mv']['vid']
            song['singer'] = info['singer']

            song['title'] = info['title']
            song['time_public'] = info['time_public']
            if mv:
                headers = {
                    "Accept": "*/*",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-type": "application/x-www-form-urlencoded",
                    "Origin": "https://y.qq.com",
                    "Pragma": "no-cache",
                    "Referer": "https://y.qq.com/",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
                }
                cookies = {
                    "eas_sid": "41n7I1F6t642h8o3C9a2m2v0g3",
                    "pgv_pvid": "5788204336",
                    "fqm_pvqid": "595f19aa-a599-4d7a-836c-8bb8d9ef63c9",
                    "ts_uid": "5895747992",
                    "fqm_sessionid": "4e3dfdcc-85c2-4e10-b9da-87ea5efae054",
                    "pgv_info": "ssid=s2716925376",
                    "_qpsvr_localtk": "0.682655934460251",
                    "psrf_qqopenid": "",
                    "wxopenid": "opCFJwyZFOVUmN-I3CXmTBjbBGC8",
                    "wxuin": "1152921505285173556",
                    "qm_keyst": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
                    "psrf_qqaccess_token": "",
                    "psrf_qqrefresh_token": "",
                    "qqmusic_key": "W_X_63B0aQaLTVfipA2EU4zu-oL7v7yrWDaGPKbKDUtX7qHwopEnwRuVpe7oawKNm4iak9uGl47Tt2uwWiOY",
                    "tmeLoginType": "1",
                    "wxrefresh_token": "81_f_BCKpSA028OdvpmSjG5c2vlY-krhF9lp4ZmQcwUCNlbvKpqW7EMmcXjRp7YfwWVGOJUF5R_REqPLccJcCz8BAxxEOVMo3U6e8Zw5tOf28M",
                    "psrf_qqunionid": "",
                    "euin": "oK6kowEAoK4z7K-F7K6loi4k7c**",
                    "wxunionid": "oqFLxsrrW6fR8NTx-YKijNxrhp6w",
                    "login_type": "2",
                    "ts_last": "y.qq.com/n/ryqq/mv/004EKSyH0r5kJG"
                }
                url = "https://u.y.qq.com/cgi-bin/musicu.fcg"
                data = {
                    "comm": {
                        "ct": 6,
                        "cv": 0,
                        "g_tk": 975243157,
                        "uin": 1152921505285173500,
                        "format": "json",
                        "platform": "yqq"
                    },
                    "mvInfo": {
                        "module": "music.video.VideoData",
                        "method": "get_video_info_batch",
                        "param": {
                            "vidlist": [
                                mv
                            ],
                            "required": [
                                "vid",
                                "type",
                                "sid",
                                "cover_pic",
                                "duration",
                                "singers",
                                "new_switch_str",
                                "video_pay",
                                "hint",
                                "code",
                                "msg",
                                "name",
                                "desc",
                                "playcnt",
                                "pubdate",
                                "isfav",
                                "fileid",
                                "filesize_v2",
                                "switch_pay_type",
                                "pay",
                                "pay_info",
                                "uploader_headurl",
                                "uploader_nick",
                                "uploader_uin",
                                "uploader_encuin",
                                "play_forbid_reason"
                            ]
                        }
                    },
                    "mvUrl": {
                        "module": "music.stream.MvUrlProxy",
                        "method": "GetMvUrls",
                        "param": {
                            "vids": [
                                mv
                            ],
                            "request_type": 10003,
                            "addrtype": 3,
                            "format": 264,
                            "maxFiletype": 60
                        }
                    }
                }
                data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

                async with aiohttp.ClientSession() as session:
                    async with session.post(url=url, headers=headers, cookies=cookies, data=data) as response:
                        if response.status == 200:
                            if response.headers.get('content-type') == 'application/json':
                                html = await response.json()
                            else:
                                html = await response.text()
                                html = eval(
                                    html.replace('null', '0').replace('False', '0').replace('false', '0').replace(
                                        'True',
                                        '0').replace(
                                        'true', '0').replace('\\/', '/'))

                            url = html['mvUrl']['data'][mv]['mp4']
                            song['url'] = url[1:4]
                            songs.append(song)
        detail['total'] = len(songs)
        detail['mv'] = songs
        return detail

    async def handle_ranks(self, keyword):
        rank = {3: '欧美榜', 4: '流行指数榜', 5: '内地榜', 6: '港台榜', 16: '韩国榜', 17: '日本榜',
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
        topid = [idex for idex, value in rank.items() if value == keyword][0]
        if topid:
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
                "pgv_pvid": "1937823549",
                "fqm_pvqid": "9e9c84f4-7e0a-4fae-95ee-49dd0d0183a8",
                "ts_uid": "6834418836",
                "fqm_sessionid": "82c6e2c3-447e-4add-89a8-b8e112ebf0ba",
                "pgv_info": "ssid=s1914219376",
                "ts_refer": "cn.bing.com/",
                "ts_last": "y.qq.com/n/ryqq/toplist/4"
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
                    "module": "musicToplist.ToplistInfoServer",
                    "method": "GetDetail",
                    "param": {
                        "topid": topid,
                        "offset": 0,
                        "num": 20,
                        "period": "2024-06-10"
                    }
                }
            }
            data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

            params = {
                "_": str(int(time.time() * 1000)),
                "sign": await self.get_sign(data)
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                        data=data) as response:
                    if response.status == 200:
                        if response.headers.get('content-type') == 'application/json':
                            html = await response.json()
                        else:
                            html = await response.text()
                            html = eval(
                                html.replace('null', '0').replace('False', '0').replace('false', '0').replace('True',
                                                                                                              '0').replace(
                                    'true', '0').replace('\\/', '/'))
                        return html['req_1']['data']

    async def handle_song(self, keyword):
        data = {'官方歌单': 3317, '音乐人在听': 1069, '达人心选': 3900, '': 199, '国语': 1, '粤语': 146, '英语': 3,
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
        id = data[keyword]
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
                    "category_id": id,
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
                    "category_id": id
                }
            }
        }
        data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

        params = {
            "_": str(int(time.time() * 1000)),
            "sign": await self.get_sign(data)
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, cookies=cookies, params=params,
                                    data=data) as response:
                if response.status == 200:
                    if response.headers.get('content-type') == 'application/json':
                        html = await response.json()
                    else:
                        html = await response.text()
                        html = eval(
                            html.replace('null', '0').replace('False', '0').replace('false', '0').replace('True',
                                                                                                          '0').replace(
                                'true', '0').replace('\\/', '/'))
                    return html


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    music = QQMusic()
    results = loop.run_until_complete(music.handle_song('音乐人在听'))
    print(results)
