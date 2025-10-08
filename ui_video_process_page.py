# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_process_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_video_process_page(object):
    def setupUi(self, video_process_page):
        if not video_process_page.objectName():
            video_process_page.setObjectName(u"video_process_page")
        video_process_page.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(video_process_page.sizePolicy().hasHeightForWidth())
        video_process_page.setSizePolicy(sizePolicy)
        video_process_page.setMinimumSize(QSize(750, 500))
        video_process_page.setStyleSheet(u"")
        self.central_widget = QWidget(video_process_page)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy1)
        self.central_widget.setMinimumSize(QSize(0, 0))
        self.central_widget.setStyleSheet(u"#central_widget{\n"
"background-color: transparent;\n"
"}")
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.central_widget)
        self.header.setObjectName(u"header")
        self.header.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy2)
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setStyleSheet(u"#header {\n"
"background-color:rgb(230, 230, 230);\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.return_botton = QPushButton(self.header)
        self.return_botton.setObjectName(u"return_botton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.return_botton.sizePolicy().hasHeightForWidth())
        self.return_botton.setSizePolicy(sizePolicy3)
        self.return_botton.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        font.setBold(False)
        self.return_botton.setFont(font)
        self.return_botton.setStyleSheet(u"#return_botton{\n"
"background-color:rgba(205, 205, 205,170);  \n"
"border-radius: 4px;\n"
"color:black;\n"
"}\n"
" #return_botton:hover {\n"
"    background-color:rgba(215,215, 215,150) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"	border-radius: 4px;\n"
"    font-weight:2px;\n"
"}\n"
"#return_botton:selected{\n"
"    background-color: #45a049; /* \u70b9\u51fb\u65f6\u80cc\u666f\u989c\u8272\u7a0d\u5fae\u53d8\u6697 */\n"
"    transform: scale(0.95); /* \u6309\u94ae\u70b9\u51fb\u65f6\u7a0d\u5fae\u7f29\u5c0f\uff0c\u6a21\u62df\u6309\u4e0b\u7684\u6548\u679c */\n"
"}")
        icon = QIcon()
        icon.addFile(u"icon/home_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.return_botton.setIcon(icon)
        self.return_botton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.return_botton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.min_botton = QPushButton(self.header)
        self.min_botton.setObjectName(u"min_botton")
        sizePolicy3.setHeightForWidth(self.min_botton.sizePolicy().hasHeightForWidth())
        self.min_botton.setSizePolicy(sizePolicy3)
        self.min_botton.setMinimumSize(QSize(33, 30))
        self.min_botton.setMaximumSize(QSize(33, 30))
        self.min_botton.setStyleSheet(u"QPushButton{border:  none;}\n"
"QPushButton:hover {\n"
"background-color:rgba(175,175,175,150) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"border-radius:3px;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.min_botton.setIcon(icon1)
        self.min_botton.setIconSize(QSize(50, 20))

        self.horizontalLayout_2.addWidget(self.min_botton)

        self.max_botton = QPushButton(self.header)
        self.max_botton.setObjectName(u"max_botton")
        sizePolicy3.setHeightForWidth(self.max_botton.sizePolicy().hasHeightForWidth())
        self.max_botton.setSizePolicy(sizePolicy3)
        self.max_botton.setMinimumSize(QSize(33, 30))
        self.max_botton.setMaximumSize(QSize(33, 30))
        self.max_botton.setMouseTracking(True)
        self.max_botton.setStyleSheet(u"QPushButton{border:  none;}\n"
"QPushButton:hover {\n"
"background-color:rgba(175,175,175,150) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"border-radius:3px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/max.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_botton.setIcon(icon2)
        self.max_botton.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.max_botton)

        self.close_botton = QPushButton(self.header)
        self.close_botton.setObjectName(u"close_botton")
        sizePolicy3.setHeightForWidth(self.close_botton.sizePolicy().hasHeightForWidth())
        self.close_botton.setSizePolicy(sizePolicy3)
        self.close_botton.setMinimumSize(QSize(25, 25))
        self.close_botton.setMaximumSize(QSize(25, 25))
        self.close_botton.setMouseTracking(True)
        self.close_botton.setStyleSheet(u"QPushButton{border:  none;}\n"
"QPushButton:hover {\n"
"background-color:rgba(255,0,0,200) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"border-radius:3px;\n"
"}")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.close_botton.setIcon(icon3)
        self.close_botton.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.close_botton)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        self.main_page = QFrame(self.central_widget)
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.main_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.video_frame = QFrame(self.main_page)
        self.video_frame.setObjectName(u"video_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy4)
        self.video_frame.setMinimumSize(QSize(250, 0))
        self.video_frame.setStyleSheet(u"#video_frame{\n"
"background-color:rgb(247, 247, 247);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.video_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bar_frame = QFrame(self.video_frame)
        self.bar_frame.setObjectName(u"bar_frame")
        sizePolicy2.setHeightForWidth(self.bar_frame.sizePolicy().hasHeightForWidth())
        self.bar_frame.setSizePolicy(sizePolicy2)
        self.bar_frame.setMinimumSize(QSize(0, 35))
        self.bar_frame.setStyleSheet(u"QFrame {\n"
"border: 2px solid rgb(240, 240, 240); \n"
"border-top:transparent;\n"
"border-left:transparent;\n"
"border-right:transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.bar_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.process_bar = QProgressBar(self.bar_frame)
        self.process_bar.setObjectName(u"process_bar")
        sizePolicy3.setHeightForWidth(self.process_bar.sizePolicy().hasHeightForWidth())
        self.process_bar.setSizePolicy(sizePolicy3)
        self.process_bar.setMinimumSize(QSize(150, 0))
        self.process_bar.setMaximumSize(QSize(16777215, 20))
        self.process_bar.setStyleSheet(u"QProgressBar {\n"
"    background-color:transparent; /* \u80cc\u666f\u989c\u8272 */\n"
"    border: 2px  solid; /* \u8fb9\u6846 */\n"
"	border-color: rgba(24, 36, 255,200);\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"	padding:4px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(24, 36, 255,200); /* \u586b\u5145\u8fdb\u5ea6\u6761\u7684\u989c\u8272 */\n"
"    border-radius: 8px; /* \u586b\u5145\u90e8\u5206\u7684\u5706\u89d2 */\n"
"    border-radius: 4px; /* \u5706\u89d2 */\n"
"}")
        self.process_bar.setValue(24)
        self.process_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.process_bar)

        self.start_btn = QPushButton(self.bar_frame)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy3.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy3)
        self.start_btn.setMinimumSize(QSize(30, 30))
        self.start_btn.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"icon/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_btn.setIcon(icon4)
        self.start_btn.setIconSize(QSize(18, 18))
        self.start_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.start_btn)

        self.restart_btn = QPushButton(self.bar_frame)
        self.restart_btn.setObjectName(u"restart_btn")
        sizePolicy3.setHeightForWidth(self.restart_btn.sizePolicy().hasHeightForWidth())
        self.restart_btn.setSizePolicy(sizePolicy3)
        self.restart_btn.setMinimumSize(QSize(30, 30))
        self.restart_btn.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u"icon/restart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_btn.setIcon(icon5)
        self.restart_btn.setIconSize(QSize(20, 20))
        self.restart_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.restart_btn)


        self.verticalLayout_2.addWidget(self.bar_frame)

        self.verticalSpacer_2 = QSpacerItem(10, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.video_widget = QWidget(self.video_frame)
        self.video_widget.setObjectName(u"video_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.video_widget.sizePolicy().hasHeightForWidth())
        self.video_widget.setSizePolicy(sizePolicy5)
        self.video_widget.setMinimumSize(QSize(500, 350))

        self.verticalLayout_2.addWidget(self.video_widget)

        self.video_info_frame = QFrame(self.video_frame)
        self.video_info_frame.setObjectName(u"video_info_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.video_info_frame.sizePolicy().hasHeightForWidth())
        self.video_info_frame.setSizePolicy(sizePolicy6)
        self.video_info_frame.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"MS Gothic"])
        self.video_info_frame.setFont(font1)
        self.video_info_frame.setStyleSheet(u"QFrame{\n"
"Background-color:transparent;\n"
"border: none;\n"
"}\n"
"QLabel{\n"
"color:rgb(150, 150, 150);}")
        self.video_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.video_info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.video_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_video_dile_size = QLabel(self.video_info_frame)
        self.label_video_dile_size.setObjectName(u"label_video_dile_size")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(10)
        self.label_video_dile_size.setFont(font2)

        self.gridLayout_2.addWidget(self.label_video_dile_size, 2, 0, 1, 1)

        self.label_video_size = QLabel(self.video_info_frame)
        self.label_video_size.setObjectName(u"label_video_size")
        self.label_video_size.setFont(font2)

        self.gridLayout_2.addWidget(self.label_video_size, 2, 1, 1, 1)

        self.label_video_length = QLabel(self.video_info_frame)
        self.label_video_length.setObjectName(u"label_video_length")
        sizePolicy4.setHeightForWidth(self.label_video_length.sizePolicy().hasHeightForWidth())
        self.label_video_length.setSizePolicy(sizePolicy4)
        self.label_video_length.setFont(font2)

        self.gridLayout_2.addWidget(self.label_video_length, 1, 0, 1, 1)

        self.label_video_frame_rate = QLabel(self.video_info_frame)
        self.label_video_frame_rate.setObjectName(u"label_video_frame_rate")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_video_frame_rate.sizePolicy().hasHeightForWidth())
        self.label_video_frame_rate.setSizePolicy(sizePolicy7)
        self.label_video_frame_rate.setMinimumSize(QSize(0, 0))
        self.label_video_frame_rate.setFont(font2)

        self.gridLayout_2.addWidget(self.label_video_frame_rate, 1, 1, 1, 1)

        self.label_video_path = QLabel(self.video_info_frame)
        self.label_video_path.setObjectName(u"label_video_path")
        sizePolicy4.setHeightForWidth(self.label_video_path.sizePolicy().hasHeightForWidth())
        self.label_video_path.setSizePolicy(sizePolicy4)
        self.label_video_path.setFont(font2)

        self.gridLayout_2.addWidget(self.label_video_path, 0, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.video_info_frame)


        self.horizontalLayout_4.addWidget(self.video_frame)

        self.mode_chose_frame = QFrame(self.main_page)
        self.mode_chose_frame.setObjectName(u"mode_chose_frame")
        sizePolicy4.setHeightForWidth(self.mode_chose_frame.sizePolicy().hasHeightForWidth())
        self.mode_chose_frame.setSizePolicy(sizePolicy4)
        self.mode_chose_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mode_chose_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graph_frame = QFrame(self.mode_chose_frame)
        self.graph_frame.setObjectName(u"graph_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(6)
        sizePolicy8.setHeightForWidth(self.graph_frame.sizePolicy().hasHeightForWidth())
        self.graph_frame.setSizePolicy(sizePolicy8)
        self.graph_frame.setStyleSheet(u"#graph_frame{\n"
"background-color:rgb(255, 255, 255);\n"
"border: 2px solid rgb(240, 240, 240); \n"
"border-top:transparent;\n"
"border-left:transparent;\n"
"border-right:transparent;\n"
"}")

        self.verticalLayout.addWidget(self.graph_frame)

        self.input_frame = QFrame(self.mode_chose_frame)
        self.input_frame.setObjectName(u"input_frame")
        sizePolicy6.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
        self.input_frame.setSizePolicy(sizePolicy6)
        self.input_frame.setStyleSheet(u"#input_frame{\n"
"background-color:rgb(255, 255, 255);\n"
"border: 2px solid rgb(240, 240, 240); \n"
"border-left:transparent;\n"
"border-right:transparent;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.input_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.input_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(12)
        self.label.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label)

        self.leftframe = QFrame(self.input_frame)
        self.leftframe.setObjectName(u"leftframe")
        sizePolicy2.setHeightForWidth(self.leftframe.sizePolicy().hasHeightForWidth())
        self.leftframe.setSizePolicy(sizePolicy2)
        self.leftframe.setMinimumSize(QSize(0, 35))
        self.leftframe.setMaximumSize(QSize(16777215, 35))
        self.leftframe.setStyleSheet(u"#leftframe{\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}")
        self.leftframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.leftframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.input1 = QDoubleSpinBox(self.leftframe)
        self.input1.setObjectName(u"input1")
        self.input1.setMinimumSize(QSize(0, 15))
        self.input1.setStyleSheet(u" #input1{\n"
"	border-radius: 4px;\n"
"}")
        self.input1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input1.setDecimals(0)
        self.input1.setMaximum(999999999.000000000000000)
        self.input1.setSingleStep(10.000000000000000)
        self.input1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.input1.setValue(5.000000000000000)

        self.gridLayout_3.addWidget(self.input1, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.leftframe)

        self.label_2 = QLabel(self.input_frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(14)
        self.label_2.setFont(font4)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.rightframe = QFrame(self.input_frame)
        self.rightframe.setObjectName(u"rightframe")
        sizePolicy2.setHeightForWidth(self.rightframe.sizePolicy().hasHeightForWidth())
        self.rightframe.setSizePolicy(sizePolicy2)
        self.rightframe.setMinimumSize(QSize(0, 35))
        self.rightframe.setMaximumSize(QSize(16777215, 35))
        self.rightframe.setStyleSheet(u"#rightframe{\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}")
        self.rightframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.rightframe)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.input2 = QDoubleSpinBox(self.rightframe)
        self.input2.setObjectName(u"input2")
        self.input2.setMinimumSize(QSize(0, 15))
        self.input2.setStyleSheet(u" #input2{\n"
"	border-radius: 4px;\n"
"}")
        self.input2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input2.setDecimals(0)
        self.input2.setMaximum(999999999.000000000000000)
        self.input2.setSingleStep(10.000000000000000)
        self.input2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.input2.setValue(70.000000000000000)

        self.gridLayout_4.addWidget(self.input2, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.rightframe)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.input_frame)

        self.choseframe = QFrame(self.mode_chose_frame)
        self.choseframe.setObjectName(u"choseframe")
        sizePolicy6.setHeightForWidth(self.choseframe.sizePolicy().hasHeightForWidth())
        self.choseframe.setSizePolicy(sizePolicy6)
        self.choseframe.setStyleSheet(u"#choseframe{\n"
"background-color:rgb(255, 255, 255);\n"
"border: 2px solid rgb(240, 240, 240); \n"
"border-top:transparent;\n"
"border-left:transparent;\n"
"border-right:transparent;\n"
"}")
        self.choseframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.choseframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.choseframe)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mode_widget = QTabWidget(self.choseframe)
        self.mode_widget.setObjectName(u"mode_widget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.mode_widget.sizePolicy().hasHeightForWidth())
        self.mode_widget.setSizePolicy(sizePolicy9)
        font5 = QFont()
        font5.setFamilies([u"\u9ed1\u4f53"])
        font5.setBold(False)
        self.mode_widget.setFont(font5)
        self.mode_widget.setStyleSheet(u"QTabBar::tab {\n"
"color: rgb(108, 108, 108);\n"
"font: 14pt \"Franklin Gothic\";\n"
"height:40;\n"
"width:120;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"background: transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    height:40;\n"
"    color:rgba(57, 100, 255,230);\n"
"    border-bottom:1px solid;\n"
"    border-width:3px;\n"
"    border-color:rgba(24, 36, 255,200);\n"
"}\n"
"QWidget{\n"
"	background: transparent;\n"
"}\n"
"")
        self.tab_fx = QWidget()
        self.tab_fx.setObjectName(u"tab_fx")
        self.mode_widget.addTab(self.tab_fx, "")
        self.tab_ft = QWidget()
        self.tab_ft.setObjectName(u"tab_ft")
        self.mode_widget.addTab(self.tab_ft, "")

        self.gridLayout_5.addWidget(self.mode_widget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.choseframe)


        self.horizontalLayout_4.addWidget(self.mode_chose_frame)


        self.gridLayout.addWidget(self.main_page, 1, 0, 1, 1)

        video_process_page.setCentralWidget(self.central_widget)

        self.retranslateUi(video_process_page)

        self.mode_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(video_process_page)
    # setupUi

    def retranslateUi(self, video_process_page):
        video_process_page.setWindowTitle(QCoreApplication.translate("video_process_page", u"video_process_page", None))
        self.return_botton.setText(QCoreApplication.translate("video_process_page", u"\u56de\u5230\u4e3b\u9875\u9762", None))
        self.min_botton.setText("")
        self.max_botton.setText("")
        self.close_botton.setText("")
        self.start_btn.setText("")
        self.restart_btn.setText("")
        self.label_video_dile_size.setText(QCoreApplication.translate("video_process_page", u"\u6587\u4ef6\u5927\u5c0f", None))
        self.label_video_size.setText(QCoreApplication.translate("video_process_page", u"\u5206\u8fa8\u7387", None))
        self.label_video_length.setText(QCoreApplication.translate("video_process_page", u"\u957f\u5ea6", None))
        self.label_video_frame_rate.setText(QCoreApplication.translate("video_process_page", u"\u5e27\u901f\u7387", None))
        self.label_video_path.setText(QCoreApplication.translate("video_process_page", u"\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("video_process_page", u"\u6bd4\u4f8b\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("video_process_page", u"\uff1a", None))
        self.mode_widget.setTabText(self.mode_widget.indexOf(self.tab_fx), QCoreApplication.translate("video_process_page", u"Strain-t mode", None))
        self.mode_widget.setTabText(self.mode_widget.indexOf(self.tab_ft), QCoreApplication.translate("video_process_page", u"Stress-t mode", None))
    # retranslateUi

