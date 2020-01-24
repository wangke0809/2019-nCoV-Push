# 2019-nCoV-DingTalk-Push

抓取 Telegram 频道 @nCoV2019 进行钉钉通知。

频道地址：https://t.me/s/nCoV2019

为什么不使用频道提供的 RSS ？因为 RSS 内容不实时。

# 使用说明

## 安装

```bash
git clone https://github.com/wangke0809/2019-nCoV-DingTalk-Push.git
pip install -r requirements
```

## 配置

```bash
cp config.py.example config.py
```

修改 API。

## 启动

```bash
python main.py
```