from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame, QSizePolicy, QMenu
from PySide6.QtGui import QPixmap, QImage, QPainter, QBrush, QColor, QPainterPath, QFont, QAction, QIcon
from PySide6.QtCore import Qt, QRectF, QPropertyAnimation, QEasingCurve, QSize, QRect,QObject,QEvent
from testmainwindow import testWindow
import sys
import os
import cv2
import configparser
from datetime import datetime
from video_process_page import video_process_page
def save_to_ini(video_path):
    if not os.path.isabs(video_path):
        video_path = os.path.abspath(video_path)
    video_name = os.path.basename(video_path)

    # Use OpenCV to get video size and length
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get video size
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_size = f"{width}x{height}"

    # Get video length in seconds
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_length = frame_count / fps if fps else 0
    frame_rate = f"{fps:.2f} FPS" if fps else "Unknown FPS"
    cap.release()

    # Get video file size in bytes
    file_size_bytes = os.path.getsize(video_path)
    file_size_mb = file_size_bytes / (1024 * 1024)  # Convert to megabytes

    config = configparser.ConfigParser()
    config.read('file_record.ini')
    section_name = f"{video_name}_{video_path}"
    if not config.has_section(section_name):
        config.add_section(section_name)

    config.set(section_name, 'video_name', video_name)
    config.set(section_name, 'video_path', video_path)
    config.set(section_name, 'video_size', video_size)
    config.set(section_name, 'video_length', f"{video_length:.2f} seconds")
    config.set(section_name, 'frame_rate', frame_rate)
    config.set(section_name, 'file_size', f"{file_size_mb:.2f} MB")
    config.set(section_name, 'last_accessed', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open('file_record.ini', 'w') as configfile:
        config.write(configfile)
def delete_from_ini(video_path):
    if not os.path.isabs(video_path):
        video_path = os.path.abspath(video_path)
    video_name = os.path.basename(video_path)

    config = configparser.ConfigParser()
    config.read('file_record.ini')
    section_name = f"{video_name}_{video_path}"

    if config.has_section(section_name):
        config.remove_section(section_name)
        with open('file_record.ini', 'w') as configfile:
            config.write(configfile)
        print(f"Section '{section_name}' removed from file_record.ini.")
    else:
        print(f"No section found for '{section_name}' in file_record.ini.")
class recent_open_file_widget(QWidget):
    def __init__(self, parent=None, video_path=''):
        super().__init__(parent)
        # 变量初始化，所有的变量都先列在这
        self.video_path = video_path
        self.video_name = os.path.basename(video_path)
        self.pixmap_first_frame_original=self.save_first_frame()
        #self.pixmap_first_frame
        #self.pixmap_first_frame_bigger
        self.checked=False
        # 在此之后设置可视化界面

        self.frame = QFrame(self)
        self.frame.setContentsMargins(0, 0, 0, 0)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.frame.setFrameShape(QFrame.StyledPanel)
        #self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setStyleSheet("background-color: transparent; border-radius: 5px;")
        self.setFixedSize(122, 160)
        #将frame置于中心
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)
        #frame中内容
        #image_label
        self.layout = QVBoxLayout(self.frame)
        self.image_label = QLabel(self.frame)
        self.image_label.setFixedSize(100, 100)
        self.image_label.setStyleSheet("background-color: transparent")
        self.pixmap_first_frame = self.pixmap_first_frame_original.scaled(self.image_label.size()*0.95, Qt.KeepAspectRatio)
        self.pixmap_first_frame_biggger=self.pixmap_first_frame_original.scaled(self.image_label.size(), Qt.KeepAspectRatio)
        self.pixmap_first_frame = self.get_rounded_pixmap(self.pixmap_first_frame, 20)
        self.pixmap_first_frame_biggger = self.get_rounded_pixmap(self.pixmap_first_frame_biggger, 20)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(self.pixmap_first_frame)
        self.layout.addWidget(self.image_label)
        #video_name_label
        self.video_name_label = QLabel(self.frame)
        self.video_name_label.setStyleSheet("background-color: transparent")
        self.font = QFont("Arial", 10)
        self.video_name_label.setFont(self.font)
        self.video_name=self.shorten_name(self.video_name,12)
        self.video_name_label.setText(self.video_name)
        self.video_name_label.setFixedHeight(30)
        self.video_name_label.setAlignment(Qt.AlignCenter)
        self.video_name_label.setWordWrap(True)
        self.layout.addWidget(self.video_name_label)

        #save_to_ini(video_path)
    def save_first_frame(self):  # 保存在了first_video_frame中
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
        ret, frame = cap.read()
        if ret:
            # 裁剪确保为方形
            height, width, _ = frame.shape
            if width != height:
                print("Warning: Image is not square, cropping.")
                min_dim = min(width, height)
                start_x = (width - min_dim) // 2
                start_y = (height - min_dim) // 2
                frame = frame[start_y:start_y + min_dim, start_x:start_x + min_dim]
            #保存第一帧到jpg
            # first_frame_path = os.path.splitext(self.video_name)[0] + "_first_frame.jpg"
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame_rgb.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            if not ret:
                print(f"Error: Could not read frame from video at {self.video_path}")
        cap.release()
        return pixmap

    #使得图片有圆角
    def get_rounded_pixmap(self, pixmap, radius):
        size = pixmap.size()
        rounded_pixmap = QPixmap(size)
        rounded_pixmap.fill(Qt.transparent)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(QRectF(0, 0, size.width(), size.height()), radius, radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded_pixmap
    #缩短名字
    def shorten_name(self, name, max_length=8):
        if len(name) > max_length:
            name, ext = os.path.splitext(self.video_name)
            name = f"{name[:8]}...{ext}"
            return name
        else:
            return name
    def image_scaled_up(self,bigger=False):
        if bigger:
            self.image_label.setPixmap(self.pixmap_first_frame_biggger)
        else:
            self.image_label.setPixmap(self.pixmap_first_frame)
    def delete_self_from_ini(self):
        delete_from_ini(self.video_path)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if(self.checked==False):
                print("checked_FtT")
                self.checked = True
                self.frame.setStyleSheet("background-color: rgba(128, 128, 128, 100); border-radius: 20px;")
            else:
                print("checked_TtF")
                self.checked = False
                self.frame.setStyleSheet("background-color: transparent; border-radius: 5px;")
            event.accept()
        else:
            super().mousePressEvent(event)
    def enterEvent(self, event):
        if self.checked==False:
            self.frame.setStyleSheet("background-color: rgba(128, 128, 128, 50); border-radius: 20px;")
        self.image_scaled_up(True)
        super().enterEvent(event)
    def leaveEvent(self, event):
        if self.checked==False:
            self.frame.setStyleSheet("background-color: transparent; border-radius: 5px;")
        self.image_scaled_up(False)
        super().leaveEvent(event)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.setStyleSheet("""
                    QMenu {
                        background-color: #f0f0f0; 
                        border-radius: 5px; 
                    }
                    QMenu::item {
                        padding: 5px 20px;
                        background-color: transparent; 
                    }
                     QMenu::item:selected {
                        background-color: #a0a0a0; 
                        border-radius: 5px; 
                    }
                    """)


        open_icon = QIcon.fromTheme("document-new")
        open_action = QAction(open_icon, "Open", self)
        open_action.triggered.connect(self.open_video)
        context_menu.addAction(open_action)



        context_menu.exec(event.globalPos())

    def open_video(self):
        top_level_widget = self.window()
        top_level_widget.hide()
        self.video_process_page = video_process_page(parent=self,video_path=self.video_path)
        self.video_process_page.show()
        save_to_ini(self.video_path)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Hide the top-level parent widget
            self.open_video()

            event.accept()
        else:
            super().mouseDoubleClickEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = recent_open_file_widget(parent=None, video_path='C:/Users/lenovo/Desktop/2.mp4')
    window.show()
    sys.exit(app.exec_())