import config
from logger import Logger
from push import Push
from spider import Spider
from spiderMirror import SpiderMirror
import time
from state import State
import traceback
import sys

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)


def isCityInTitle(cityFilter, title):
    cities = cityFilter.split(" ")
    for city in cities:
        if city in title:
            return True
    return False


def run():
    try:
        msgs = spider.getPosts()
        log.info("get %d posts", len(msgs))
        i = 0
        if len(msgs) > 0:
            for id, tag, city, title, text, url in msgs:
                i += 1
                if useMirror:
                    pushTitle = title
                    pushText = text
                else:
                    pushTitle = ""
                    if tag:
                        pushTitle = "#" + tag + "#"
                    if city:
                        pushTitle += "#" + city + "#"
                    pushTitle += "【" + title + "】"
                    pushText = "#疫情聚合#" + pushTitle + "\r\n" + text + " 【转自：" + url + ' 】'
                    pushText = pushText.replace('【】', '')
                    if "pinned" in pushText:
                        continue
                if cityFilter and not isCityInTitle(cityFilter, pushTitle):
                    continue
                log.info("send msg")
                push.sendMsg(pushTitle, pushText)
                if usrAction:
                    state.setPostId(spider.postId)
                if len(msgs) != i:
                    log.info("sleep 20s")
                    time.sleep(20)
    except Exception as e:
        log.error("error: %s", traceback.format_exc())


if __name__ == '__main__':
    # use github action to run?
    if len(sys.argv) > 1:
        usrAction = True
        log.info("use github action")
    else:
        usrAction = False

    push = Push(token=config.PushToken, keyWord=config.PushKeyWord, weiboSCF=config.WeiboSCFUrl,
                weiboRef=config.WeiboRef, weiboCookie=config.WeiboCookie, weixinToken=config.WeixinToken)

    useMirror = False if config.TelegramMirror is None else True

    if not useMirror:
        spider = Spider()
    else:
        spider = SpiderMirror(config.TelegramMirror)

    cityFilter = config.City

    if usrAction:
        state = State(config.Redis)
        spider.postId = state.getPostId()
    else:
        spider.postId = 741

    while True:
        run()
        if usrAction:
            break
        else:
            log.info("sleep 60s")
            time.sleep(60)
