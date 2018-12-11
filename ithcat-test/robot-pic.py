import itchat
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import duowan as dw
import os


# 发送信息
def send_msg():    
    dw._init()
    dw.run()    

    # group  = itchat.get_friends()
    group = itchat.get_chatrooms(True)
    for g in group:
        print(g['NickName'])
    user_info = itchat.search_chatrooms(name='百万基佬群') 
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        rootdir = './download/'
        file_list = os.listdir(rootdir)
        for i in range(0,len(file_list)):
            path = os.path.join(rootdir,file_list[i])
            if os.path.isfile(path):
                filename,filetype = os.path.splitext(path) 
                if filetype=='.mp4':
                    res = itchat.send_video(path, toUserName=user_name)
                else:
                    res = itchat.send_image(path, toUserName=user_name)
                print('%s%s%s已经发送'%(res,filename,filetype))
                break
        print('fuck over')

# 定时任务
def after_login():
    sched.add_job(send_msg,'cron',day = '*',hour=23,minute=1,second=11)
    # sched.add_job(send_msg,'interval', seconds=3)
    sched.start()

def after_logout():
    sched.shutdown()

if __name__ == '__main__':
    sched = BlockingScheduler()
    itchat.auto_login(hotReload=True)
    # itchat.auto_login(loginCallback=after_login, exitCallback=after_logout)
    after_login() 
    # send_msg()
    # itchat.run()