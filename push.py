from dingtalkchatbot.chatbot import DingtalkChatbot


class Push(object):

    def __init__(self, token, keyWord):
        self.d = DingtalkChatbot(
            'https://oapi.dingtalk.com/robot/send?access_token=%s' % token)
        self.keyWord = keyWord

    def sendMsg(self, title, msg, is_at_all=False):
        self.d.send_markdown(title=self.keyWord + title, text=msg, is_at_all=is_at_all)


if __name__ == '__main__':
    msg = '#重要通知【人社部：企业不得开除因疫情不能正常上班的员工】人社部24日对外发布通知，明确对新型冠状病毒感染的肺炎患者、疑似病人、密切接触者在其隔离治疗期间或医学观察期间以及因政府实施隔离措施或采取其他紧急措施导致不能提供正常劳动的企业职工，企业应当支付职工在此期间的工作报酬，并不得依据劳动合同法第四十条、四十一条与职工解除劳动合同。在此期间，劳动合同到期的，分别顺延至职工医疗期期满、医学观察期期满、隔离期期满或者政府采取的紧急措施结束。（澎湃新闻）'
    push = Push("23a4cdba7b05a4026be8ff229feb193c19f3be8f7948d6dcc1c53f09008cd6ed")
    push.sendMsg("test,Giao", msg)
