import cv2
import numpy as np
import time
import os
import glob
from PySide6.QtCore import QThread, Signal
import threading

def img2video(form_video,source_dir):
    cap = cv2.VideoCapture(form_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    output_video_path=f'D:\\srtp\\img_segAndcorr-master\\after.mp4'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    tests_path = glob.glob(os.path.join(source_dir, '*.png'))
    tests_path.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    print(os.path.join(source_dir, '*.png'))
    for test_path in tests_path:
        img = cv2.imread(test_path)
        out.write(img)
    out.release()


if __name__ == "__main__":
    img2video("1.mp4",'D:\\srtp\\img_segAndcorr-master\\data4correction\\data\\test2')