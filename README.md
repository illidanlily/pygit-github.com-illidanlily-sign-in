第二次软工结对编程作业
==
环境搭建
=
在运行之前请确保自己的已安装以下：<br>
 1.python<br>
 2.numpy  可在pycharm或vscode直接安装<br>
 3.vscode或pycharm（可选）<br>
 下载链接：<br>
[python环境](URL "https://www.python.org/")<br>
[pycharm](URL "https://www.jetbrains.com/pycharm/")<br>
[vscode](URL "https://code.visualstudio.com/")<br>

运行代码
=
在git clone完该仓库之后首先运行data_create.py,该文件是数据集生成器，会在d盘生成五个csv文件，每个文件对应相应课程的学生名单以及签到情况<br>
生成文件：<br>
![图片](https://github.com/illidanlily/pygit-github.com-illidanlily-sign-in/blob/master/QQ%E5%9B%BE%E7%89%8720221009124231.jpg)<br>
在已经生成5个csv文件后再运行qd.py文件，该文件是点名算法文件，会将对应的五个学生考勤表输入.直接运行.<br>
运行后会要求输入点名科目，能点名的科目有五个分别是：软件工程，图形学，概率论，接口技术，数据库。在输入完后会给出E的结果，并且会直接在数据集生成的文件上进行修改，将用于输入的文件作为输出文件输出<br>
## 运行结果：<br>
![图片](https://github.com/illidanlily/pygit-github.com-illidanlily-sign-in/blob/master/JZ%7BPF%25J%60Q%7B90K9_22%5BC%7B0MF.png)<br>
生成文件即为引用的文件<br>

算法
=
![图片](https://github.com/illidanlily/pygit-github.com-illidanlily-sign-in/blob/master/356ff1b0c7784764aebf5b62607adec0.png)<br>
在考勤表内有20次课考勤情况，到了为1缺勤为0，当点到名该值为1则为无效点名总请求次数+1<br>
若点到名该值为0则总请求次数和有效次数都+1<br>
在点名时会根据该生绩点生成一定权重的点名概率，并且在一次点名后会根据该生考勤情况来决定下一次点名的概率<br>
最后使输出的E能够稳定在0.9左右
