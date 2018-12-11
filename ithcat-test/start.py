import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     print('%s:%s'%(msg,msg.fileName))
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register([TEXT,PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def group_text(msg):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+msg.type)
    path = './download/'
    msg.download(path+msg.fileName)
    # from_user = ''
    if msg['ToUserName'] == from_group:
        if msg.type==RECORDING:
            itchat.send_file(path+msg.fileName,to_group)
            pass
        else:                
            itchat.send('%s:%s'%(msg['ActualNickName'],msg['Content']),to_group)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" over")


itchat.auto_login(hotReload=True)
from_group = ''
to_group= ''
group  = itchat.get_chatrooms(update=True)
for g in group:
    if g['NickName'] == '桔梗,秋之暖,断风格男、':#从群中找到指定的群聊
        from_group = g['UserName']
        # for menb in g['MemberList']:
        #     #print(menb['NickName'])
        #     if menb['NickName'] == "断风格男、":#从群成员列表找到用户,只转发他的消息
        #         from_user = menb['UserName']
        #         break
    if g['NickName'] == '家': #把消息发到这个群
        to_group = g['UserName']
print(from_group)
print(to_group)
itchat.run()