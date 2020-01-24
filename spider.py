import requests
from bs4 import BeautifulSoup


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
            content = i.select(".tgme_widget_message_text")[0]
            c1 = content.a.get_text()
            c2 = content.b.get_text()
            title = c1 + " " + c2
            content = content.get_text()
            self.postId = id
            res.append((id, title, content))
        return res


if __name__ == '__main__':
    s = Spider()
    res = s.getPosts()
    print(res)
    res = s.getPosts()
    print(res)
