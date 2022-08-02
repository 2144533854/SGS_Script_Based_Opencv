首先这个脚本需要用雷电模拟器 

第一步安装python，下载后安装即可。
https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe

第二步 安装包 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python

第三步运行cop.py 应该会有如下问题：

1、Local_Screenshots_Path = r'C:\Users\st\Documents\雷电模拟器\Pictures\Screenshots'  
这个路径是雷电模拟器与电脑截图连通的地方（意思是说雷电模拟器进行截图的图片，会同步到电脑上），需要保证有这个文件夹。

2、下面两个exe路径要有，如果是前面路径名称不一致需要改成一致，比如有人可能把不安装在D盘，装在C盘，那么就需要把字符串中的D替换为C。

ldconsole_exe = 'D:\\Changzhi\\dnplayer2\\ldconsole.exe '
ld_exe = 'D:\\Changzhi\\dnplayer2\\ld.exe '

