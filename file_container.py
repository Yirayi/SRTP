from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QApplication, QFileDialog
from PySide6.QtCore import Qt
import sys
import configparser
import os
from recent_open_file import recent_open_file_widget,save_to_ini
from ui_file_container import  Ui_Container

#pyside6-uic file_container.ui -o ui_file_container.py
class file_container(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Container()
        self.ui.setupUi(self)
        self.widgets = []
        self.widgets_count = 0
        self.num_per_row = 4
        self.refresh_widgets_from_ini()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridlayout = QGridLayout(self.ui.frame_down)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)

        self.add_all_widget()
        #在下面设置ui中样式
        self.ui.frame_down.setStyleSheet("background-color: transparent;border: none;")

        #下面连接槽函数
        self.ui.delete_button.clicked.connect(self.delete_checkded_widget_from_ini)
        self.ui.add_button.clicked.connect(self.add_new_widget_to_ini)

    def refresh_widgets_from_ini(self):
        self.widgets = []
        self.widgets_count = 0
        config = configparser.ConfigParser()
        config.read('file_record.ini')
        for section in config.sections():
            video_path = config.get(section, 'video_path', fallback=None)
            print('video_path:', video_path)
            if video_path:
                self.widgets_count+=1
                widget = recent_open_file_widget(video_path=video_path)
                self.widgets.append(widget)
    def clear_widgets_from_gridlayout(self):
        while self.gridlayout.count():
            item = self.gridlayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
    def add_all_widget(self):
        self.clear_widgets_from_gridlayout()
        for index, widget in enumerate(self.widgets):
            row = index // self.num_per_row  # Calculate row number
            col = index % self.num_per_row  # Calculate column number
            self.gridlayout.addWidget(widget, row, col)

    def delete_checkded_widget_from_ini(self):
        print('delete begin')
        for widget in self.widgets:
            if widget.checked==True:
                widget.delete_self_from_ini()
        self.refresh_widgets_from_ini()
        self.add_all_widget()
        print('delete widget success')
    def add_new_widget_to_ini(self):
        open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold, "Pic File(*.mp4 *.mkv *.avi *.flv "
                                                                              "*.jpg *.png)")
        if name:
            save_to_ini(name)
            print(name +'save to ini success')
        self.refresh_widgets_from_ini()
        self.add_all_widget()
        return name

    def resizeEvent(self, event):
        new_num_per_row = max(1, self.width() // 130)
        if new_num_per_row != self.num_per_row:
            print('resize_to', new_num_per_row)
            self.num_per_row = new_num_per_row
            if(self.num_per_row<=len(self.widgets)):
                self.refresh_widgets_from_ini()
                self.add_all_widget()
        super().resizeEvent(event)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    container = file_container()
    container.show()
    sys.exit(app.exec_())