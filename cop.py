import time

import numpy as np

import cv2
import shutil
import os
import time
from datetime import datetime, timedelta

import os

Bath_Path=os.path.abspath(__file__).replace('CONFIG.py','')

Real_Screenshots_Path =os.path.join(Bath_Path,'pictures','Screenshots')
Real_source_Path = os.path.join(Bath_Path,'pictures','source')
NumPic_for_Award = os.path.join(Bath_Path,'pictures','number')

Local_Screenshots_Path = r'C:\Users\st\Documents\雷电模拟器\Pictures\Screenshots'
print('-------脚本配置初始化-------')
if not os.path.exists(Local_Screenshots_Path):
    print(f'第一次使用请修改用户名  \n将cop.py文件 第19行代码   {Local_Screenshots_Path}   中C:\\Users\\ 后面改为自己用户名名称\n')
DELAY=2
print(f'点击操作默认延迟为2秒，当前为{DELAY}秒 如果需要更改，请修改CONFIG.py文件第14行代码 DELAY={DELAY}\n')

ldconsole_exe = 'D:\\Changzhi\\dnplayer2\\ldconsole.exe '
ld_exe = 'D:\\Changzhi\\dnplayer2\\ld.exe '
print(f'请根据自己电脑配置,找到雷电模拟器的ldconsole.exe和ld.exe路径，如何和当前路径不符，请去将cop.py文件 第26、27行代码修改 \n\n当前路径为{ldconsole_exe}  {ld_exe}')

print('-------脚本配置初始化结束-------')






class Dnconsole:
    # 请根据自己电脑配置
    console = ldconsole_exe
    ld = ld_exe
    share_path = Local_Screenshots_Path

    def copy_img(self, s):
        name = os.path.join(Real_Screenshots_Path, s)
        shutil.copy(name, Real_source_Path)

    @staticmethod
    def launch(index: int):
        cmd = Dnconsole.console + 'launch --index ' + str(index)
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    @staticmethod
    def dnld(index: int, command: str, silence: bool = True):
        cmd = Dnconsole.ld + '-s %d "%s"' % (index, command)
        # print(cmd)
        if silence:
            os.system(cmd)
            return ''
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    @staticmethod
    def touch(index: int, x: int, y: int, delay: int = 0):
        if delay == 0:
            Dnconsole.dnld(index, 'input tap %d %d' % (x, y))
        else:
            Dnconsole.dnld(index, 'input swipe %d %d %d %d %d' % (x, y, x, y, delay))
def copy_img(s):
    name = os.path.join(Real_Screenshots_Path, s)
    shutil.copy(name, Real_source_Path)


def touch(index: 0, x: int, y: int, defualt_delay=DELAY):
    if not defualt_delay:
        Dnconsole.dnld(index, 'input tap %d %d' % (x, y))
    else:
        Dnconsole.dnld(index, 'input tap %d %d' % (x, y))
        time.sleep(defualt_delay)


def ShowImage(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)  # 等待时间，0表示任意键退出
    cv2.destroyAllWindows()


def get_pos(s1: str, s2: str):
    name1 = os.path.join(Real_Screenshots_Path, s1)
    name2 = os.path.join(Real_source_Path, s2)
    img1 = cv2.imread(name1, 0)
    img2 = cv2.imread(name2, 0)

    temp = img1.copy()
    result = cv2.matchTemplate(img2, img1, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    (startX, startY) = maxLoc
    endX = startX + img2.shape[1]
    endY = startY + +img2.shape[0]
    x1 = (startX + endX) // 2
    y1 = (startY + endY) // 2
    # print(0,','+str(x1)+',',str(y1))
    cv2.rectangle(temp, (startX, startY), (endX, endY), (255, 0, 0), 2)
    import numpy as np
    # result = np.hstack((img1, temp))
    # ShowImage('temp', temp)
    # return name1
    return startX, endX, startY, endY


def get_daily_number_pic(s):
    Dnconsole.dnld(0, 'screencap -p /sdcard/Pictures/Screenshots/{0}'.format(s))

    copy_img(s)

    temp2 = os.path.join(NumPic_for_Award, s)
    name = os.path.join(Real_source_Path, s)

    img1 = cv2.imread(name, 0)
    img1 = img1[291:339, 360:400]
    cv2.imwrite(temp2, img1)
    print(img1)
    return temp2


def get_now_pic(s):
    Dnconsole.dnld(0, 'screencap -p /sdcard/Pictures/Screenshots/{0}'.format(s))
    copy_img(s)
    return s


def compare_pic(img1, img2):
    try:
        img3 = img1 - img2
    except Exception as e:
        print(str(e))
        import ipdb;
        ipdb.set_trace()
    status = np.where(img3 != 0)[0].shape[0]
    return status  # status==0 表示两个图片相同


def get_renwu_number(name2):
    img2 = cv2.imread(name2, 0)
    for i in range(1, 13):
        name = os.path.join(NumPic_for_Award, str(i) + '.png')
        img1 = cv2.imread(name, 0)
        j = compare_pic(img1, img2)
        if j == 0:
            return i
        else:
            continue

    # for i in range(0,40):
    #
    #     print(zero[i]==img3[i])


def get_yuanbao():  # 领取元宝
    touch(0, 230, 467, 2)
    touch(0, 230, 467, 2)
    touch(0, 1588, 211, 2)
    touch(0, 300, 170, 2)
    x = 760
    y = 80

    for i in range(3, 10):
        print(' ')
        for j in range(1, i):
            touch(0, x + j * 200, y)
            print(x + j * 200, y, j)

        x -= 110
        y += 100


def get_renwu_award():  # 领取任务
    touch(0, 866, 990, 2)
    s = 'number.png'
    name = get_daily_number_pic(s)
    nubmer = get_renwu_number(name)
    print(f'待领取的任务数量为:{nubmer}个')
    for i in range(0, nubmer):
        print(f'领取第{i + 1}个任务')
        touch(0, 1581, 386, 3)
    # -------那年今日任务--------
    touch(0, 1581, 386, 3)
    touch(0, 1097, 635)
    touch(0, 1419, 635, 2)
    touch(0, 1097, 635)
    touch(0, 1419, 635, 2)
    touch(0, 1581, 386, 0.5)
    # -------领取上方宝箱--------
    touch(0, 980, 170, 1)
    touch(0, 1180, 170, 1)
    touch(0, 1380, 170, 1)
    # -------领取下方宝箱--------
    touch(0, 970, 1000, 1)
    touch(0, 970, 1000, 1)
    touch(0, 1380, 1000, 1)
    touch(0, 1380, 1000, 1)
    # -------领取摇钱树--------
    get_yuanbao()


def yanlian_guaji():
    sgs_time = 0
    while sgs_time < 60 * 60:
        second_count = 3
        while (True):
            # if k==0:#第一次需要从主界面进入
            #     touch(0, 427, 574,2)
            touch(0, 289, 852, 2)
            touch(0, 1600, 573, 2)

            c1 = datetime.now().now()
            for _ in range(0, second_count):
                print(f'等待60秒')
                time.sleep(60)
                sgs_time += 60
            for _ in range(0, 3):
                touch(0, 316, 704)
            if second_count > 1:
                second_count -= 1
            get_now_pic('shilian.png')
            x, x1, y, y1 = get_pos('shilian.png', 'siwangjiemian.png')
            name2 = os.path.join(Real_Screenshots_Path, 'shilian.png')
            name3 = os.path.join(Real_source_Path, 'siwangjiemian.png')
            name4 = os.path.join(Real_Screenshots_Path, 'siwangjiemian.png')

            img1 = cv2.imread(name2, 0)
            img2 = cv2.imread(name3, 0)
            img3 = img1[y:y1, x:x1]
            cv2.imwrite(name4, img3)
            img4 = cv2.imread(name4, 0)

            num = compare_pic(img2, img4)
            if num == 10957:
                print(f'当前已挂机{sgs_time // 60}分钟 ')
                break
            else:
                print(f'当前检测未完成  进入下次等待')
                continue
    touch(0, 1854, 79, 2)  # 点击返回
    touch(0, 1854, 79, 2)  # 点击返回






# touch(0 ,1253, 298)  #点击单人匹配
#
# time.sleep(10)
#
# touch(0 ,1635, 257)  #点击推荐


# touch(0 ,1854, 78)  #点击加号
# touch(0 ,1701, 89)  #点击托管
# touch(0 ,1452, 85)             #点击退出游戏
# 0 ,1789, 839  死亡
#

#    神吕蒙
# touch(0,380,476)             #点击5人军争
# touch(0, 1402, 238)             #点击演练
# touch(0 ,1854 ,79)             #点击加号
# touch(0 ,1452, 85)             #点击退出游戏
# touch(0 ,1152, 616)             #点击确定

# touch(0,380,476)
# touch(0, 1402, 238)
# time.sleep(5)

# for i in range(0,2):
#     touch(0,380,476)             #点击5人军争
#     touch(0 ,1546, 853)          #点将
#     time.sleep(1)
#     touch(0 ,1624, 193)          #点神
#
#     touch(0 ,580, 359)          #点神吕蒙
#
#     touch(0 ,1854 ,79)             #点击返回
#
#     touch(0, 1402, 238)             #点击演练
#     time.sleep(10)
#     touch(0 ,223, 652)             #选神吕蒙
#     touch(0 ,223, 652)             #选神吕蒙
#     touch(0 ,1854 ,79)             #点击加号
#     touch(0 ,1452, 85)             #点击退出游戏
#     touch(0 ,1152, 616)             #点击确定
#     time.sleep(10)

def writes_and_receive(f, minute):
    f.writelines(f'{datetime.now().now()}  领取{minute}分钟礼包')
    print(f'领取{minute}分钟礼包')
    touch(0, 1854, 79)  # 点击返回
    touch(0, 1854, 79)  # 点击礼包
    touch(0, 427, 574, 2)


f = open('7mmtv.txt', 'a')


def daily():
    start_time = datetime.now().now()
    f.writelines(f'-----------{datetime.now().now()}-----------  开始日常任务')
    Dnconsole.launch(0)  # 打开模拟器
    touch(0, 427, 574, 2)
    for i in range(0, 30):
        print(f'第{i}次演练')
        f.writelines(f'{datetime.now().now()}  第{i}次演练')
        # if datetime.now().now()-start_time>=timedelta(minutes=10):
        #     writes_and_receive(f,10)
        # elif datetime.now().now()-start_time>=timedelta(minutes=15):
        #     writes_and_receive(f,15)
        # elif datetime.now().now()-start_time>=timedelta(minutes=30):
        #     writes_and_receive(f, 30)

        touch(0, 380, 476)  # 点击5人军争

        touch(0, 1546, 853)  # 点将

        time.sleep(1)

        touch(0, 1152, 365)  # 点神吕蒙

        touch(0, 1854, 79)  # 点击返回

        touch(0, 1402, 238)  # 点击演练

        time.sleep(12)
        touch(0, 223, 652)  # 选神吕蒙
        touch(0, 223, 652, 2)  # 选神吕蒙

        touch(0, 1864, 79, 2)  # 点击加号
        touch(0, 1452, 85)  # 点击退出游戏

        touch(0, 1152, 616)  # 点击确定
        time.sleep(10)

        f.writelines(f'-----------{datetime.now().now()}-----------  结束日常任务\n')
    touch(0, 1864, 79)  # 点击返回


def paiwei_guaji():
    pass


def huanhua_guaji():
    touch(0, 292, 974)
    time.sleep(1.5)
    touch(0, 707, 622)
    time.sleep(1.5)
    touch(0, 1647, 430)


def shilian_guaji():
    get_now_pic('shilian.png')
    name3 = r'C:\Users\st\Desktop\web\izone\sgs\pictures\source\kongxue.png'
    img2 = cv2.imread(name3, 0)


# 幻化挂机
# get_now_pic('huanhua.png')
# x,x1,y,y1=get_pos('huanhua.png','kongxue.png')
# name2=r'C:\Users\st\Desktop\web\izone\sgs\pictures\Screenshots\huanhua.png'
# name3=r'C:\Users\st\Desktop\web\izone\sgs\pictures\source\kongxue.png'
# img1=cv2.imread(name2, 0)
# img2=cv2.imread(name3, 0)
# img3=img1[y:y1,x:x1]
# print(compare_pic(img2,img3))
# # ShowImage('1',img3)
# import ipdb;ipdb.set_trace()
# cv2.imwrite(r'C:\Users\st\Desktop\web\izone\sgs\pictures\source\kongxue.png',img3)
# 试炼挂机

def sleep_time(c1, second):
    from datetime import datetime, timedelta
    # 获取当前的日期，年月份

    time.sleep(second)
    c2 = datetime.now().now()
    c3 = c2 - c1
    print(c3)
    print(c3 <= timedelta(seconds=03.906222))


while (True):
    print('---------三国杀挂机系统---------')
    print('---------1、日常演练 ----------')
    print('---------2、任务领取+元宝树领取----')
    print('---------3、武将演练挂机---------')
  #  print('---------4、幻化之战挂机---------')
    print('-----------0、退出系统-----------')
    c=input('请选择功能：')
    c=int(c)
    if c==1:
        daily()
        # yanlian_guaji()
        # get_renwu_award()
    elif c==2:
        get_renwu_award()
    elif c==3:
        yanlian_guaji()
    elif c==0:
        break
#
# # Dnconsole.launch(0)#打开模拟器
# s1 = 'junzhenchang.png'
# s2 = 'yanlian.png'
# name=get_pos(s,s2)
# print(name)

# reader = easyocr.Reader(['ch_sim','en'])
# # 读取图像
# result = reader.readtext(name)
# # 结果
# print(result)


# touch(0,380,476)             #点击5人军争
# touch(0, 1402, 238)             #点击演练
# touch(0 ,1854 ,79)             #点击加号
# touch(0 ,1452, 85)             #点击退出游戏
# touch(0 ,1152, 616)             #点击确定

# touch(0,380,476)
# touch(0, 1402, 238)
# time.sleep(5)


#
# def ShowImage(name, image):
#     cv2.imshow(name, image)
#     cv2.waitKey(0)  # 等待时间，0表示任意键退出
#     cv2.destroyAllWindows()
#
#
# import cv2
# import numpy as np
# import os
# s1='1.png'
# s2='return.png'
# path= r'C:\Users\st\Desktop\web\izone\sgs\pictures\Screenshots'
# path2= r'C:\Users\st\Desktop\web\izone\sgs\pictures\source'
# name1=os.path.join(path,s1)
# name2=os.path.join(path2,s2)
# image = cv2.imread(name1, 0)
# template = cv2.imread(name2, 0)
# h, w = template.shape[:2]
#
# ShowImage('image', image)
# ShowImage('template', template)
# print(image.shape)
# print(template.shape)
#
# temp = image.copy()
# res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = min_loc
# bottom_right = (top_left[0]+w, top_left[1]+h)
# cv2.rectangle(temp, top_left, bottom_right, 255, 2)

# result = np.hstack((image, temp))
# ShowImage('temp', result)
