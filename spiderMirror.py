import requests
import re


class SpiderMirror(object):

    def __init__(self, url):
        self.url = url
        self.postId = 0

    def getPosts(self):
        res = requests.get(self.url)
        data = res.json()
        print(data)
        res = []
        newId = self.postId
        for item in data['items']:
            link = item['link']
            id = int(link.split('/')[-1])
            if id <= self.postId:
                continue
            if newId == self.postId:
                newId = id
            title = item['title']
            content = item['contentSnippet']
            url = re.findall('（<a href="(.*?)" target="_blank" rel="noopener" onclick="return confirm', item['content'],
                             re.S)
            if url:
                url = url[0]
            else:
                url = ''
            # id, tag, city, title, text, url
            res.append((id, "", "", title, content, url))
        self.postId = newId
        return res


if __name__ == '__main__':
    import config

    s = SpiderMirror(config.TelegramMirror)
    for n in s.getPosts():
        print(n[0])
    print(s.getPosts())
