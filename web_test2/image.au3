#定位到打开窗口
WinActivate("打开");
# #等待文件上传  毫秒
Sleep(1000)
# 设置上传的文件
ControlSetText("打开","","Edit1","D:\Pycharm_workspace\web\picture.jpg")
# #等待文件上传  毫秒
Sleep(1000)
# 点击上传按钮
ControlClick("打开","","Button1")