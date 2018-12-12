import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import duowan as dw
import douyin as dy
import json
import os


# 发送多玩信息
def send_dw_msg():    
    dw._init()
    dw.run()
    f = open(dw.get_value('file_name_list'),'r')
    file_list = json.loads(f.read())
    # group  = itchat.get_friends()
    group = itchat.get_chatrooms(True)
    for g in group:
        print(g['NickName'])
    user_info = itchat.search_chatrooms(name='百万基佬群') 
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        for item in file_list:
            res = itchat.send_msg(item['title'], toUserName=user_name)
            filetype = item['file_name'].split('.')[-1]
            if filetype=='mp4':
                res = itchat.send_video(item['file_name'], toUserName=user_name)
            else:
                res = itchat.send_image(item['file_name'], toUserName=user_name)
            print('已经发送%s %s'%(res,item['file_name']))
            # break
        
        print('fuck all over')

# 发送抖音周热
def send_douyin_msg(): 
    print('来了老弟')
    pass

# 定时任务
def crontab(): 
    print('定时任务开始')
    sched.add_job(send_dw_msg,'cron',day = '*',hour=7,minute=55,second=1)
    # sched.add_job(send_dw_msg,'interval', seconds=3)
    sched.add_job(send_douyin_msg,'cron',day_of_week = '2,6' ,hour=11,minute=19,second=32)
    sched.start()

def after_logout():
    sched.shutdown()

if __name__ == '__main__':
    sched = BlockingScheduler()
    itchat.auto_login(hotReload=True)
    # itchat.auto_login(loginCallback=crontab, exitCallback=after_logout)
    # crontab() 
    send_dw_msg()
    # itchat.run()
    # todo 做个全家生日播报