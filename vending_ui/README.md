# Vending Machine UI
智能传感器与执行器实验室实训台UI界面。 
## 用户接口
### 人脸识别
对比预设已知用户，实时侦测识别人脸。可通过UI直接注册新用户。可通过UI登录或注销用户状态。
#### 已知用户存储位置
已知用户照片存储在`/data/known_faces`文件夹下， 每个用户以用户名为文件夹，文件夹内存放用户照片\
![known_faces](./doc/img/directory_tree.png)
### ROS 接口
通过ROS接受实训台内传感器状态数据，发送控制指令
#### 发布的话题
#### 订阅的话题
- `drink_temp(std_msgs/Float32)`\
实训台内部温度，单位为摄氏度。 
- `drink_stats(std_msgs/String)`\
饮料库位状态，`1`为库位存在饮料，`0`为库位不存在饮料。字符串长度为6，分别对应6个饮料储存库位。
- `drink_ready(std_msgs/String)`\
饮料等待提取状态， `1`为可以提取，`0`为无饮料可供提取。