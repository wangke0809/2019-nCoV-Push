import config
from logger import Logger
from push import Push
from spider import Spider
import time
import traceback

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)

if __name__ == '__main__':
    push = Push(config.PushToken, config.PushKeyWord, config.WeiboRef, config.WeiboCookie, config.WeiboSCFUrl)
    spider = Spider()
    spider.postId = 700
    while True:
        try:
            msgs = spider.getPosts()
            log.info("get %d posts", len(msgs))
            if len(msgs) > 0:
                for id, tag, city, title, text, url in msgs:
                    pushTitle = ""
                    if tag:
                        pushTitle = "#" + tag + "#"
                    if city:
                        pushTitle += "#" + city + "#"
                    pushTitle += "【" + title + "】"
                    pushText = "#疫情聚合#" + pushTitle + "\r\n" + text + " 【转自：" + url + ' 】'
                    push.sendMsg(pushTitle, pushText)
                    time.sleep(60)
        except Exception as e:
            log.error("error: %s", traceback.format_exc())
        time.sleep(60)
