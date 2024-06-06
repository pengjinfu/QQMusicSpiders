import execjs


def sign(data):
    with open('./qq_music.js', 'r', encoding='utf-8') as file:
        js_code = file.read()
    if not data:
        print(f'参数不能为空，现在使用测试data')
        data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"28644833441163176","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_2":{"module":"music.paycenterapi.LoginStateVerificationApi","method":"GetChargeAccount","param":{"appid":"mlive"}}}'
    ctx = execjs.compile(js_code).call('getSign', data)

    return ctx


if __name__ == '__main__':
    print(sign(''))
