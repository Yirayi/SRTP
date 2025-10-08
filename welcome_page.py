# This P-ython file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QApplication, QWidget,QVBoxLayout,QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#pyside6-uic welcome_page.ui -o ui_welcome_page.py
from PySide6.QtGui import QCursor,QPainter, QPen,QFont,QMouseEvent,QFontDatabase
from PySide6.QtCore import Qt,QRect,QPoint  # 新增导入 Qt
from ui_welcome_page import Ui_welcome_page
from file_container import file_container
class welcome_page(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_welcome_page()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 保留原有标志 + 隐藏边框
        # 实现最小化、全屏和关闭功能
        self.ui.min_botton.clicked.connect(self.showMinimized)
        self.ui.max_botton.clicked.connect(self.toggle_maximized)
        self.ui.close_botton.clicked.connect(self.close)
        # 初始化拖动的起始点
        self.drag_position = QPoint(0, 0)
        self.drag_pos = None
        #文件相关实现
        self.file_container=file_container(self)
        self.file_layout = QVBoxLayout(self.ui.file_frame)
        self.file_layout.setContentsMargins(0, 0, 0, 0)
        self.file_layout.setSpacing(0)
        self.file_layout.addWidget(self.file_container)
        #ui
        self.ui.open_new_btn.clicked.connect(self.OpenNewPressEvent)
        self.new_video_to_open="None"
        self.font_id = QFontDatabase.addApplicationFont("font/font.otf")
        self.font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.font = QFont(self.font_family)
        QApplication.setFont(self.font)
        self.ui.open_new_btn.setStyleSheet("""
                   QPushButton {
                       /* Normal state */
                       padding: 2px;
                   }
                   QPushButton:hover {
                       /* Hover state */
                       padding-bottom: 5px; /* Move icon slightly upwards */
                   }
               """)
    def OpenNewPressEvent(self):
        self.new_video_to_open = self.file_container.add_new_widget_to_ini()
        for widget in self.file_container.widgets:
            if widget.video_path == self.new_video_to_open:
                widget.open_video()
                break

    def toggle_maximized(self):
        # 判断窗口是否已经最大化
        if self.isMaximized():
            self.showNormal()  # 恢复到原来的状态
        else:
            self.showMaximized()  # 最大化窗口

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

if __name__ == "__main__":
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = welcome_page()
        widget.show()
        sys.exit(app.exec())
