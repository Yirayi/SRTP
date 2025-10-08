import cv2
import numpy as np
import os
import time

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
        m[y:, x:] = temp
    elif x <= 0 and y >= 0:
        temp = src_image[0:src_image.shape[0] - y, -x:]
        m[y:, :temp.shape[1]] = temp
    elif x >= 0 and y <= 0:
        temp = src_image[-y:, 0:src_image.shape[1] - x]
        m[:temp.shape[0], x:] = temp
    elif x <= 0 and y <= 0:
        temp = src_image[-y:, -x:]
        m[:temp.shape[0], :temp.shape[1]] = temp
    return m

def my_filled_circle(img, center):
    cv2.circle(img, center, 512 // 8, (96, 96, 96), -1, lineType=8)

def video_to_image(video_path, save_path):
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print("Failed to open video!")
        return

    total_frame_number = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    rate = capture.get(cv2.CAP_PROP_FPS)
    frame_to_start = 1
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_to_start)
    frame_to_stop = total_frame_number
    current_frame = frame_to_start

    while current_frame <= frame_to_stop:
        ret, frame = capture.read()
        if not ret:
            print("Failed to read video frame")
            break
        print(f"Writing frame {current_frame}")
        cv2.imwrite(os.path.join(save_path, f"{current_frame}.png"), frame)
        current_frame += 1
def cor_video(standard_image_path,start_frame, end_frame,save_as_video=True):
    start_time = time.time()
    start_image = cv2.imread(standard_image_path, cv2.IMREAD_GRAYSCALE)

def main():
    start_time = time.time()
    start_image = cv2.imread("data4correction\\data\\test2_after\\1_pre.png", cv2.IMREAD_GRAYSCALE)
    background_image = cv2.imread("data4correction\\data\\test2_after\\1_pre.png")
    win_size = 10
    detector = cv2.ORB_create()
    keypoints = detector.detect(start_image, None)
    feature_a = np.array([kp.pt for kp in keypoints], dtype=np.float32)
    feature_b = np.empty_like(feature_a)
    features_found = np.empty((len(feature_a),), dtype=np.uint8)

    for pt in feature_a:
        cv2.circle(background_image, (int(pt[0]), int(pt[1])), 5, (0, 255, 0), 2)

    cv2.imshow("result", background_image)
    cv2.imwrite("data4correction\\data\\cornerdetect2.png", background_image)

    for i in range(2, 258):
        image_name = f"data4correction\\data\\test2_afte" \
                     f"r\\{i}_pre.png"
        src = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
        if src is None:
            print("END!!")
            break

        src_image = cv2.imread(image_name)
        feature_b, features_found, _ = cv2.calcOpticalFlowPyrLK(start_image, src, feature_a, None, winSize=(win_size * 2 + 1, win_size * 2 + 1), maxLevel=5, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.3))

        total = np.sum(features_found)
        if total > 0:
            x_pixel = np.sum((feature_a[:, 0] - feature_b[:, 0]) * features_found) / total
            y_pixel = np.sum((feature_a[:, 1] - feature_b[:, 1]) * features_found) / total
        else:
            x_pixel = 0
            y_pixel = 0

        dst = subpixel_translate(src, x_pixel, y_pixel)
        result_name = f"data4correction\\data\\test2_cor\\drift({i}).tif"
        cv2.imwrite(result_name, dst)
        start_image = src
        feature_a = feature_b

    elapsed_time = time.time() - start_time
    print(f"Program running time is: {elapsed_time} seconds")
    cv2.imshow("result", background_image)
    cv2.imwrite("data4correction\\data\\orb_detect.png", background_image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()