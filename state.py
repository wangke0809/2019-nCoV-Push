import redis

class State(object):

    def __init__(self, url):
        self.rds = redis.Redis.from_url(url)
        self.key = 'NCOVPOSTID'

    def setPostId(self, id):
        self.rds.set(self.key, id)

    def getPostId(self):
        id = self.rds.get(self.key)
        return int(id)

if __name__ == '__main__':
    import config
    state = State(config.Redis)
    state.setPostId(123)
    print(state.getPostId())