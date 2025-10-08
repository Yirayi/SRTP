import glob
import numpy as np
import torch
import cv2
from Unet.model import UNet
from collections import deque
import os
import threading
from PySide6.QtCore import QThread, Signal
torch.cuda.empty_cache()
def video_segment(video_path, save_as_video=True):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if device.type == 'cuda':
        print("Using GPU for processing.")
    else:
        print("Using CPU for processing.")
    net = UNet(n_channels=1, n_classes=1)
    net.to(device=device)
    net.load_state_dict(torch.load('G:\\Cute\\QtProject\\master_srtp\\Unet\\best_model_174.pth', map_location=device))

    net.eval()

    # 读取视频
    cap = cv2.VideoCapture(video_path)
    # 创建videoWriter
    base_name, ext = os.path.splitext(os.path.basename(video_path))
    # 处理过程的图片保存的文件夹
    frame_save_dir = os.path.join('G:\\Cute\\QtProject\\master_srtp\\data\\processing', base_name)
    origin_frames_dir = os.path.join(frame_save_dir, 'origin')
    segmented_frames_dir = os.path.join(frame_save_dir, 'segmented')
    os.makedirs(frame_save_dir, exist_ok=True)
    os.makedirs(origin_frames_dir, exist_ok=True)
    os.makedirs(segmented_frames_dir, exist_ok=True)

    if(save_as_video):
        video_save_dir = os.path.join('G:\\Cute\\QtProject\\master_srtp\\data\\result', base_name)

        os.makedirs(video_save_dir, exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_name = f"{base_name}_segmented{ext}"
        output_video_path = os.path.join(video_save_dir, video_name)
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # 开始处理
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(origin_frames_dir, f"{frame_count}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    tests_path = glob.glob(os.path.join(origin_frames_dir, '*.png'))
    tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    for test_path in tests_path:
        # 保存结果地址
        frame_number = os.path.splitext(os.path.basename(test_path))[0]
        # 保存结果地址
        segmented_frame = os.path.join(segmented_frames_dir, f"{frame_number}.png")
        print(f"Processing {test_path} to{segmented_frame}...")
        # 读取图片
        img = cv2.imread(test_path)
        # 转为灰度图
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 转为batch为1，通道为1，大小为512*512的数组
        img = img.reshape(1, 1, img.shape[0], img.shape[1])
        # 转为tensor
        img_tensor = torch.from_numpy(img)
        # 将tensor拷贝到device中，只用cpu就是拷贝到cpu中，用cuda就是拷贝到cuda中。
        img_tensor = img_tensor.to(device=device, dtype=torch.float32)
        # 预测
        pred = net(img_tensor)
        # 提取结果
        pred = np.array(pred.data.cpu()[0])[0]
        # print(pred)
        # 处理结果
        pred[pred >= 0.5] = 255
        pred[pred < 0.5] = 0

        #pred= remove_noise(pred)

        cv2.imwrite(segmented_frame, pred)
        if save_as_video and out is not None:
            bgr_frame = cv2.cvtColor(pred.astype(np.uint8), cv2.COLOR_GRAY2BGR)
            out.write(bgr_frame)
    cap.release()
    if save_as_video and out is not None:
        out.release()
#progress_bar相关

class VideoSegmentWorker(QThread):
    progress = Signal(int)  # Signal to emit progress
    finished = Signal()     # Signal to emit when finished

    def __init__(self, video_path, save_as_video=True):
        super().__init__()
        self.video_path = video_path
        self.save_as_video = save_as_video
        self._pause_event = threading.Event()
        self._pause_event.set()  # Initially not paused
        self._is_running = True
        self.progress_record = 0
        self.percent_save_org = 10
        self.percent_seg = 30

    def run(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        net = UNet(n_channels=1, n_classes=1)
        net.to(device=device)
        net.load_state_dict(torch.load('G:\\Cute\\QtProject\\master_srtp\\Unet\\202403.pth', map_location=device))
        net.eval()

        cap = cv2.VideoCapture(self.video_path)
        base_name, ext = os.path.splitext(os.path.basename(self.video_path))
        frame_save_dir = os.path.join('G:\\Cute\\QtProject\\master_srtp\\data\\processing', base_name)
        origin_frames_dir = os.path.join(frame_save_dir, 'origin')
        segmented_frames_dir = os.path.join(frame_save_dir, 'segmented')
        os.makedirs(frame_save_dir, exist_ok=True)
        os.makedirs(origin_frames_dir, exist_ok=True)
        os.makedirs(segmented_frames_dir, exist_ok=True)

        if self.save_as_video:
            video_save_dir = os.path.join('G:\\Cute\\QtProject\\master_srtp\\data\\result', base_name)
            os.makedirs(video_save_dir, exist_ok=True)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            video_name = f"{base_name}_segmented{ext}"
            output_video_path = os.path.join(video_save_dir, video_name)
            out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count = 0
        while cap.isOpened() and self._is_running:
            self._pause_event.wait()  # Wait if paused
            ret, frame = cap.read()
            if not ret:
                break
            frame_filename = os.path.join(origin_frames_dir, f"{frame_count}.png")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1
            self.progress.emit(self.progress_record+frame_count/ total_frames * self.percent_save_org)
        self.progress_record+=self.percent_save_org
        frame_segment_count=0
        tests_path = glob.glob(os.path.join(origin_frames_dir, '*.png'))
        tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
        for test_path in tests_path:
            if(self._is_running):
                self._pause_event.wait()
            # 保存结果地址
            frame_number = os.path.splitext(os.path.basename(test_path))[0]
            # 保存结果地址
            segmented_frame = os.path.join(segmented_frames_dir, f"{frame_number}.png")
            print(f"Processing {test_path} to{segmented_frame}...")
            # 读取图片
            img = cv2.imread(test_path)
            # 转为灰度图
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # 转为batch为1，通道为1，大小为512*512的数组
            img = img.reshape(1, 1, img.shape[0], img.shape[1])
            # 转为tensor
            img_tensor = torch.from_numpy(img)
            # 将tensor拷贝到device中，只用cpu就是拷贝到cpu中，用cuda就是拷贝到cuda中。
            img_tensor = img_tensor.to(device=device, dtype=torch.float32)
            # 预测
            pred = net(img_tensor)
            # 提取结果
            pred = np.array(pred.data.cpu()[0])[0]
            # print(pred)
            # 处理结果
            pred[pred >= 0.5] = 255
            pred[pred < 0.5] = 0



            cv2.imwrite(segmented_frame, pred)
            if self.save_as_video and out is not None:
                bgr_frame = cv2.cvtColor(pred.astype(np.uint8), cv2.COLOR_GRAY2BGR)
                out.write(bgr_frame)
            frame_segment_count+=1
            self.progress.emit(self.progress_record+frame_segment_count/len(tests_path)*self.percent_seg)
        self.progress_record+=self.percent_seg
        cap.release()
        if self.save_as_video and out is not None:
            out.release()

        self.finished.emit()  # Emit finished signal

    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()

    def stop(self):
        self._is_running = False
        self.resume()
def preserve_large_black_regions(frames, current_index, window_size=2, threshold=0.95):
    current_frame = frames[current_index]
    total_frames = len(frames)
    # Calculate the average frame from the neighboring frames
    start_index = max(0, current_index - window_size)
    end_index = min(total_frames, current_index + window_size + 1)

    # Exclude the current frame from the average calculation
    neighboring_frames = [frames[i] for i in range(start_index, end_index) if i != current_index]
    average_frame = np.mean(neighboring_frames, axis=0)

    # Calculate the difference between the current frame and the average frame
    difference = np.abs(current_frame - average_frame)

    # Identify large inconsistent white regions
    inconsistent_regions = difference > (threshold * 255)

    # Remove inconsistent white regions by setting them to black
    current_frame[inconsistent_regions] = 0

    return current_frame

def remove_noise(processing,kernel_close_size=30):
    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    processing = cv2.morphologyEx(processing, cv2.MORPH_OPEN, kernel_open)
    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_close_size, kernel_close_size))
    processing = cv2.morphologyEx(processing, cv2.MORPH_CLOSE, kernel_close)

    return processing
def smooth(processing):
    processing = cv2.bilateralFilter(processing, d=9, sigmaColor=75, sigmaSpace=75)
    gaussian_blur = cv2.GaussianBlur(processing, (9, 9), 10.0)
    processing = cv2.addWeighted(processing, 1.5, gaussian_blur, -0.5, 0)
    return processing


if __name__ == '__main__':
    video_segment('1.mp4')