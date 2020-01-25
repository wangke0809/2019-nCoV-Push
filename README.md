# 2019-nCoV-Push

抓取 Telegram 频道 @nCoV2019 进行通知。

现在已经支持转发频道内容到钉钉群和微博 [@聚合提醒](https://www.weibo.com/u/7378955365)。

频道地址：https://t.me/s/nCoV2019

为什么不使用频道提供的 RSS ？因为 RSS 内容不实时。

为什么不抓取丁香园？因为丁香园聚合信息不够全。

爬虫 `spider.py` 可单独使用，已经解析出`id, tag, city, title, text, refUrl`

# 使用说明

## 安装

```bash
git clone https://github.com/wangke0809/2019-nCoV-Push.git
pip install -r requirements.txt
```

## 配置

```bash
cp config.py.example config.py
```

修改 PushToken 即可使用，如有需要，后续考虑增加其他推送渠道。

钉钉群机器人 API Token 申请参考：[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq/26eaddd5)

微博需要在网页版抓取登陆 Cookie 。由于部署在 AWS 海外区域，发现直接使用 Cookie 调用微博发送接口失败，于是在[腾讯云云函数(SCF)](https://cloud.tencent.com/document/product/583)上实现发送微博，进行远程调用。

如需使用云函数 SCF ，将 `weibo.py` 与 `weiboSCF.py` 上传至腾讯云 SCF，配置 API 网关触发方式即可，当然要修改`weiboSCF.py`里面的 `Cookie` 配置。 

## 启动

```bash
python main.py
```
