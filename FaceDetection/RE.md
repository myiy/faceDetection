# 人脸检测程序

## 简介

这个程序使用 OpenCV 库进行实时人脸检测。支持检测前脸、侧脸、眼睛以及微笑。程序可以从本地图像、本地视频、网络视频或摄像头中读取图像流，并在图像中绘制检测框。适用于大多数常见的人脸识别任务。

## 功能

- **前脸检测**：识别并标记正面人脸。
- **侧脸检测**：识别并标记侧面人脸。
- **眼睛检测**：识别并标记人脸上的眼睛。
- **微笑检测**：识别并标记人脸上的微笑。

## 安装

1. 确保你已安装 Python 3 和 pip。
2. 安装 OpenCV 库：

   ```bash
   pip install opencv-python
   ```

3. 下载并放置 Haar 特征分类器 XML 文件到 `./lib/` 目录下。你可以从 [OpenCV GitHub 仓库](https://github.com/opencv/opencv/tree/master/data/haarcascades) 中获取这些文件。

## 使用

### 运行程序

在终端中运行以下命令来启动程序：

```bash
python FaceDetection.py --mode <模式> --index <索引>
```

其中：
- `--mode`：模式选择。可以是以下值：
  - `c`：相机模式
  - `i`：图片模式（尚未实现）
  - `v`：视频模式
- `--index`：根据模式不同，含义如下：
  - **相机模式 (`c`)**：输入相机索引（例如 `0` 表示默认摄像头）。
  - **视频模式 (`v`)**：输入视频文件 URL 或网络视频流 URL。

### 示例

1. **相机模式**（使用默认摄像头）：

   ```bash
   python FaceDetection.py --mode c --index 0
   ```

2. **视频模式**（使用本地视频文件）：

   ```bash
   python FaceDetection.py --mode v --index path/to/your/video.mp4
   ```

### 退出程序

按 `q` 键可以退出程序并关闭窗口。

## 注意事项

- 确保 Haar 特征分类器 XML 文件正确放置于 `./lib/` 目录。
- 视频或摄像头设备的索引需要根据实际情况调整。

## 贡献

如果你发现了任何问题或有改进建议，请提交问题或拉取请求。

## 许可

这个项目使用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。
