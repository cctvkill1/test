# encoding=utf-8 
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
 


def ungzip(data):
    try:  
        print('正在解压.....')
        data = gzip.decompress(data)
        # print(data)
        # print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data
 
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
 

# 链家新增加了ip流量异常判断 然后跳转到验证页面
# 首先是http://captcha.lianjia.com/ 这个页面 通过http://captcha.lianjia.com/human/ 获取 4张图和uuid 然后uuid写到 form表单里 表单里还有个bitvalue和_csrf
# _csrf是个验证的随机字符串  bitvalue 是用户选择图片的二进制数字 bitvalue ^= 1 << index;  1<<index 就是1向左移动index位 （1<<1 就是10 十进制是2 1<<2 就是100 十进制4……）
# 然后bitvalue做位异或运算 （例子：a的值为二进制的1010，b的值为二进制的1100，那么a^b = 0110） 大致效果就是 0000 4位中 选择了的补1  0001 0010 0011……然后转十进制
# 最后$.post('/human/' 服务器会写好cookie sessionstorage localstorage 再访问其他页面就OK了 
# 分析完了 实践部分还没搞

# 下面是cookie 抓取的例子

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Encoding': ' deflate', 这就不用解压了
    'Host': 'www.zhihu.com',
    'DNT': '1'
}
 
url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
# data = ungzip(data)     # 解压
_xsrf = getXSRF(data.decode())
 
url += 'login/email'
id = '这里填你的知乎帐号'
password = '这里填你的知乎密码'
postDict = {
        '_xsrf':_xsrf,
        'email': id,
        'password': password,
        'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
# data = ungzip(data)
 
print(data.decode())