# UI implement tutorial

## 配置开发环境
系统版本为 Ubuntu 18.04
### PyQt
1. 安装PyQt：
由于ROS的Python版本为2.7，所以需要安装对应Python2的PyQt
```bash
sudo apt install python-qt5
```
2. 安装QtDesigner, pyuic:
- QtDesigner: 以图形化界面创建编辑ui文件
- pyuic: 将ui文件转换为py文件
```
sudo apt install qt5tools-dev-tools
```
### ROS
1. 安装ROS：\
按照[官方步骤](http://wiki.ros.org/melodic/Installation/Ubuntu)安装ROS Melodic
2. 配置系统环境：\
配置系统环境变量
```bash
source /opt/ros/melodic/setup.bash
```
3. 创建工作空间：\
ROS包的编译与运行需要放在工作空间中，在合适位置创建ROS工作空间
```bash
mkdir -p catkin_ws/src
```
4. 创建包：\
由于UI需要与ROS连接，所以为UI创建ROS包
```bash
catkin_create_pkg vending_ui rospy std_msgs std_srvs
```
## 使用QtDesigner和PyQt搭建界面
使用QtDesigner设计编辑界面画面，使用PyQt编辑接口连接
### QtDesigner
- QtDesigner界面介绍
- 创建对话窗口Dialog
- 创建按钮PushButton
- 创建显示Label
- 创建数字显示LCD
- 创建显示区域GroupBox
- 创建布局Layout
- 创建文字输入LineEdit
### PyQt
- 转换ui文件\
通过`pyuic5`将由QtDesigner设计的ui文件转换为Python文件
```bash
pyuic5 ui_file.ui -o ui_file.py
```
- 调用ui文件\
导入转换好的ui文件，以及必要的Qt部件类
```python
from vending_demo_ui import *
from PyQt5.QtWidgets import QDialog, QApplication
```
创建Dialog界面类，实例化通过Designer编辑的ui
```python
class VendingUI(QDialog):
    def __init__(self):
        super(VendingUI, self).__init__()
        self.ui = UI_Dialog()
        self.ui.setupUi(self)
```
创建Qt程序，显示界面
```python
if __name__ == 'main':
    app = QApplication(sys.argv)
    v = VendingUI()
    v.show()
    sys.exit(app.exec_())
```
- 插入图片\
利用`label`显示图片
- Signal/Slot\
利用信号与槽机制实现功能触发、传递变量等
- QThread\
利用Qt创建线程
- 显示摄像头画面\
利用线程与信号槽实现实时显示摄像头拍摄的画面
### ROS
- 显示ROS连接状态\
利用`rosgraph`测试当前环境中是否有ROS Master
- 显示订阅消息\
利用Signal/Slot在界面上显示订阅的消息内容