from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
import sys


class testWindow(QMainWindow):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("Test Window")

        # Create QLabel and set alignment
        self.video_label = QLabel(video_path)
        self.video_label.setAlignment(Qt.AlignCenter)

        # Set QLabel as the central widget
        self.setCentralWidget(self.video_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = testWindow(video_path='C:/Users/lenovo/Desktop/2.mp4')
    window.show()
    sys.exit(app.exec())