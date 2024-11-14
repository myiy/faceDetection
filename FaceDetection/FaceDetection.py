import time

import cv2 as cv

from face_compare import face_compare

# 加载人脸识别分类器
# haarcascade_frontalface_default最简单,精度低
# haarcascade_frontalface_alt2精度稍好,速度快
face_cas = cv.CascadeClassifier('./lib/haarcascade_frontalface_alt2.xml')

# 侧脸检测haarcascade_profileface
side_face_cas = cv.CascadeClassifier('./lib/haarcascade_profileface.xml')


def draw_box(frame, title, x1, y1, x2, y2):
    '''
    绘制识别框
    frame:为绘制对象
    title:为识别框上标题
    x1,y1,x2,y2:绘制坐标
    '''
    cv.putText(frame, title, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    face_box = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return face_box


def videoFace(url):
    '''
    视频人脸识别
    url: 视频地址，可以是本地路径，也可以是网络路径
    url: 0表示本地摄像头索引
    '''
    #
    # 1. 按url读取摄像头/本地/网络视频
    video = cv.VideoCapture(url)

    # 2. 在每帧数据中进行人脸识别
    while(video.isOpened()):
        # 获取视频状态和视频帧图像
        video_status, img_frame = video.read()

        if video_status == True:
            # 转换为灰度图像
            img_gray = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

            # 3. 实例化OpenCV人脸识别的分类器
            
            # 4. 调用模型识别前人脸
            faceRects = face_cas.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faceRects:
                x2 = x+w
                y2 = y+h
                # 计算置信度（可以根据实际情况修改）
                confidence = round(w * h / (img_frame.shape[0] * img_frame.shape[1]), 2)  # 这里假设为检测框的面积比例
                if confidence > 0.05:
                    path = './images/slice/face-{}.jpg'.format(str(timcv2库怎么安装e.time()))
                    cv.imwrite(path, img_frame)
                    is_true = face_compare(path)
                    if is_true:
                        return

                text = f'Front Face:{confidence*100:.2f}%'

                draw_box(img_frame, text, x, y, x2, y2)
            side_face = side_face_cas.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            #
            for (x, y, w, h) in side_face:
                x2 = x+w
                y2 = y+h
                # 计算置信度（可以根据实际情况修改）
                confidence = round(w * h / (img_frame.shape[0] * img_frame.shape[1]), 2)  # 这里假设为检测框的面积比例
                text = f'Side Face:{confidence*100:.2f}%'
                #绘制识别框
                if confidence > 0.05:
                    path = './images/slice/face-{}.jpg'.format(str(time.time()))
                    cv.imwrite(path,img_frame)
                    is_true = face_compare(path)
                    if is_true:
                        return
                draw_box(img_frame, text, x, y, x2, y2)
            cv.imshow("Real-time Detection", img_frame)
            
            # 按 'q' 键退出
            if cv.waitKey(1) & 0xFF == ord('q'):
                breakodeF
    cv.destroyAllWindows()


if __name__ == "__main__":
    #print("欢迎使用人脸检测程!按Ctrl+C退出程序!")
    #operation = input("请输入操作：\n- 本地相机人脸识别(无窗口),请输入序号0\n- 视频人脸识别（有窗口）,请输入视频url\n")
    #print("按q键关闭窗口")
    videoFace(2)
