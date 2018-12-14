import itchat
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler
import time
import duowan as dw
import douyin as dy
import json
import os
import requests


# 发送多玩信息
def send_dw_msg():    
    dw._init()
    dw.run()
    file_list = dw.get_value('file_list')
    begin_str = dw.get_value('begin_str') 
    # print(file_list)
    # group = itchat.get_chatrooms(True)
    # for g in group:
    #     print(g['NickName'])
    user_info = itchat.search_chatrooms(name='垃圾程序猿高级交流会所') 
    success = 0
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        if len(file_list)>0: 
            itchat.send_msg('---多玩图库播报开始--- '+begin_str, toUserName=user_name)
            for item in file_list:
                itchat.send_msg(item['title'], toUserName=user_name)
                filetype = item['file_name'].split('.')[-1]
                if filetype=='mp4':
                    res = itchat.send_video(item['file_name'], toUserName=user_name)
                else:
                    res = itchat.send_image(item['file_name'], toUserName=user_name)
                print('已经发送%s %s'%(res,item['file_name']))
                if '请求成功' in str(res):
                    success+=1
                    time.sleep(2)
                else:
                    itchat.send_msg('上一条发送失败了！让我静一静', toUserName=user_name)
                    time.sleep(10)
                # break
            
            # print('多玩 fuck over 共%d条 成功%d条'%(len(file_list),success))
            itchat.send_msg('---多玩图库播报结束---  共%d条 成功%d条'%(len(file_list),success), toUserName=user_name)

# 发送抖音周热
def send_douyin_msg():   
    dy._init()
    dy.run()
    file_list = dy.get_value('file_list')
    # print(file_list)
    group = itchat.search_chatrooms(name='垃圾程序猿高级交流会所') 
    success = 0
    if len(group) > 0:
        user_name = group[0]['UserName']
        if len(file_list)>0: 
            itchat.send_msg('---抖音视频播报开始---', toUserName=user_name)
            for item in file_list:
                # print(item)
                itchat.send_msg(item['title'], toUserName=user_name)
                filetype = item['file_name'].split('.')[-1]
                if filetype=='mp4':
                    res = itchat.send_video(item['file_name'], toUserName=user_name)
                else:
                    res = itchat.send_image(item['file_name'], toUserName=user_name)
                if '请求成功' in res:
                    success+=1
                print('已经发送%s %s'%(res,item['file_name']))
                # break
                time.sleep(2) 

            # print('抖音 fuck over 共%d条 成功%d条'%(len(file_list),success))
            itchat.send_msg('---抖音视频播报结束--- 共%d条 成功%d条'%(len(file_list),success), toUserName=user_name)

# 收发消息
@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    if  msg.text.startswith('#'): 
        # print('我收到: ' + msg.text[1:] )
        reply = get_response(msg.text[1:]) 
        msg.user.send(reply) 


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
    'key' : 'e64ad48100081ab77b668aa3105fe552', 
    'info' : msg,
    'userid' : '123456', 
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        r_str =  r.get('text')
        if r.get('list'):
            l = r.get('list')
            t = ''
            for li in l:
                t += li.get('name') or li.get('article')
                t += '\n'
                t += li.get('detailurl')
            r_str = r_str  + t
        if r.get('url'):
            r_str = r_str +'\n'+ r.get('url')
        return r_str
    except:
        return "未知错误，请联系群主" #出问题就回复“呵呵”
 
# 定时任务
def crontab(): 
    print('定时任务开始')
    sched.add_job(send_dw_msg,'cron',day = '*',hour=8,minute=30,second=1)
    sched.add_job(send_dw_msg,'cron',day = '*',hour=11,minute=50,second=1)
    sched.add_job(send_dw_msg,'cron',day = '*',hour=18,minute=1,second=1)
    # sched.add_job(send_dw_msg,'interval', seconds=3)
    # 0,3,6 是星期1星期4星期天
    sched.add_job(send_douyin_msg,'cron',day_of_week = '5' ,hour=10,minute=30,second=1)
    sched.start()

def after_logout():
    sched.shutdown()

if __name__ == '__main__':
    sched = BackgroundScheduler()
    itchat.auto_login(enableCmdQR=2,hotReload=True)
    crontab() 
    itchat.run()
    # test
    # send_dw_msg()
    # send_douyin_msg()

    # todo 做个全家生日播报