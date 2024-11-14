# faceDetection
中国机器人大赛RoboCup机器人世界杯中国赛-居家项目：【人脸识别+语音播报】功能
如果你觉得有用的话，别忘了点个star喔～
有任何问题都可以提问喔～

## 思路
1.语音播报：使用微软自带的语音播报，直接pip install edge-tts，即可使用
  具体可以查看：https://github.com/bu950223/edge-tts-web-ui
  
2.人脸检测
  使用的是：https://github.com/jianxi-Erin/FaceDetection
  
3.人脸对比
  使用的是第三方接口：讯飞
    https://www.xfyun.cn/doc/face/xffaceComparisonRecg/API.html

## 环境安装
  确保安装了python3、pip、edge-tts等

## 整体结构

<img width="326" alt="image" src="https://github.com/user-attachments/assets/45a0448a-3331-45d5-8308-4f4e5192ce97">



## 修改配置
  1.修改face_cpmpare.py文件的appid、apisecret、apikey
  
  <img width="991" alt="image" src="https://github.com/user-attachments/assets/2d19c5ce-0dc8-4cd9-bdc0-19b69f2c1c6c">

  

  2.修改face_cpmpare_python3_demo.py文件的appid、apisecret、apikey
  
  <img width="948" alt="image" src="https://github.com/user-attachments/assets/1f05885c-382d-42a3-827e-311bed33ffaf">
  


  3.在images/users下面添加志愿者的照片，格式为.jpg

  
  
  4.修改users.json，和images/users下照片命名一致
  
  <img width="926" alt="image" src="https://github.com/user-attachments/assets/73d95d3c-f705-4d77-b97e-1fe0ade458a3">



  5.采用的是外接摄像头形式，直接运行FaceDetection.py即可，第一次运行的时候会有点慢，有语音包的生成。

  ！！！！如果你觉得语音包生成的有点慢的话，可以直接在FaceDetection文件的终端运行：edge-tts --text '检测到志愿者1' --write-media ./person1.mp3 --voice zh-CN-YunxiNeural
  
  如果想手动输入本地相机或者其他，可以释放注释，自行手动选择
  
  <img width="974" alt="image" src="https://github.com/user-attachments/assets/be477617-3249-4de0-84cb-4169eb797169">






  


