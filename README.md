# 2019-nCoV-Push

武汉新冠状病毒肺炎疫情信息推送：抓取 Telegram 频道 @nCoV2019 进行通知。

现在已经支持转发频道内容到微信，钉钉群和微博 [@聚合提醒](https://www.weibo.com/u/7378955365)。

频道地址：https://t.me/s/nCoV2019

发送微博：[WeiboSender](https://github.com/wangke0809/WeiboSender)

为什么不使用频道提供的 RSS ？因为 RSS 内容不实时。

为什么不抓取丁香园？因为丁香园聚合信息不够全。

爬虫 `spider.py` 可单独使用，已经解析出`id, tag, city, title, text, refUrl`

# 使用说明

## 依赖

- Python3 +

在 Python3.5, Python3.6, Python3.7 下经过测试。

## 安装

```bash
git clone https://github.com/wangke0809/2019-nCoV-Push.git
pip install -r requirements.txt
```

## 配置

```bash
cp config.py.example config.py
```

支持过滤城市进行推送，在配置文件中配置需要通知的城市。

考虑到部分同学墙内部署，增加了镜像站爬虫，数据来自墙内镜像地址：http://2019ncov.tk/ ，在配置文件中配置 `TelegramMirror` 即可。

### 微信通知

微信通知使用方糖大叔的 [Server酱](http://sc.ftqq.com/3.version)，修改配置文件填写 Token 即可。

### 钉钉通知

钉钉群机器人 API Token 申请参考：[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq/26eaddd5)

### 微博

~~直接发微博：修改配置文件中微博发送地址和 cookie 即可。微博需要在网页版手动抓取登陆 Cookie，且过期时间较短。~~

~~由于部署在 AWS 海外区域，发现直接使用 Cookie 调用微博发送接口失败，于是在[腾讯云云函数(SCF)](https://cloud.tencent.com/document/product/583)上实现发送微博，进行远程调用。(阿里云同理，当然也可以自建服务)~~

~~如需使用云函数 SCF ，将 `weibo.py` 与 `weiboSCF.py` 上传至腾讯云 SCF，配置 API 网关触发方式即可，当然要修改`weiboSCF.py`里面的 `Cookie` 配置。 ~~

不建议使用上述方法，推荐使用[WeiboSender](https://github.com/wangke0809/WeiboSender)，登陆态维持时间长且比较稳定。

## 启动

```bash
python main.py
```

### Github Actions 定时启动

Github Actions 运行时可直接访问 Telegram ，解决了国内服务器不能访问某些资源的问题，运行记录见：[这里](https://github.com/wangke0809/2019-nCoV-Push/actions)

Github Actions 需要通过 Redis 记录已通知消息 id，配置文件中 `Redis` 配置项格式为 `redis://:password@host:6379/0`。

已经配置了每隔 5 分钟[自动运行脚本](https://github.com/wangke0809/2019-nCoV-Push/blob/master/.github/workflows/pythonapp.yml)，需要在配置文件中通过环境变量配置需要使用的通知方式，同时将通知需要的 Token 设置在项目的 `secret`里。

需要的环境变量：

```yaml
DingTalkToken: ${{ secrets.DingTalkToken }}
DingTalkWord: ${{ secrets.DingTalkWord }}
RedisUrl: ${{ secrets.RedisUrl }}
WeiboUrl: ${{ secrets.WeiboUrl }}
```

当前脚本启动命令如下，可根据需求修改

```bash
cp config.py.example config.py
python main.py action
```

## 效果预览

| ![](https://github.com/wangke0809/2019-nCoV-push/blob/master/imgs/DingTalk.jpg?raw=true) | ![](https://github.com/wangke0809/2019-nCoV-push/blob/master/imgs/Wechat.jpg?raw=true) | ![](https://github.com/wangke0809/2019-nCoV-push/blob/master/imgs/Weibo.jpg?raw=true) |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
|               钉钉群机器人               |               微信Server酱               |               微博               |
