import config
from logger import Logger
from push import Push
from spider import Spider
import time
from state import State
import traceback

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)

if __name__ == '__main__':
    token = config.PushToken
    keyword = config.PushKeyWord
    weiboScf = config.WeiboSCFUrl
    redisUrl = config.Redis
    push = Push(token=token, keyWord=keyword, weiboSCF=weiboScf)
    spider = Spider()
    state = State(redisUrl)
    spider.postId = state.getPostId()
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
                state.setPostId(spider.postId)
                time.sleep(60)
    except Exception as e:
        log.error("error: %s", traceback.format_exc())
