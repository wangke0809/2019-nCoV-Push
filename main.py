import config
from logger import Logger
from push import Push
from spider import Spider
import time
from state import State
import traceback
import argparse

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True, help="DingTalk Token")
    parser.add_argument("--keyword", required=True, help="DingTalk keyword")
    parser.add_argument("--weibo", required=True, help="Weibo scf url")
    parser.add_argument("--redis", required=True, help="redis url")
    args = parser.parse_args()
    token = parser.token
    keyword = parser.keyword
    weiboScf = parser.weibo
    redisUrl = parser.redis
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
