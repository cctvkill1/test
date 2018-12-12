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
    file_list = dw.get_value('file_list') 
    group = itchat.get_chatrooms(True)
    for g in group:
        print(g['NickName'])
    user_info = itchat.search_chatrooms(name='垃圾程序猿高级交流会所') 
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
        
        print('多玩 fuck all over')

# 发送抖音周热
def send_douyin_msg():   
    dy._init()
    dy.run()
    file_list = dy.get_value('file_list')
    group = itchat.get_chatrooms(True)
    for g in group:
        print(g['NickName'])
    user_info = itchat.search_chatrooms(name='垃圾程序猿高级交流会所') 
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        for item in file_list:
            # print(item)
            res = itchat.send_msg(item['title'], toUserName=user_name)
            filetype = item['file_name'].split('.')[-1]
            if filetype=='mp4':
                res = itchat.send_video(item['file_name'], toUserName=user_name)
            else:
                res = itchat.send_image(item['file_name'], toUserName=user_name)
            print('已经发送%s %s'%(res,item['file_name']))
            # break
        print('抖音 fuck all over')

# 定时任务
def crontab(): 
    print('定时任务开始')
    sched.add_job(send_dw_msg,'cron',day = '*',hour=7,minute=59,second=1)
    # sched.add_job(send_dw_msg,'interval', seconds=3)
    # 0,3,6 是星期1星期4星期天
    sched.add_job(send_douyin_msg,'cron',day_of_week = '0,3,6' ,hour=9,minute=10,second=1)
    sched.start()

def after_logout():
    sched.shutdown()

if __name__ == '__main__':
    sched = BlockingScheduler()
    itchat.auto_login(enableCmdQR=2,hotReload=True)
    # itchat.auto_login(loginCallback=crontab, exitCallback=after_logout)
    crontab() 
    # itchat.run()
    
    # todo 做个全家生日播报