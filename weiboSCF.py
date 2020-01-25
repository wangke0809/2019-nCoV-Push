# -*- coding: utf8 -*-
from weibo import Weibo
import sys, logging

WeiboRef = 'https://weibo.com/u/7378955365/home?wvr=5&uut=fin&from=reg'
WeiboCookie = '''cookie'''

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def main_handler(event, context):
    logger.info("start main handler")
    if "requestContext" not in event.keys():
        return {"code": 410, "errorMsg": "event is not come from api gateway"}
    weibo = Weibo(WeiboRef, WeiboCookie)
    weibo.send(event['body'])
    return ("o")
