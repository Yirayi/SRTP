# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_welcome_page(object):
    def setupUi(self, welcome_page):
        if not welcome_page.objectName():
            welcome_page.setObjectName(u"welcome_page")
        welcome_page.resize(1000, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(welcome_page.sizePolicy().hasHeightForWidth())
        welcome_page.setSizePolicy(sizePolicy)
        welcome_page.setMinimumSize(QSize(750, 450))
        welcome_page.setMaximumSize(QSize(16777215, 450))
        welcome_page.setStyleSheet(u"QMainWindow {\n"
"                background-color: white;\n"
"            }")
        self.central_widget = QWidget(welcome_page)
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
"background-color:white;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.min_botton = QPushButton(self.header)
        self.min_botton.setObjectName(u"min_botton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.min_botton.sizePolicy().hasHeightForWidth())
        self.min_botton.setSizePolicy(sizePolicy3)
        self.min_botton.setMinimumSize(QSize(33, 30))
        self.min_botton.setMaximumSize(QSize(33, 30))
        self.min_botton.setStyleSheet(u"QPushButton{border:  none;}\n"
"QPushButton:hover {\n"
"    background-color:rgba(175,175,175,150) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.min_botton.setIcon(icon)
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
"    background-color:rgba(175,175,175,150) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/max.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_botton.setIcon(icon1)
        self.max_botton.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.max_botton)

        self.close_botton = QPushButton(self.header)
        self.close_botton.setObjectName(u"close_botton")
        sizePolicy3.setHeightForWidth(self.close_botton.sizePolicy().hasHeightForWidth())
        self.close_botton.setSizePolicy(sizePolicy3)
        self.close_botton.setMinimumSize(QSize(33, 30))
        self.close_botton.setMaximumSize(QSize(33, 30))
        self.close_botton.setMouseTracking(True)
        self.close_botton.setStyleSheet(u"QPushButton{border:  none;}\n"
"QPushButton:hover {\n"
"    background-color:rgba(255,0,0,200) ;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6309\u94ae\u7684\u80cc\u666f\u8272 */\n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.close_botton.setIcon(icon2)
        self.close_botton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_botton)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        self.main_page = QFrame(self.central_widget)
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.main_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.welcome_frame = QFrame(self.main_page)
        self.welcome_frame.setObjectName(u"welcome_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.welcome_frame.sizePolicy().hasHeightForWidth())
        self.welcome_frame.setSizePolicy(sizePolicy4)
        self.welcome_frame.setMinimumSize(QSize(250, 0))
        self.welcome_frame.setStyleSheet(u"#welcome_frame{\n"
"background-color:white;\n"
"\n"
"border: 2px solid rgb(240, 240, 240); \n"
"border-bottom:transparent;\n"
"border-left:transparent;\n"
"border-right:transparent;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(10, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.video_widget = QWidget(self.welcome_frame)
        self.video_widget.setObjectName(u"video_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.video_widget.sizePolicy().hasHeightForWidth())
        self.video_widget.setSizePolicy(sizePolicy5)
        self.video_widget.setMinimumSize(QSize(80, 0))
        self.video_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.video_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.symbol_btn = QPushButton(self.video_widget)
        self.symbol_btn.setObjectName(u"symbol_btn")
        sizePolicy3.setHeightForWidth(self.symbol_btn.sizePolicy().hasHeightForWidth())
        self.symbol_btn.setSizePolicy(sizePolicy3)
        self.symbol_btn.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icon/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.symbol_btn.setIcon(icon3)
        self.symbol_btn.setIconSize(QSize(100, 100))
        self.symbol_btn.setFlat(True)

        self.gridLayout_2.addWidget(self.symbol_btn, 1, 1, 1, 1)

        self.label = QLabel(self.video_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.video_widget)

        self.tool_frame = QFrame(self.welcome_frame)
        self.tool_frame.setObjectName(u"tool_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.tool_frame.sizePolicy().hasHeightForWidth())
        self.tool_frame.setSizePolicy(sizePolicy6)
        self.tool_frame.setMinimumSize(QSize(0, 180))
        font1 = QFont()
        font1.setPointSize(9)
        self.tool_frame.setFont(font1)
        self.tool_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tool_frame.setStyleSheet(u"border:None;")
        self.tool_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tool_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.tool_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(181, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.open_new_frame = QFrame(self.tool_frame)
        self.open_new_frame.setObjectName(u"open_new_frame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.open_new_frame.sizePolicy().hasHeightForWidth())
        self.open_new_frame.setSizePolicy(sizePolicy7)
        self.open_new_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.open_new_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.open_new_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.open_new_btn = QPushButton(self.open_new_frame)
        self.open_new_btn.setObjectName(u"open_new_btn")
        sizePolicy3.setHeightForWidth(self.open_new_btn.sizePolicy().hasHeightForWidth())
        self.open_new_btn.setSizePolicy(sizePolicy3)
        self.open_new_btn.setMinimumSize(QSize(80, 80))
        self.open_new_btn.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u"icon/open_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_new_btn.setIcon(icon4)
        self.open_new_btn.setIconSize(QSize(80, 80))
        self.open_new_btn.setFlat(True)

        self.verticalLayout.addWidget(self.open_new_btn)

        self.label_new_video = QLabel(self.open_new_frame)
        self.label_new_video.setObjectName(u"label_new_video")
        sizePolicy2.setHeightForWidth(self.label_new_video.sizePolicy().hasHeightForWidth())
        self.label_new_video.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_new_video.setFont(font2)
        self.label_new_video.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_new_video)


        self.horizontalLayout.addWidget(self.open_new_frame)

        self.horizontalSpacer_3 = QSpacerItem(181, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.tool_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.welcome_frame)

        self.file_frame = QFrame(self.main_page)
        self.file_frame.setObjectName(u"file_frame")
        sizePolicy4.setHeightForWidth(self.file_frame.sizePolicy().hasHeightForWidth())
        self.file_frame.setSizePolicy(sizePolicy4)
        self.file_frame.setStyleSheet(u"#file_frame{\n"
"background-color:rgb(240,240,240);\n"
"}")

        self.horizontalLayout_4.addWidget(self.file_frame)


        self.gridLayout.addWidget(self.main_page, 1, 0, 1, 1)

        welcome_page.setCentralWidget(self.central_widget)

        self.retranslateUi(welcome_page)

        QMetaObject.connectSlotsByName(welcome_page)
    # setupUi

    def retranslateUi(self, welcome_page):
        welcome_page.setWindowTitle(QCoreApplication.translate("welcome_page", u"video_process_page", None))
        self.min_botton.setText("")
        self.max_botton.setText("")
        self.close_botton.setText("")
        self.symbol_btn.setText("")
        self.label.setText(QCoreApplication.translate("welcome_page", u" \u7eb3\u7c73\u6750\u6599\u529b\u5b66\u6027\u80fd\u5206\u6790", None))
        self.label_new_video.setText(QCoreApplication.translate("welcome_page", u"\u6253\u5f00\u65b0\u6587\u4ef6", None))
    # retranslateUi

