# -*- coding: utf8 -*-  
import random  
class Doudizhu:#斗地主的一个类，下面使用的变量如果在两个实例方法里使用，要定义成实例属性。要不然会出现后面不能引用前面的变量。  
    def __init__(self):  
        self.a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,  
                19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,  
                36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]  
    def xipai(self):#洗牌  
        random.shuffle(self.a)  
        n=random.randint(1,54)  
        b=self.a[:n]  
        c=self.a[n:]  
        self.a=c+b  
    def fapai(self):#发牌  
        self.str1=self.a[:-3:3]  
        self.str2=self.a[1:-3:3]  
        self.str3=self.a[2:-3:3]  
        self.str4=self.a[-3:]  
    def qiangdizhu(self):#抢地主  
        n=random.randint(1,3)  
        self.dizhu=n#定义一个实例属性，赋给地主的序号  
        if n==1:  
            self.str1+=self.str4  
        if n==2:  
            self.str2+=self.str4  
        if n==3:  
            self.str3+=self.str4  
    def mapai(self):#码牌  
        self.str1.sort(reverse=True)  
        self.str2.sort(reverse=True)  
        self.str3.sort(reverse=True)  
    def yingshe(self):#映射  
        paizd=[(0,'方片3'),(1,'梅花3'),(2,'红桃3'),(3,'黑桃3'),  
               (4,'方片4'),(5,'梅花4'),(6,'红桃4'),(7,'黑桃4'),  
               (8,'方片5'),(9,'梅花5'),(10,'红桃5'),(11,'黑桃5'),  
               (12,'方片6'),(13,'梅花6'),(14,'红桃6'),(15,'黑桃6'),  
               (16,'方片7'),(17,'梅花7'),(18,'红桃7'),(19,'黑桃7'),  
               (20,'方片8'),(21,'梅花8'),(22,'红桃8'),(23,'黑桃8'),  
               (24,'方片9'),(25,'梅花9'),(26,'红桃9'),(27,'黑桃9'),  
               (28,'方片10'),(29,'梅花10'),(30,'红桃10'),(31,'黑桃10'),  
               (32,'方片J'),(33,'梅花J'),(34,'红桃J'),(35,'黑桃J'),  
               (36,'方片Q'),(37,'梅花Q'),(38,'红桃Q'),(39,'黑桃Q'),  
               (40,'方片K'),(41,'梅花K'),(42,'红桃K'),(43,'黑桃K'),  
               (44,'方片A'),(45,'梅花A'),(46,'红桃A'),(47,'黑桃A'),  
               (48,'方片2'),(49,'梅花2'),(50,'红桃2'),(51,'黑桃2'),  
               (52,'小王'),(53,'大王')]  
        zdpai = dict(paizd)  
        paistr1=''  
        for i in range (len(self.str1)):  
            paistr1+=zdpai[self.str1[i]]+' '  
        paistr2=''  
        for i in range (len(self.str2)):  
            paistr2+=zdpai[self.str2[i]]+' '  
        paistr3=''  
        for i in range (len(self.str3)):  
            paistr3+=zdpai[self.str3[i]]+' '  
        self.user1=paistr1 #这里要把牌的序列赋给三个玩家的实例属性  
        self.user2=paistr2  
        self.user3=paistr3  
user=Doudizhu()#使用这个类时，要挨个使用实例的方法  
user.xipai()  
user.fapai()  
user.qiangdizhu()  
user.mapai()  
user.yingshe()  

print ('dizhu:',user.dizhu)  
print ('user1:',user.user1)  
print ('user2:',user.user2)  
print ('user3:',user.user3)  