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
require('./webpack')

// 加载器

function getSign(data) {
    o = qq(147).default
    return o(data)
}

