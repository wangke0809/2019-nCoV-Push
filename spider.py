import requests
from bs4 import BeautifulSoup
import re


class Spider(object):

    def __init__(self):
        self.postId = 0

    def getPosts(self):
        html = requests.get('https://t.me/s/nCoV2019')
        html.raise_for_status()
        soup = BeautifulSoup(html.text, 'html5lib')
        msg = soup.select(".tgme_widget_message_wrap")
        res = []
        for i in msg:
            idStr = i.select(".tgme_widget_message")[0].get("data-post")
            id = int(idStr.split("/")[1])
            if id <= self.postId:
                continue

            content = i.select(".tgme_widget_message_text")
            if len(content) > 0:
                content = content[0]
            else:
                continue

            aTags = content.find_all('a')
            c1 = ''
            c2 = ''
            city = ""
            ref = None
            if aTags and aTags[-1].get("onclick"):
                ref = None if 'return confirm' not in aTags[-1].get("onclick") else (
                    aTags[-1], aTags[-1].get_text(), aTags[-1].get("href"))
            if content.a:
                c1 = content.a.get_text()
                c1 = c1.replace("#", "")
            title = re.findall(r'【(.*?)】', content.get_text(), re.S)
            if len(title) > 0:
                c2 = title[0]
                citys = c2.split(" ")
                for c in citys:
                    if '#' in c:
                        c2 = c2.replace(c, c + "#")
                        city = c.replace("#", "").replace("【", "").strip()
                        break
            tag = c1.strip()
            if city != "":
                title = c2.replace("#", "").replace("【", "").strip().replace("】", "").strip()
            else:
                title = c2.replace("【", "").strip().replace("】", "").strip()
            title = title.replace(" ", "")
            text = content.get_text()
            ret = re.findall(r'】(.*?)$', text, re.S)
            if len(ret) > 0:
                text = ret[0]
                text = text.strip()
            self.postId = id
            res.append((id, tag, city, title, text, ref[2] if ref is not None else ""))
        return res


if __name__ == '__main__':
    s = Spider()
    s.postId = 717
    res = s.getPosts()
    print(res)
    res = s.getPosts()
    print(res)
