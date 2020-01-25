import requests
import json
import time
import urllib


class Weibo(object):

    def __init__(self, ref, cookie):
        self.hdrs = {
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://weibo.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Referer": ref,
            "Accept-Language": "zh-CN",
            "Cookie": cookie,
        }

    def send(self, text):
        ts = int(time.time() * 1000)
        post_str = f'location=page_100505_manage&text={urllib.parse.quote(text)}&style_type=1&pdetail=1005052216356441&isReEdit=false&rank=0&pub_type=dialog&_t=0'
        url = f'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd={ts}'
        res = requests.post(url, data=post_str, headers=self.hdrs).content.decode('gbk')
        print(res)
        j = json.loads(res)
        if j['code'] == '100000':
            return True
        else:
            return False


if __name__ == '__main__':
    import config
    weibo = Weibo(config.WeiboRef, config.WeiboCookie)
    weibo.send("武汉加油！")
