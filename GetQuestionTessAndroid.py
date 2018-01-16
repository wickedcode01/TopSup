from PIL import Image
from common import screenshot, ocr, methods
from threading import Thread
import time
import sys

print("请选择APP。1、冲顶大会2、芝士超人3、西瓜视频")
print("请出现题目再按回车")
type = int(input());

while True:

    t = time.clock()
    # 截图
    screenshot.check_screenshot()

    img = Image.open("./screenshot.png")

    # 文字识别
    question, choices = ocr.ocr_img(img,type)
   # print(question,choices)
    # # 打开浏览器方法搜索问题
    # methods.run_algorithm(0, question, choices)
    # # 将问题与选项一起搜索方法，并获取搜索到的结果数目
    # methods.run_algorithm(1, question, choices)
    # # 用选项在问题页面中计数出现词频方法
    # methods.run_algorithm(2, question, choices)

    # 多线程
    #m1 = Thread(methods.run_algorithm(0, question, choices))
    m2 = Thread(methods.run_algorithm(1, question, choices))
    m3 = Thread(methods.run_algorithm(2, question, choices))
    #m1.start()
    m2.start()
    m3.start()

    end_time = time.clock()
    print('耗时:',end_time - t)
    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print('------------------------')
