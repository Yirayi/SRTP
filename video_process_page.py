# This P-ython file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QApplication, QWidget,QVBoxLayout,QPushButton,QGridLayout

# Important:
# You need to run the following command to generate the ui_form.py file
#pyside6-uic video_process_page.ui -o ui_video_process_page.py

#     pyside2-uic form.ui -o ui_form.py
from PySide6.QtGui import QCursor,QPainter, QPen,QFont,QMouseEvent,QFontDatabase
from PySide6.QtCore import Qt,QRect,QPoint,QSize,QPropertyAnimation, QEasingCurve,QTimer,QByteArray,QUrl
from ui_video_process_page import Ui_video_process_page
from PySide6.QtGui import QIcon,QPixmap
import configparser
import os
from Unet.video_segment import VideoSegmentWorker
from cor.drift_correction import DriftCorrectionWorker
from cor.drift_correction import img2video
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget

class video_process_page(QMainWindow):
    def __init__(self, parent=None,video_path=None):
        super().__init__(parent)
        self.ui = Ui_video_process_page()
        self.ui.setupUi(self)
        self.video_path=video_path
        # 添加隐藏边框的代码
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 保留原有标志 + 隐藏边框
        #实现最小化、全屏和关闭功能
        self.ui.min_botton.clicked.connect(self.showMinimized)
        self.ui.max_botton.clicked.connect(self.toggle_maximized)
        self.ui.close_botton.clicked.connect(self.close)
        #其余ui部件连接槽函数
        self.ui.return_botton.clicked.connect(self.return_to_welcome_page)
        self.ui.start_btn.clicked.connect(self.startPressEvent)
        self.ui.restart_btn.clicked.connect(self.restartPressEvent)
        #ui动画相关
        self.progress_animation = QPropertyAnimation(self.ui.process_bar, QByteArray(b"value"))
        self.progress_animation.setDuration(1000)  # 动画持续时间设置为1000毫秒
        self.progress_animation.setEndValue(0)
        self.progress_animation.setEasingCurve(QEasingCurve.OutQuad)
        #ui中的视频信息
        if self.video_path:
            self.load_video_info()
        # 初始化拖动的起始点
        self.drag_position = QPoint(0, 0)
        self.drag_pos = None
        #视频处理相关
        self.video_path = video_path
        self.isrunning=False
        self.ui.process_bar.setValue(0)

        self.segment_worker = VideoSegmentWorker(self.video_path)
        self.segment_worker.progress.connect(lambda value: self.ui.process_bar.setValue(value))
        self.segment_worker.finished.connect(self.seg_finished_event)
        self.basename, _ = os.path.splitext(os.path.basename(self.video_path))
        self.DriftCorrectionWorker=DriftCorrectionWorker(video_name=self.basename,standard_frame=0)
        self.DriftCorrectionWorker.progress.connect(lambda value: self.ui.process_bar.setValue(value))
        self.DriftCorrectionWorker.finished.connect(self.drift_finished_event)
        #添加视频
        self.video_widget = QVideoWidget(self)
        self.video_layout = QGridLayout(self.ui.video_widget)
        self.video_layout.addWidget(self.video_widget, 0, 0)
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

    def seg_finished_event(self):
        print("seg_Finished processing")
        self.DriftCorrectionWorker.start()
    def drift_finished_event(self):
        print("drift_Finished processing")
        img2video(self.video_path,self.basename)
        QTimer.singleShot(1000, self.play_video)
        #下面的为应付代码，记得删掉
        icon_start = QIcon()
        icon_start.addFile(u"icon/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.start_btn.setIcon(icon_start)
        self.isrunning = False
    def play_video(self):
        self.video_file_path = f"G:\\Cute\\QtProject\\master_srtp\\data\\result\\{self.basename}\\{self.basename}_origin.mp4"
        print(self.video_file_path)
        self.media_player.setSource(QUrl.fromLocalFile(self.video_file_path))
        self.media_player.play()
    def load_video_info(self):
        config = configparser.ConfigParser()
        config.read('file_record.ini')
        video_name = os.path.basename(self.video_path)
        section_name = f"{video_name}_{self.video_path}"

        if config.has_section(section_name):
            video_path = config.get(section_name, 'video_path', fallback='Unknown')
            video_size = config.get(section_name, 'video_size', fallback='Unknown')
            video_length = config.get(section_name, 'video_length', fallback='Unknown')
            frame_rate = config.get(section_name, 'frame_rate', fallback='Unknown')
            file_size = config.get(section_name, 'file_size', fallback='Unknown')

            # Assuming you have QLabel widgets in your UI to display this information
            self.ui.label_video_path.setText(f"路径: {video_path}")
            self.ui.label_video_size.setText(f"分辨率: {video_size}")
            self.ui.label_video_length.setText(f"视频长度: {video_length}")
            self.ui.label_video_frame_rate.setText(f"帧速率: {frame_rate}")
            self.ui.label_video_dile_size.setText(f"文件大小: {file_size}")
        else:
            print(f"No information found for video: {self.video_path}")

    #全屏和取消全屏的函数
    def toggle_maximized(self):
        # 判断窗口是否已经最大化
        if self.isMaximized():
            self.showNormal()  # 恢复到原来的状态
            icon_min = QIcon()
            icon_min.addFile(u"icon/max.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.max_botton.setIcon(icon_min)
        else:
            self.showMaximized()  # 最大化窗口
            icon_min = QIcon()
            icon_min.addFile(u"icon/min.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.max_botton.setIcon(icon_min)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()
            event.accept()
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = None
            event.accept()
    def return_to_welcome_page(self):
        if(self.parent()):
            self.parent().topLevelWidget().show()
            self.close()
        else:
            print("parent is None")
    def startPressEvent(self):
        if not self.isrunning:
            print("切换至running")
            icon_start = QIcon()
            icon_start.addFile(u"icon/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.start_btn.setIcon(icon_start)
            self.isrunning=True
            self.segment_worker.start()
        elif self.isrunning:
            icon_start = QIcon()
            icon_start.addFile(u"icon/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.start_btn.setIcon(icon_start)
            self.isrunning = False
            self.segment_worker.pause()
            print("切换至stop")

    def restartPressEvent(self):
        print("restart pressed")
        self.rotation_angle = 0
        rotation_timer = QTimer(self)
        def rotate_icon():
            # Load the original icon
            original_icon = QIcon(u"icon/restart.png")
            pixmap = original_icon.pixmap(20, 20)  # Adjust size as needed

            # Create a new pixmap to rotate
            rotated_pixmap = QPixmap(pixmap.size())
            rotated_pixmap.fill(Qt.transparent)  # Fill with transparent color

            # Create a painter to rotate the pixmap
            painter = QPainter(rotated_pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            # Rotate the pixmap
            painter.translate(rotated_pixmap.width() / 2, rotated_pixmap.height() / 2)
            painter.rotate(self.rotation_angle)  # Rotate by the current angle
            painter.translate(-rotated_pixmap.width() / 2, -rotated_pixmap.height() / 2)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            # Set the rotated pixmap as the button's icon
            self.ui.restart_btn.setIcon(QIcon(rotated_pixmap))

            # Increment the rotation angle
            self.rotation_angle += 5  # Adjust the increment for desired speed
            if self.rotation_angle >= 360:
                rotation_timer.stop()  # Stop the timer after a full rotation
                rotation_timer.deleteLater()  # Delete the timer

        # Connect the timer to the rotate_icon function
        rotation_timer.timeout.connect(rotate_icon)
        rotation_timer.start(16)
        #实现进度条归零
        current_value = self.ui.process_bar.value()
        print("currentvalue:", current_value)
        self.progress_animation.setEndValue(0)
        self.progress_animation.start()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = video_process_page(video_path="C:\\Users\\lenovo\\Desktop\\goodone.mp4")
    widget.play_video()
    widget.show()
    sys.exit(app.exec())   #   pyside6-uic form.ui -o ui_form.py
