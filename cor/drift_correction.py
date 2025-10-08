import cv2
import numpy as np
import time
import os
import glob
from PySide6.QtCore import QThread, Signal
import threading
sigmaG = 4.0
EPSILON = 0.01

inputPath = "2.mp4"
outputPath = "after.mp4"
x_pixel = 0.0  # x方向的像素偏移
y_pixel = 0.0  # y方向的像素偏移
MAX_CORNERS = 30  # 角点的个数
x = 0.0
y = 0.0

def subpixel_translate(src, dx, dy):
    """
    src: input array
    dx: distance in x direction
    dy: distance in y direction
    """

    rows, cols = src.shape
    dst = np.zeros_like(src)

    for i in range(rows):
        y = int(i - dy)
        u = (i - dy) - y
        if 0 <= y < rows - 1:
            srcdata = src[y]
            srcdata1 = src[y + 1]
            for j in range(cols - 1):
                x = int(j - dx)
                v = (j - dx) - x
                if 0 <= x < cols - 1:
                    dst[i, j] = (1 - u) * (1 - v) * srcdata[x] + (1 - u) * v * srcdata[x + 1] + u * (1 - v) * srcdata1[x] + u * v * srcdata1[x + 1]
    return dst

def im_move(src_image, x, y):
    m = np.zeros_like(src_image)
    if x >= 0 and y >= 0:
        temp = src_image[0:src_image.shape[0] - y, 0:src_image.shape[1] - x]
        m[y:y + temp.shape[0], x:x + temp.shape[1]] = temp
    elif x <= 0 and y >= 0:
        temp = src_image[0:src_image.shape[0] - y, -x:src_image.shape[1]]
        m[y:y + temp.shape[0], 0:temp.shape[1]] = temp
    elif x >= 0 and y <= 0:
        temp = src_image[-y:src_image.shape[0], 0:src_image.shape[1] - x]
        m[0:temp.shape[0], x:x + temp.shape[1]] = temp
    elif x <= 0 and y <= 0:
        temp = src_image[-y:src_image.shape[0], -x:src_image.shape[1]]
        m[0:temp.shape[0], 0:temp.shape[1]] = temp
    return m

def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    cv2.circle(img, center, 512 // 8, (96, 96, 96), thickness, line_type)

def video2image(s1, s2):
    capture = cv2.VideoCapture(s1)
    if not capture.isOpened():
        print("open failed!!!")
        return

    total_frame_number = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    rate = capture.get(cv2.CAP_PROP_FPS)
    frame_to_start = 1
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_to_start)
    frame_to_stop = total_frame_number
    stop = False
    current_frame = frame_to_start

    while not stop:
        ret, frame = capture.read()
        if not ret:
            print("读取视频失败")
            return
        print(f"正在写第{current_frame}帧")
        cv2.imwrite(f"{s2}{current_frame}.png", frame)
        if current_frame > frame_to_stop:
            stop = True
        current_frame += 1

def img2video(form_video,source_video_name,target_dir=None):
    cap = cv2.VideoCapture(form_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    source_dir=os.path.join(f'G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{source_video_name}\\drift_corrected')
    if target_dir==None:
        target_dir=f'G:\\Cute\\QtProject\\master_srtp\\data\\result\\{source_video_name}'
    output_video_path = os.path.join(target_dir, f'{source_video_name}_drifted.mp4')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    tests_path = glob.glob(os.path.join(source_dir, '*.tif'))
    tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    print(os.path.join(source_dir, '*.png'))
    for test_path in tests_path:
        img = cv2.imread(test_path)
        out.write(img)
    out.release()

def dir2video(form_video,source_frames_path,targer_form="png"):
    cap = cv2.VideoCapture(form_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_video_path = os.path.join(source_frames_path, 'assembled.mp4')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    tests_path = glob.glob(os.path.join(source_frames_path, f'*.{targer_form}'))
    tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[0]))
    for test_path in tests_path:
        img = cv2.imread(test_path)
        out.write(img)
    out.release()

class DriftCorrectionWorker(QThread):
    progress = Signal(int)  # Signal to emit progress
    finished = Signal()     # Signal to emit when finished

    def __init__(self,video_name,standard_frame=0,start_frame=0,end_frame=0):
        super().__init__()
        self.video_name=video_name
        self.standard_frame=standard_frame
        self.start_frame=start_frame
        self.end_frame=end_frame
        self._pause_event = threading.Event()
        self._pause_event.set()  # Initially not paused
        self._is_running = True
        self.progress_record = 40
        self.percent_drift = 60

    def run(self):
        target_dir = f"G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{self.video_name}\\segmented"
        tests_path = glob.glob(os.path.join(target_dir, '*.png'))
        tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

        save_dir = f"G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{self.video_name}\\drift_corrected"
        os.makedirs(save_dir, exist_ok=True)
        self.start_image = cv2.imread(tests_path[self.standard_frame], cv2.IMREAD_GRAYSCALE)
        win_size = 10
        detector = cv2.SIFT_create()
        keypoints = detector.detect(self.start_image, None)
        featureA = np.array([kp.pt for kp in keypoints], dtype=np.float32)
        featureB = np.zeros_like(featureA)
        features_found = np.zeros(len(featureA), dtype=np.uint8)

        global x_pixel, y_pixel, x, y
        if (self.end_frame == 0):
            end_frame = len(tests_path)

        drift_count=0
        for i in range(self.start_frame, end_frame - 1):
            if (self._is_running):
                self._pause_event.wait()
            image_name = tests_path[i]
            src = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
            if src is None:
                print("END！！")
                break

            featureB, features_found, _ = cv2.calcOpticalFlowPyrLK(self.start_image, src, featureA, None,winSize=(win_size * 2 + 1, win_size * 2 + 1),maxLevel=5, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.3))

            total = 0
            for j in range(len(featureA)):
                if not features_found[j]:
                    continue
                x_pixel += featureA[j][0] - featureB[j][0]
                y_pixel += featureA[j][1] - featureB[j][1]
                total += 1

            if total > 0:
                y += y_pixel / total
                x += x_pixel / total

            dst = subpixel_translate(src, x, y)
            result_name = os.path.join(save_dir, f"{i}.tif")
            cv2.imwrite(result_name, dst)
            self.start_image = src
            featureA = featureB
            x_pixel = 0
            y_pixel = 0
            drift_count+=1
            self.progress.emit(self.progress_record + drift_count / len(tests_path) * self.percent_drift)
        self.finished.emit()  # Emit finished signal
    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()

    def stop(self):
        self._is_running = False
        self.resume()
def drift_cor(video_name,standard_frame,start_frame=0,end_frame=0):
    target_dir = f"G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{video_name}\\segmented"
    tests_path = glob.glob(os.path.join(target_dir, '*.png'))
    tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

    save_dir = f"G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{video_name}\\drift_corrected"
    os.makedirs(save_dir, exist_ok=True)
    drift_view_dir = f"G:\\Cute\\QtProject\\master_srtp\\data\\processing\\{video_name}\\drift_view"
    os.makedirs(drift_view_dir, exist_ok=True)

    time0 = time.time()
    start_image = cv2.imread(tests_path[standard_frame], cv2.IMREAD_GRAYSCALE)
    win_size = 10
    detector = cv2.SIFT_create()
    keypoints = detector.detect(start_image, None)
    featureA = np.array([kp.pt for kp in keypoints], dtype=np.float32)
    featureB = np.zeros_like(featureA)
    features_found = np.zeros(len(featureA), dtype=np.uint8)

    feature_paths = [[] for _ in range(len(featureA))]

    global x_pixel, y_pixel, x, y
    if(end_frame == 0):
        end_frame = len(tests_path)

    print(f'from{start_frame} to {end_frame-1} frame, drift correction...')

    for i in range(start_frame, end_frame-1):
        image_name = tests_path[i]
        src = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
        if src is None:
            print("END！！")
            break

        featureB, features_found, _ = cv2.calcOpticalFlowPyrLK(start_image, src, featureA, None,
                                                               winSize=(win_size * 2 + 1, win_size * 2 + 1), maxLevel=5,
                                                               criteria=(
                                                               cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20,
                                                               0.3))

        total = 0
        for j in range(len(featureA)):
            if not features_found[j]:
                continue
            x_pixel += featureA[j][0] - featureB[j][0]
            y_pixel += featureA[j][1] - featureB[j][1]
            total += 1
            feature_paths[j].append((int(featureB[j][0]), int(featureB[j][1])))

        if total > 0:
            y += y_pixel / total
            x += x_pixel / total

        dst = subpixel_translate(src, x, y)
        result_name = os.path.join(save_dir, f"{i}.tif")
        cv2.imwrite(result_name, dst)

        color_image = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
        for j in range(len(featureA)):
            if features_found[j]:
                # Draw the path of each feature
                for k in range(1, len(feature_paths[j])):
                    cv2.line(color_image, feature_paths[j][k - 1], feature_paths[j][k], (255, 0, 0), 1)

        drift_view_name = os.path.join(drift_view_dir, f"{i}.png")
        cv2.imwrite(drift_view_name, color_image)

        start_image = src
        featureA = featureB
        x_pixel = 0
        y_pixel = 0

    time0 = time.time() - time0
    print(f"Program running time is : {time0} second")
    cv2.waitKey(0)



if __name__ == "__main__":
    #drift_cor(video_name="1",standard_frame=0)
    #dir2video("C:\\Users\\lenovo\\Desktop\\test_video1.mp4","D:\\srtp\\img_segAndcorr-master\\data4correction\\data\\test2_after")
    #drift_cor(video_name="test_video1", standard_frame=0)
    dir2video("C:\\Users\\lenovo\\Desktop\\test_video1.mp4",source_frames_path="G:\\Cute\\QtProject\\master_srtp\\data\\processing\\test_video1\\drift_view")