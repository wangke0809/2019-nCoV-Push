import config
from logger import Logger
from push import Push
from spider import Spider
import time

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)

if __name__ == '__main__':
    push = Push(config.PushToken, config.PushKeyWord, config.WeiboRef, config.WeiboCookie, config.WeiboSCFUrl)
    spider = Spider()
    setup = True
    while True:
        try:
            msgs = spider.getPosts()
            log.info("get %d posts", len(msgs))
            if len(msgs) > 0:
                if setup:
                    setup = False
                    continue
                for id, tag, city, title, text, url in msgs:
                    if tag:
                        pushTitle = "#" + tag + "#"
                    if city:
                        pushTitle += "#" + city + "#"
                    pushTitle += "【" + title + "】"
                    pushText = pushTitle + "\r\n" + text + " 【转自：" + url + ' 】'
                    push.sendMsg(pushTitle, pushText)
        except Exception as e:
            log.error("error: %s", e)
        time.sleep(60)
