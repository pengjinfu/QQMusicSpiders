// 补window环境
window = global;

document = {};
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    product: "Gecko",
    productSub: "20030107",
}
location = {
    "ancestorOrigins": {},
    "href": "https://y.qq.com/n/ryqq/singer_list",
    "origin": "https://y.qq.com",
    "protocol": "https:",
    "host": "y.qq.com",
    "hostname": "y.qq.com",
    "port": "",
    "pathname": "/n/ryqq/singer_list",
    "search": "",
    "hash": ""
}
// 定义全局加载器接收变量
var qq;

// 导入模块
require('D:/QQMusicSpiders/v1/src/js/webpack.js')
!function (e) {
    function t(t) {
        for (var a, n, d = t[0], c = t[1], i = t[2], l = 0, u = []; l < d.length; l++) n = d[l], Object.prototype.hasOwnProperty.call(o, n) && o[n] && u.push(o[n][0]), o[n] = 0;
        for (a in c) Object.prototype.hasOwnProperty.call(c, a) && (e[a] = c[a]);
        for (b && b(t); u.length;) u.shift()();
        return f.push.apply(f, i || []), r()
    }

    function r() {
        for (var e, t = 0; t < f.length; t++) {
            for (var r = f[t], a = !0, n = 1; n < r.length; n++) {
                var c = r[n];
                0 !== o[c] && (a = !1)
            }
            a && (f.splice(t--, 1), e = d(d.s = r[0]))
        }
        return e
    }

    var a = {}, n = {
        21: 0
    }, o = {
        21: 0
    }, f = [];

    function d(t) {
        if (a[t]) return a[t].exports;
        var r = a[t] = {
            i: t, l: !1, exports: {}
        };
        return e[t].call(r.exports, r, r.exports, d), r.l = !0, r.exports
    }

    d.e = function (e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            20: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1,
            26: 1
        }[e] && t.push(n[e] = new Promise((function (t, r) {
            for (var a = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "download_detail",
                9: "index",
                10: "msg_center",
                11: "mv",
                12: "mvList",
                13: "mv_toplist",
                14: "notfound",
                15: "player",
                16: "player_radio",
                17: "playlist",
                18: "playlist_edit",
                19: "profile",
                20: "radio",
                22: "search",
                23: "singer",
                24: "singer_list",
                25: "songDetail",
                26: "toplist"
            }[e] || e) + "." + {
                1: "2e3d715e72682303d35b",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "e3bedf2b5810f8db0684",
                9: "ea0adb959fef9011fc25",
                10: "020422608fe8bfb1719a",
                11: "8bdb1df6c5436b790baa",
                12: "47ce9300786df1b70584",
                13: "4aee33230ba2d6b81dce",
                14: "e6f63b0cf57dd029fbd6",
                15: "1d2dbefbea113438324a",
                16: "d893492de07ce97d8048",
                17: "9484fde660fe93d9f9f0",
                18: "67fb85e7f96455763c83",
                19: "5e8c651e74b13244f7cf",
                20: "3befd83c10b19893ec66",
                22: "b2d11f89ea6a512a2302",
                23: "c7a38353c5f4ebb47491",
                24: "df0961952a2d3f022894",
                25: "4c080567e394fd45608b",
                26: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = d.p + a, f = document.getElementsByTagName("link"), c = 0; c < f.length; c++) {
                var i = (b = f[c]).getAttribute("data-href") || b.getAttribute("href");
                if ("stylesheet" === b.rel && (i === a || i === o)) return t()
            }
            var l = document.getElementsByTagName("style");
            for (c = 0; c < l.length; c++) {
                var b;
                if ((i = (b = l[c]).getAttribute("data-href")) === a || i === o) return t()
            }
            var u = document.createElement("link");
            u.rel = "stylesheet", u.type = "text/css", u.onload = t, u.onerror = function (t) {
                var a = t && t.target && t.target.src || o,
                    f = new Error("Loading CSS chunk " + e + " failed.\n(" + a + ")");
                f.code = "CSS_CHUNK_LOAD_FAILED", f.request = a, delete n[e], u.parentNode.removeChild(u), r(f)
            }
                , u.href = o, 0 !== u.href.indexOf(window.location.origin + "/") && (u.crossOrigin = "anonymous"), document.getElementsByTagName("head")[0].appendChild(u)
        })).then((function () {
            n[e] = 0
        })));
        var r = o[e];
        if (0 !== r) if (r) t.push(r[2]); else {
            var a = new Promise((function (t, a) {
                r = o[e] = [t, a]
            }));
            t.push(r[2] = a);
            var f, c = document.createElement("script");
            c.charset = "utf-8", c.timeout = 120, d.nc && c.setAttribute("nonce", d.nc), c.src = function (e) {
                return d.p + "js/" + ({
                    1: "common",
                    3: "album",
                    4: "albumDetail",
                    5: "album_mall",
                    6: "category",
                    7: "cmtpage",
                    8: "download_detail",
                    9: "index",
                    10: "msg_center",
                    11: "mv",
                    12: "mvList",
                    13: "mv_toplist",
                    14: "notfound",
                    15: "player",
                    16: "player_radio",
                    17: "playlist",
                    18: "playlist_edit",
                    19: "profile",
                    20: "radio",
                    22: "search",
                    23: "singer",
                    24: "singer_list",
                    25: "songDetail",
                    26: "toplist"
                }[e] || e) + ".chunk." + {
                    1: "5e1cf4fe669e008d3018",
                    3: "60c3e6466bf86237e3c3",
                    4: "805f72801c9039bdba42",
                    5: "e7991b6193953db62b75",
                    6: "63d12c68f904e8bd4d62",
                    7: "3d6ef0cefab73ee07acb",
                    8: "400de3c452106624cb2f",
                    9: "f35380810bd59ed43e01",
                    10: "66c75aabeb4ef645fa45",
                    11: "55abde3b3e60e5d208da",
                    12: "b381c0102fa5c4afde60",
                    13: "9ea1628ad380b2d9b674",
                    14: "5ea243997c9b940a0048",
                    15: "338035f09211f838463d",
                    16: "5a9fe70b49e8cd1e9a8c",
                    17: "9eadbe22abeff411fa84",
                    18: "6ef03976f240a0d38967",
                    19: "280cd4639fdbebe5f12f",
                    20: "21252db45de3ea95a092",
                    22: "3ab3f879eb1b53f4e1b9",
                    23: "d4001fe29c8bc7a90f63",
                    24: "06f5c944e03952dce97a",
                    25: "f3e1e2a50b799fafc8de",
                    26: "38da0668d79ba663e75e"
                }[e] + ".js?max_age=2592000"
            }(e), 0 !== c.src.indexOf(window.location.origin + "/") && (c.crossOrigin = "anonymous");
            var i = new Error;
            f = function (t) {
                c.onerror = c.onload = null, clearTimeout(l);
                var r = o[e];
                if (0 !== r) {
                    if (r) {
                        var a = t && ("load" === t.type ? "missing" : t.type), n = t && t.target && t.target.src;
                        i.message = "Loading chunk " + e + " failed.\n(" + a + ": " + n + ")", i.name = "ChunkLoadError", i.type = a, i.request = n, r[1](i)
                    }
                    o[e] = void 0
                }
            };
            var l = setTimeout((function () {
                f({
                    type: "timeout", target: c
                })
            }), 12e4);
            c.onerror = c.onload = f, document.head.appendChild(c)
        }
        return Promise.all(t)
    }
        , d.m = e, d.c = a, d.d = function (e, t, r) {
        d.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0, get: r
        })
    }
        , d.r = function (e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
        , d.t = function (e, t) {
        if (1 & t && (e = d(e)), 8 & t) return e;
        if (4 & t && "object" === typeof e && e && e.__esModule) return e;
        var r = Object.create(null);
        if (d.r(r), Object.defineProperty(r, "default", {
            enumerable: !0, value: e
        }), 2 & t && "string" != typeof e) for (var a in e) d.d(r, a, function (t) {
            return e[t]
        }
            .bind(null, a));
        return r
    }
        , d.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e.default
        } : function () {
            return e
        };
        return d.d(t, "a", t), t
    }
        , d.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
        , d.p = "/ryqq/", d.oe = function (e) {
        throw e
    };
    var c = window.webpackJsonp = window.webpackJsonp || [], i = c.push.bind(c);
    c.push = t, c = c.slice();
    for (var l = 0; l < c.length; l++) t(c[l]);
    var b = i;
    r()
    // 可以看到整个webpack都是d在操作，所以d就是加载器
    qq = d
}([]);

function getSign(data) {
    o = qq(147).default
    return o(data)
}

data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505285173556","g_tk_new_20200303":975243157,"g_tk":975243157},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"59937750457250010","search_type":0,"query":"我会好好的","page_num":1,"num_per_page":10}}}'

console.log(
    getSign(data)
)

