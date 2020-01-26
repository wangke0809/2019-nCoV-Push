import config
from logger import Logger
from push import Push
from spider import Spider
import time
from state import State
import traceback
import sys

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)


def run():
    try:
        msgs = spider.getPosts()
        log.info("get %d posts", len(msgs))
        i = 0
        if len(msgs) > 0:
            for id, tag, city, title, text, url in msgs:
                i += 1
                pushTitle = ""
                if tag:
                    pushTitle = "#" + tag + "#"
                if city:
                    pushTitle += "#" + city + "#"
                pushTitle += "【" + title + "】"
                pushText = "#疫情聚合#" + pushTitle + "\r\n" + text + " 【转自：" + url + ' 】'
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
    spider = Spider()

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
