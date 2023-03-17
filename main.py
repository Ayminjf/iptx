import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from IptxCalc import Iptx
from Iptx import Ui_MainWindow_Iptx


class UiIptx(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.uiiptx = Ui_MainWindow_Iptx()
        self.uiiptx.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()
        self.btns()

    def mousePressEvent(self, evt):
        self.oldpos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldpos = evt.globalPos()

    def btns(self):
        self.uiiptx.startcalc_btn.clicked.connect(self.startCalculating)
        self.uiiptx.subneting_btn.clicked.connect(self.startSubneting)
        self.uiiptx.reset.clicked.connect(self.reset)
        self.uiiptx.help_btn.clicked.connect(self.helpa)

    def ip(self):
        return self.uiiptx.inputip_txt.text()

    def useriptx(self):  # user Ip Pass To Class
        return Iptx(self.ip())

    def startCalculating(self):
        # -> binaryIp - classIp - subnetMaskIp - hostIp - networkIp - broadcastIp - minimumIp - maximumIp

        try:
            inputip = self.uiiptx.inputip_txt.text()
            if (inputip != ""):
                ipsplite = list(Iptx(self.ip()).ipwxyz().values())
                if ((int(ipsplite[0]) < 223) & (int(ipsplite[1]) < 223) & (int(ipsplite[2]) < 223) & (int(ipsplite[3]) < 223)):

                    self.uiiptx.binary_txt.setText(
                        self.useriptx().binaryIp(self.ip()))
                    self.uiiptx.classip_txt.setText(
                        self.useriptx().classIp()[0])
                    self.uiiptx.subnetmask_txt.setText(
                        self.useriptx().subnetMaskIp())
                    self.uiiptx.hostid_txt.setText(self.useriptx().hostIp())
                    self.uiiptx.networkid_txt.setText(
                        self.useriptx().networkIp())
                    self.uiiptx.broadcastip_txt.setText(
                        self.useriptx().broadcastIp())
                    self.uiiptx.minimumip_txt.setText(
                        self.useriptx().minimumIp())
                    self.uiiptx.maximumip_txt.setText(
                        self.useriptx().maximumIp())
                    self.bcshnbmxmnToolTip()

                else:
                    QMessageBox.information(
                        self, "Error !?", "IP is out of range !!!")
            else:
                QMessageBox.information(
                    self, "Error !?", "Your IP should not be empty !!!")
        except:
            QMessageBox.information(self, "Error !?", "IP is not VALID !!!")

    def startSubneting(self):
        try:
            counter = int(0)
            subnetslist = self.useriptx().subnetsIp(
                int(self.uiiptx.noscomboBox.currentText()))
            self.uiiptx.subnets_txt.clear()
            for i in subnetslist:
                counter += 1
                self.uiiptx.subnets_txt.insertPlainText(
                    f"[{counter}] {str(i)} \n")
            self.startBinarySubneting()
        except:
            QMessageBox.information(
                self, "Error !?", "Your IP should not be empty !!!")

    def startBinarySubneting(self):
        counter = int(0)
        nos = int(self.uiiptx.noscomboBox.currentText())
        subnetslist = self.useriptx().subnetsBinaryIp(nos)
        self.uiiptx.subnetscomboBox.clear()
        # self.uiiptx.subnetscomboBox.addItem("")
        for i in subnetslist:
            counter += 1
            self.uiiptx.subnetscomboBox.addItem(
                f"[{counter}] {str(i)}")

        self.uiiptx.subnetscomboBox.addItem("")

    def setToolTipStyle(self, tip):
        return f"<p align=\"center\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">{tip}</span></p>"

    def bcshnbmxmnToolTip(self):
        self.uiiptx.binary_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().showIp()))
        self.uiiptx.classip_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().classIp()[1])))
        self.uiiptx.subnetmask_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().subnetMaskIp())))
        self.uiiptx.hostid_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().hostIp())))
        self.uiiptx.networkid_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().networkIp())))
        self.uiiptx.broadcastip_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().broadcastIp())))
        self.uiiptx.minimumip_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().minimumIp())))
        self.uiiptx.maximumip_txt.setToolTip(self.setToolTipStyle(
            self.useriptx().binaryIp(self.useriptx().maximumIp())))

    def reset(self):
        self.uiiptx.inputip_txt.clear()
        self.uiiptx.noscomboBox.setCurrentIndex(0)
        self.uiiptx.binary_txt.clear()
        self.uiiptx.classip_txt.clear()
        self.uiiptx.subnetmask_txt.clear()
        self.uiiptx.hostid_txt.clear()
        self.uiiptx.networkid_txt.clear()
        self.uiiptx.broadcastip_txt.clear()
        self.uiiptx.minimumip_txt.clear()
        self.uiiptx.maximumip_txt.clear()
        self.uiiptx.subnets_txt.clear()
        self.uiiptx.subnetscomboBox.clear()

    def setMessageBoxStyle(self, tip):
        return f"<p align=\"left\"><span style=\" font-family:\'consolas\'; font-size:11pt; font-weight:600;\">{tip}</span></p>"

    def helpa(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("Developer information")
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(self.setMessageBoxStyle(
            "Developer : Amin Jafari <br><br> GitHub : <a href='https://github.com/Aminjjjeffrey'>Aminjjjeffrey</a> <br><br> Gmail : <a href='mailto:aminjjjeffrey@gmail.com?subject=%3F&body=%3F'>Aminjjjeffrey@gmail.com</a>"))
        message_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = UiIptx()
    sys.exit(app.exec_())
