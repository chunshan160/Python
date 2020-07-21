#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/20 21:25
#@Author :春衫
#@File :123.py

'''
height、width
size = driver.get_window_size()
start_x = size["width"]*0.9
start_y = size["height"]*0.5
end_x = size["width"]* 0.1
end_y = size["height"]*0.5
#从右向左滑
driver.swipe(start_x,start_y, end_x, end_y, 200)
#从左向右滑
driver. swipe(end_x, end_y, start_x,start_y,200)
#上下滑动
#向上滑动:X轴不变，Y轴从大到小。
#向上滑动:X轴不变，Y轴从小到大。
driver.swipe(size["width"]* 0.5,size["height"]* 0.9,size["width"]* 0.5,size["height"]* 0.1)
driver.swipe(size["width"]* 0.5,size["height"]* 0.1,size["width"]* 0.5, size["height"]* 0.9)


appium-模拟触屏
TouchAction类
将一系列的动作放在一个链条中，然后将该链条传递给服务器。服务器接受到该链条后，解析
个动作，逐个执行。
短按(press)
长按(longPress)
点击(tap)
移动到(move_to)X,y为相对上一个坐标的移动距离
等待(wait)
释放(release)
执行(perform)
取消(cancel)


ele = driver.find_element_by_id("")
#元素的大小
size = ele.size
#均分的步长高和宽一样。
step = size["width"]/6
#元素的起点坐标–左上角
ori = ele.location
point1 = (ori["x"]+step,ori["y"]+step)
point2 =(point1[o] + step*2, point1[1]) 相对于point1,X轴增加了2*step
point3 = (point2[o] + step*2, point2[1]) 相对于point2,X轴增加了2*step
point4 =(point3[0]- step*2，point3[1] + step*2) #相对于point3,X轴减少了2*step，Y轴增加了2*step
point5 =(point4[0], point4[1] + step*2) #相对于point4，X轴不变，Y轴增加了2*step

TouchAction(driver).press(x=point1[o],y=point1[1]).wait(200).\
move_to(x-point2[o],y=point2[1]).wait(200).\
move_to(x-point3[o],y-point3[1]).wait(200). \
move_to(x=point4[o],y point4[1]).wait(200). \
move_to(x point5[o],y=point5[1]).wait (200).\
release().\
perform()



hybird混合应用自动化方案
基于UiAutomator+Chromedriver
native部分则uiautomator,webview部分走chromedriver,二者结合
要求:
android 4.4+
webview必须为debug版本
获取webview页面的三种方式:
1、chrome://inspect，需要FQ
2、使用driver.page_source获取html页面
3、找开发人员要源文件
4、uc-devtools 不需要FQ




ariver.1ina_element_oy_anaro1a_ulautomator(1oc).cL1cKo
#等待WebView元素出现-html
time.sleep(1)
#前提:代码可以识别到webview需要开启app的webview debug属性。
#context#原生控件#webview
#1\先列出所有的context
cons = driver.contexts#t列表
print(cons)
#2、切换至webview
driver.switch_to.context(cons[-1])
#3、切换之后:当前的操作对象:html页面
#等待元素可见
lWebDriverlWait(driver, 20).until(EC.visibility_of_element_located(MobileBy.CLASS_NAME,’android.webkit.WebView
WebDriverWait(driver,20). until(EC.visibility_of_element_located((MobileBy.XPATH ’//button[@class="bottom-btn
driver.find_element_by_xpath('//button[@class="bottom-btn buy"]').click()



'''
