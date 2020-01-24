import config
from logger import Logger
from push import Push
from spider import Spider
import time

log = Logger.getLogger("nCoV", config.LoggerJsonConfig)

if __name__ == '__main__':
    push = Push(config.PushToken, config.PushKeyWord)
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
                for m in msgs:
                    push.sendMsg(m[1], m[2])
        except Exception as e:
            log.error("error: %s", e)
        time.sleep(60)
