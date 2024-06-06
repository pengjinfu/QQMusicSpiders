# pip install requests
# 导入第三方爬虫库：requests
import time, os

import requests
import json
from lxml import etree
import re, uuid, base64


class IndexInfo(object):
    def __init__(self):
        # 目标网址
        self.index_url = "https://y.qq.com"
        self.infos = {}

    def decode_image(self, src):
        """
        解码图片
        :param src: 图片编码
            eg:
                src="data:image/gif;base64,R0lGODlhMwAxAIAAAAAAAP///
                    yH5BAAAAAAALAAAAAAzADEAAAK8jI+pBr0PowytzotTtbm/DTqQ6C3hGX
                    ElcraA9jIr66ozVpM3nseUvYP1UEHF0FUUHkNJxhLZfEJNvol06tzwrgd
                    LbXsFZYmSMPnHLB+zNJFbq15+SOf50+6rG7lKOjwV1ibGdhHYRVYVJ9Wn
                    k2HWtLdIWMSH9lfyODZoZTb4xdnpxQSEF9oyOWIqp6gaI9pI1Qo7BijbF
                    ZkoaAtEeiiLeKn72xM7vMZofJy8zJys2UxsCT3kO229LH1tXAAAOw=="

        :return: str 保存到本地的文件名
        """
        # 1、信息提取
        result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
        if result:
            ext = result.groupdict().get("ext")
            data = result.groupdict().get("data")

        else:
            raise Exception("Do not parse!")

        # 2、base64解码
        img = base64.urlsafe_b64decode(data)
        print(img)

        # 3、二进制文件保存
        filename = "{}.{}".format(uuid.uuid4(), ext)
        with open(filename, "wb") as f:
            f.write(img)

        return filename

    def index(self, day):
        # 请求头：-模拟浏览器环境，使爬虫更加像人为访问
        headers = {
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
        }
        # 请求Cookie：模拟浏览器环境，使爬虫更加像人为访问
        cookies = {
            "pgv_pvid": "7211015108",
            "fqm_pvqid": "783e298c-2893-4d0c-87a0-6681acd57109",
            "fqm_sessionid": "53e07048-c3bc-4944-b84b-f81874b3e090",
            "pgv_info": "ssid=s9571182682",
            "ts_last": "y.qq.com/",
            "ts_refer": "cn.bing.com/",
            "ts_uid": "6589886720"
        }

        # GET请求：请求方式查看分析文档中的，标头显示了请求方式，模拟浏览器请求
        response = requests.get(self.index_url, headers=headers, cookies=cookies)

        # 获取请求数据：数据格式为文档，如果是XHR则是JSON格式，如果是图片和视频则是二进制格式
        html = response.text

        # 保存数据：保存为HTML格式，方便查看，如果index.html文件不存在则创建，w写数据，encoding编码格式为utf-8是数据格式
        with open(f'index_{day}.html', 'w', encoding='utf-8') as file:
            file.write(html)

    def handle_index(self, day):
        with open(f'index_{day}.html', 'r', encoding='utf-8') as file:
            html = file.read()
            html = etree.HTML(html)
            self.index_links(html)
            self.index_hot(html)
            self.index_news(html)

    def index_links(self, html):
        """
        首页链接
        :param html: 解析后的HTML
        :return: None
        """
        # 首页链接
        links = {}
        navs = html.xpath(
            '//a[@class="top_nav__link top_nav__link--current" or @class="top_nav__link" or @class="top_subnav__link" or @class="js_other_link"]')
        for nav in navs:
            title = nav.text
            link = self.index_url + nav.attrib['href']
            links[title] = link

        self.infos["links"] = links

    def index_hot(self, html):
        """
        歌单推荐
        :param html:解析后的HTML
        :return:None
        """
        hots = {}
        infos = html.xpath('//img[@class="playlist__pic"]')
        bfs = html.xpath('//div[@class="playlist__other"]')
        links = html.xpath('//span[@class="playlist__title_txt"]/a/@href')
        i = 1
        for info, bf, link in zip(infos, bfs, links):
            hots[i] = {'image': info.xpath('./@src')[0], 'title': info.xpath('./@alt')[0],
                       'bfl': bf.xpath('./text()')[0], 'link': self.index_url + link}
            i += 1
        self.infos["hots"] = hots

    def index_news(self, html):
        """
        新歌首发
        :param html:解析后的HTML
        :return:None
        """
        news = {}
        infos = html.xpath('//img[@class="debutlist__pic"]')
        times = html.xpath('//div[@class="debutlist__time c_tx_thin"]')
        links = html.xpath('//p[@class="debutlist__author"]/a/@href')
        signers = html.xpath('//p[@class="debutlist__author"]/a/text()')
        i = 1
        for info, time, link, singer in zip(infos, times, links, signers):
            news[i] = {'image': info.xpath('./@src')[0], 'title': info.xpath('./@alt')[0],
                       'time': time.xpath('./text()')[0], 'link': self.index_url + link, 'signer': singer}
            i += 1
        self.infos["news"] = news

    def index_other(self, day):
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
            "ts_last": "y.qq.com/",
            "ts_refer": "cn.bing.com/",
            "ts_uid": "6589886720"
        }
        url = "https://u6.y.qq.com/cgi-bin/musics.fcg"
        params = {
            "_": "1717551963372",
            "sign": "zzb04ba41b5glwdydj4tajvle4g8eqyww4b17e42d"
        }
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
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

        html = response.json()
        with open(f'index_{day}.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(html))

    def hanlde_index_other(self, day):
        with open(f'index_{day}.json', 'r', encoding='utf-8') as file:
            html = file.read()
            html = json.loads(html)
        # 搜索排行
        search = html['req_1']['data']['vec_hotkey']
        # 精彩推荐
        wonder = html['req_2']['data']['shelf']['v_niche']
        # 新碟首发
        albums = html['req_4']['data']['albums']
        # 排行榜
        rank = html['req_5']['data']['group']
        # mv
        mv = html['req_6']['data']

        self.infos["search"] = search
        self.infos["wonder"] = wonder
        self.infos["albums"] = albums
        self.infos["rank"] = rank
        self.infos["mv"] = mv

    def main(self):
        today = time.localtime()
        day = str(today.tm_year) + str(today.tm_mon) + str(today.tm_mday)
        yestoday = str(today.tm_year) + str(today.tm_mon) + str(today.tm_mday - 1)
        if os.path.exists(f'index_{yestoday}.html'):
            os.remove(f'index_{yestoday}.html')
        if os.path.exists(f'index_{yestoday}.json'):
            os.remove(f'index_{yestoday}.json')
        if os.path.exists(f'index_{day}.html'):
            pass
        else:
            self.index(day)
        if os.path.exists(f'index_{day}.json'):
            pass
        else:
            self.index_other(day)

        self.handle_index(day)
        self.hanlde_index_other(day)


if __name__ == '__main__':
    index = IndexInfo()
    index.main()




