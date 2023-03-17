from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Iptx(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(611, 100, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffff00, stop:1 #ffa733);\n"
                                 "color : rgba(0, 0,0);\n"
                                 "border-radius:5px;\n"
                                 "\n"
                                 "")
        self.reset.setObjectName("reset")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(378, 115, 16, 16))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "\n"
                                    "border: 1px solid rgba(0,0, 0);\n"
                                    "\n"
                                    "border-radius:5px;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.hostid_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.hostid_txt.setGeometry(QtCore.QRect(170, 230, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.hostid_txt.setFont(font)
        self.hostid_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                      "color : rgba(0, 0,0);\n"
                                      "border-radius:5px;")
        self.hostid_txt.setText("")
        self.hostid_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.hostid_txt.setReadOnly(True)
        self.hostid_txt.setPlaceholderText("")
        self.hostid_txt.setObjectName("hostid_txt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(16, 230, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(438, 140, 251, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "border-radius:4px;\n"
                                    "")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.noscomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.noscomboBox.setGeometry(QtCore.QRect(316, 100, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.noscomboBox.setFont(font)
        self.noscomboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.noscomboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.noscomboBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#fdfc47, stop:1 #24fe41);\n"
                                       "color : rgba(0, 0,0);\n"
                                       "border-radius:5px;\n"
                                       "\n"
                                       "")
        self.noscomboBox.setObjectName("noscomboBox")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.noscomboBox.addItem("")
        self.BackgroundBehind_2 = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundBehind_2.setEnabled(True)
        self.BackgroundBehind_2.setGeometry(QtCore.QRect(16, 20, 673, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BackgroundBehind_2.sizePolicy().hasHeightForWidth())
        self.BackgroundBehind_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setKerning(True)
        self.BackgroundBehind_2.setFont(font)
        self.BackgroundBehind_2.setToolTipDuration(0)
        self.BackgroundBehind_2.setAutoFillBackground(False)
        self.BackgroundBehind_2.setStyleSheet("background: rgba(10,10, 10,150);\n"
                                              "border: 1px solid rgba(255,255, 255);\n"
                                              "\n"
                                              "border-radius:5px;\n"
                                              "")
        self.BackgroundBehind_2.setInputMethodHints(
            QtCore.Qt.ImhNoPredictiveText)
        self.BackgroundBehind_2.setText("")
        self.BackgroundBehind_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BackgroundBehind_2.setObjectName("BackgroundBehind_2")
        self.binary_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.binary_txt.setGeometry(QtCore.QRect(16, 140, 371, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.binary_txt.setFont(font)
        self.binary_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                      "color : rgba(0, 0,0);\n"
                                      "border-radius:5px;")
        self.binary_txt.setText("")
        self.binary_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_txt.setReadOnly(True)
        self.binary_txt.setObjectName("binary_txt")
        self.networkid_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.networkid_txt.setGeometry(QtCore.QRect(170, 260, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.networkid_txt.setFont(font)
        self.networkid_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                         "color : rgba(0, 0,0);\n"
                                         "border-radius:5px;")
        self.networkid_txt.setText("")
        self.networkid_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.networkid_txt.setReadOnly(True)
        self.networkid_txt.setPlaceholderText("")
        self.networkid_txt.setObjectName("networkid_txt")
        self.startcalc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.startcalc_btn.setGeometry(QtCore.QRect(437, 100, 161, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.startcalc_btn.setFont(font)
        self.startcalc_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startcalc_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffff00, stop:1 #ffa733);\n"
                                         "color : rgba(0, 0,0);\n"
                                         "border-radius:5px;\n"
                                         "\n"
                                         "")
        self.startcalc_btn.setObjectName("startcalc_btn")
        self.inputip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.inputip_txt.setGeometry(QtCore.QRect(16, 100, 286, 26))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.inputip_txt.setFont(font)
        self.inputip_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#fdfc47, stop:1 #24fe41);\n"
                                       "color : rgba(0, 0,0);\n"
                                       "border-radius:5px;\n"
                                       "\n"
                                       "")
        self.inputip_txt.setText("")
        self.inputip_txt.setFrame(False)
        self.inputip_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.inputip_txt.setObjectName("inputip_txt")
        self.subnets_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.subnets_txt.setGeometry(QtCore.QRect(438, 170, 251, 204))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subnets_txt.setFont(font)
        self.subnets_txt.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.subnets_txt.setMouseTracking(True)
        self.subnets_txt.setAutoFillBackground(False)
        self.subnets_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                       "color : rgba(0, 0,0);\n"
                                       "border-radius:5px;\n"
                                       "padding-left: 10;\n"
                                       "padding-top: 4\n"
                                       ";\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "")
        self.subnets_txt.setUndoRedoEnabled(False)
        self.subnets_txt.setReadOnly(True)
        self.subnets_txt.setPlainText("")
        self.subnets_txt.setBackgroundVisible(False)
        self.subnets_txt.setObjectName("subnets_txt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 0, 703, 421))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#434343, stop:1 #26323e);\n"
                                 "\n"
                                 "border: 5px solid rgba(255,255, 255);\n"
                                 "\n"
                                 "border-radius:5px; \n"
                                 "")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.classip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.classip_txt.setGeometry(QtCore.QRect(170, 170, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.classip_txt.setFont(font)
        self.classip_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                       "color : rgba(0, 0,0);\n"
                                       "border-radius:5px;")
        self.classip_txt.setText("")
        self.classip_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.classip_txt.setReadOnly(True)
        self.classip_txt.setPlaceholderText("")
        self.classip_txt.setObjectName("classip_txt")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(294, 115, 16, 16))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "\n"
                                    "border: 1px solid rgba(0,0, 0);\n"
                                    "\n"
                                    "border-radius:5px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(591, 115, 16, 16))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "\n"
                                    "border: 1px solid rgba(0,0, 0);\n"
                                    "\n"
                                    "border-radius:5px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 170, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(674, 115, 16, 16))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "\n"
                                    "border: 1px solid rgba(0,0, 0);\n"
                                    "\n"
                                    "border-radius:5px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.minimumip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.minimumip_txt.setGeometry(QtCore.QRect(170, 320, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.minimumip_txt.setFont(font)
        self.minimumip_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.minimumip_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                         "color : rgba(0, 0,0);\n"
                                         "border-radius:5px;")
        self.minimumip_txt.setText("")
        self.minimumip_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.minimumip_txt.setReadOnly(True)
        self.minimumip_txt.setPlaceholderText("")
        self.minimumip_txt.setObjectName("minimumip_txt")
        self.broadcastip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.broadcastip_txt.setGeometry(QtCore.QRect(170, 290, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.broadcastip_txt.setFont(font)
        self.broadcastip_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                           "color : rgba(0, 0,0);\n"
                                           "border-radius:5px;")
        self.broadcastip_txt.setText("")
        self.broadcastip_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.broadcastip_txt.setReadOnly(True)
        self.broadcastip_txt.setPlaceholderText("")
        self.broadcastip_txt.setObjectName("broadcastip_txt")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(16, 320, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(405, 95, 16, 16))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "\n"
                                    "border: 1px solid rgba(0,0, 0);\n"
                                    "\n"
                                    "border-radius:5px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.subnetmask_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.subnetmask_txt.setGeometry(QtCore.QRect(170, 200, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.subnetmask_txt.setFont(font)
        self.subnetmask_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                          "color : rgba(0, 0,0);\n"
                                          "border-radius:5px;")
        self.subnetmask_txt.setText("")
        self.subnetmask_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.subnetmask_txt.setReadOnly(True)
        self.subnetmask_txt.setPlaceholderText("")
        self.subnetmask_txt.setObjectName("subnetmask_txt")
        self.maximumip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.maximumip_txt.setGeometry(QtCore.QRect(170, 350, 217, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.maximumip_txt.setFont(font)
        self.maximumip_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.maximumip_txt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                         "color : rgba(0, 0,0);\n"
                                         "border-radius:5px;")
        self.maximumip_txt.setText("")
        self.maximumip_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.maximumip_txt.setReadOnly(True)
        self.maximumip_txt.setPlaceholderText("")
        self.maximumip_txt.setObjectName("maximumip_txt")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(16, 290, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setObjectName("label_8")
        self.subneting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.subneting_btn.setGeometry(QtCore.QRect(400, 100, 25, 281))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subneting_btn.setFont(font)
        self.subneting_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subneting_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #ff9a14,stop:1 #d32cff);\n"
                                         "color : rgba(0, 0,0);\n"
                                         "border-radius:5px;\n"
                                         "\n"
                                         "\n"
                                         "")
        self.subneting_btn.setObjectName("subneting_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(16, 350, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(571, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.help_btn.setMinimumSize(QtCore.QSize(18, 18))
        self.help_btn.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setBold(True)
        font.setWeight(75)
        self.help_btn.setFont(font)
        self.help_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_btn.setStyleSheet("background-color: rgb(5,195,221);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "border-radius:8px;")
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        self.pushButtonMinimize = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonMinimize.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonMinimize.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        self.pushButtonMinimize.setFont(font)
        self.pushButtonMinimize.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonMinimize.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                              "border-radius:8px;")
        self.pushButtonMinimize.setText("")
        self.pushButtonMinimize.setObjectName("pushButtonMinimize")
        self.horizontalLayout.addWidget(self.pushButtonMinimize)
        self.pushButtonMaximiz = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonMaximiz.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonMaximiz.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        self.pushButtonMaximiz.setFont(font)
        self.pushButtonMaximiz.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonMaximiz.setStyleSheet("background-color: rgb(255, 226, 0);\n"
                                             "border-radius:8px;")
        self.pushButtonMaximiz.setText("")
        self.pushButtonMaximiz.setObjectName("pushButtonMaximiz")
        self.horizontalLayout.addWidget(self.pushButtonMaximiz)
        self.pushButtonExit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonExit.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButtonExit.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExit.setStyleSheet("background-color:rgb(255, 97, 6);\n"
                                          "border-radius:8px;")
        self.pushButtonExit.setText("")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(16, 260, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 200, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                   "color : rgba(0, 0,0);\n"
                                   "border-radius:4px;\n"
                                   "padding-left: 10;")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(171, 170, 5, 235))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#434343, stop:1 #26323e);\n"
                                   "\n"
                                   "")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.subnetscomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.subnetscomboBox.setGeometry(QtCore.QRect(168, 380, 521, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subnetscomboBox.setFont(font)
        self.subnetscomboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.subnetscomboBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#abbaab, stop:1 #ffffff);\n"
                                           "color : rgba(0, 0,0);\n"
                                           "border-radius:5px;\n"
                                           "\n"
                                           "selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffff00, stop:1 #ffa733);\n"
                                           "color : rgba(0, 0,0);\n"
                                           "selection-color: rgb(0, 0, 0);\n"
                                           "padding-left: 45;")
        self.subnetscomboBox.setMinimumContentsLength(0)
        self.subnetscomboBox.setObjectName("subnetscomboBox")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(16, 380, 160, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
                                    "color : rgba(0, 0,0);\n"
                                    "border-radius:4px;\n"
                                    "")
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(392, 375, 40, 5))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color:#26323e\n"
                                    "\n"
                                    "")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label.raise_()
        self.reset.raise_()
        self.hostid_txt.raise_()
        self.label_5.raise_()
        self.label_10.raise_()
        self.noscomboBox.raise_()
        self.BackgroundBehind_2.raise_()
        self.binary_txt.raise_()
        self.networkid_txt.raise_()
        self.startcalc_btn.raise_()
        self.inputip_txt.raise_()
        self.subnets_txt.raise_()
        self.classip_txt.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_2.raise_()
        self.label_15.raise_()
        self.minimumip_txt.raise_()
        self.broadcastip_txt.raise_()
        self.label_7.raise_()
        self.subnetmask_txt.raise_()
        self.maximumip_txt.raise_()
        self.label_8.raise_()
        self.subneting_btn.raise_()
        self.label_6.raise_()
        self.layoutWidget.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.subnetscomboBox.raise_()
        self.label_16.raise_()
        self.label_9.raise_()
        self.label_17.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButtonExit.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reset.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">Resets All texts</span></p></body></html>"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.label_13.setText(_translate("MainWindow", "3"))
        self.hostid_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "HOST ID"))
        self.label_10.setText(_translate("MainWindow", "SUBNETS"))
        self.noscomboBox.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">Number of Subnets</span></p></body></html>"))
        self.noscomboBox.setItemText(0, _translate("MainWindow", "2"))
        self.noscomboBox.setItemText(1, _translate("MainWindow", "4"))
        self.noscomboBox.setItemText(2, _translate("MainWindow", "8"))
        self.noscomboBox.setItemText(3, _translate("MainWindow", "16"))
        self.noscomboBox.setItemText(4, _translate("MainWindow", "32"))
        self.noscomboBox.setItemText(5, _translate("MainWindow", "64"))
        self.noscomboBox.setItemText(6, _translate("MainWindow", "128"))
        self.binary_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.binary_txt.setPlaceholderText(
            _translate("MainWindow", "Your Binary IP Address"))
        self.networkid_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.startcalc_btn.setText(_translate(
            "MainWindow", "Start Calculating"))
        self.inputip_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">Your IP</span></p></body></html>"))
        self.inputip_txt.setPlaceholderText(
            _translate("MainWindow", "ENTER IP ADDRESS"))
        self.subnets_txt.setToolTip(_translate("MainWindow", "\n"
                                               "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.classip_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "CLASS IP"))
        self.label_15.setText(_translate("MainWindow", "5"))
        self.minimumip_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.broadcastip_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "MINIMUM IP"))
        self.label_14.setText(_translate("MainWindow", "4"))
        self.subnetmask_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.maximumip_txt.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "BROADCAST IP"))
        self.subneting_btn.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">Start Calculating subnets</span></p></body></html>"))
        self.subneting_btn.setText(_translate("MainWindow", "S\n"
                                              "U\n"
                                              "B\n"
                                              "N\n"
                                              "E\n"
                                              "T\n"
                                              "I\n"
                                              "N\n"
                                              "G"))
        self.label_6.setText(_translate("MainWindow", "MAXIMUM IP"))
        self.help_btn.setText(_translate("MainWindow", "H"))
        self.label_4.setText(_translate("MainWindow", "NETWORK ID"))
        self.label_3.setText(_translate("MainWindow", "SUBNET MASK"))
        self.label_16.setText(_translate("MainWindow", "BINARY SUBNETS"))
