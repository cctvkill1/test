test
========
上传一些小实验
------------ 
###2016-7-12
网上找了个py抓妹子图试试看<br/>
将py2 改成py3，# import urllib, urllib2//被淘汰了<br/>
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2<br/>
    py3 正则匹配改一下编码
    data = urllib2.urlopen(url_index).read()
    data = data.decode('GBK')<br/> 
###2016-7-3
投票测试脚本<br/>
先随机生成ip，然后curl post 参数 伪装IP就OK了<br/>
用命令行 跑会快些<br/> 
###2016-6-17
七人转生成对阵算法（21个组合）<br/>
首先两两搭档 生成10.5个对阵<br/>
然后从组合中再随机抽取 组成剩下3.5个对阵，使得所有数字都是出现8次<br/>
注意一个组合的对手 只能出现1次 （如：12:34，下面12的组合就不能再遇到3或者4）<br/>
这算法太糙了 需要优化 速度太慢了
###2016-6-8
八人转生成对阵算法（28个组合）<br/>
试了下递归 规律没找对 好几个位置 出不来数据<br/>
然后全队列 感觉更乱了 1开头的有5040种组合 再排7排 组合更多 <br/>
然后循环的时候发现个新规律 每次出现的对手先continue 并且对手大于前面的数字<br/>
然后再循环一遍 保证出现对手只出现2次
###2015-4-20
修改了点鼠标画线的颜色 上传了雪花烟火特效
###2015-4-13
明天要交1W块的罚款（上班顺风车搭人被抓算非法运营）以后不要犯这种傻子才犯的错误<br>
canvas时钟添加了刻度
###2015-3-24
几天没学习了 今天看了下canvas的许多特效 还是有很多地方不会的不懂的 下了几个简单的看了下  准备做几个简单的特效
###2015-3-19
今天做的不多 学了下canvas 合成 输出base64图 保存可以借助其他js <br>
然后修改了前两天做的时钟bug 0-1秒不走 及其他时刻走字不准确
然后加了声音 <br>然后学了下基础操作元素 添加事件等
js canvas有些类库 <a href="http://jcscript.com/">http://jcscript.com/</a>   jCanvaScript 还有 Fabric.js<br> 
看了下其他特效 空了研究下并自己写写特效游戏之类的	
###2015-3-18
今天没做什么 看了下视频 了解canvas去操作像素 可以以做倒立渐变反色 马赛克<br/>
其中有个问题 canvas 需要加载 图片操作像素时 遇到getImageData 报错 查找了些资料<br/>
<a href="http://www.cnblogs.com/jdksummer/articles/2565998.html">http://www.cnblogs.com/jdksummer/articles/2565998.html</a>
为了阻止欺骗，浏览器会追踪 image data。当你把一个“跟canvas的域不同的”图片放到canvas上，这个canvas就成为 “tainted”(被污染的，脏的)，浏览器就不让你操作该canvas 的任何像素。这对于阻止多种类型的XSS/CSRF攻击（两种典型的跨站攻击）是非常有用的。<br/>
搭建个本地服务器环境就ok了<br/>

###2015-3-17
学习了下canvas的旋转 偏移 缩放<br/>
画图 及 图片旋转，颜色渐变，显示文字，阴影<br/>
像素 这点以后会用到
###2015-3-16
很久没学习了 突然想看下canvas<br/>
学习了下canvas的入门用法<br/>
写了3个demo页面<br/>
鼠标画画<br/>
移动方块<br/>
时钟<br/>
###2014-9-25
很久没更新了<br/>
随便搞了个俄罗斯农民乘法 js实现挺简单的 算是小儿科<br/>
不过我觉得这种乘法本身挺有意思的
###2014-9-9
上传了前些天无聊做的几道题<br/>
猴子吃桃子 弱智算法 简单的循环或者递归<br/>
约瑟夫环 2中算法 第二中自己写的 js中删除数组的方法没实现 最后是通过改值<br/>
八皇后 问题 代码简短的话采用递归<br/>
arguments这个可以获得实参（包括隐藏的参数）<br/>
熟悉下立即执行函数及js模块化编程<br/>
###2014-8-19
实在无聊啊 上传上星期做的个SVG动画<br/>
其中需要引用prefixfree.min.js 才能控制stroke-dashoffset 做出动画效果<br/>
原理就是<br/>
troke-dasharray 和 stroke-dashoffset