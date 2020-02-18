# Vending Machine UI
智能传感器与执行器实验室实训台UI界面。 
## 用户接口
### 人脸识别

### ROS 接口
#### 发布的话题
#### 订阅的话题
- `drink_temp(std_msgs/Float32)`\
实训台内部温度，单位为摄氏度。 
- `drink_stats(std_msgs/String)`\
饮料库位状态，`1`为库位存在饮料，`0`为库位不存在饮料。字符串长度为6，分别对应6个饮料储存库位。
- `drink_ready(std_msgs/String)`\
饮料等待提取状态， `1`为可以提取，`0`为无饮料可供提取。