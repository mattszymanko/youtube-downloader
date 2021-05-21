#YouTube video and audio downloader based on PyTube and PyQt5
#Date: 20.05.2021
#Version: 0.2
#Original author: Teo Altinoz <teojakub06@gmai.com> GitHub: TheLostByte


from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
import sys
from pytube import YouTube
import threading


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(643, 650)
        self._form = Form
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.vid_url_edit = QLineEdit(Form)
        self.vid_url_edit.setObjectName(u"vid_url_edit")

        self.verticalLayout.addWidget(self.vid_url_edit)

        self.search_button = QPushButton(Form)
        self.search_button.setObjectName(u"search_button")
        self.search_button.clicked.connect(lambda: self.searchVideo(Form))

        self.verticalLayout.addWidget(self.search_button)

        self.vid_info_text = QTextBrowser(Form)
        self.vid_info_text.setObjectName(u"vid_info_text")

        self.verticalLayout.addWidget(self.vid_info_text)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.vid_path_edit = QLineEdit(Form)
        self.vid_path_edit.setObjectName(u"vid_path_edit")

        self.verticalLayout.addWidget(self.vid_path_edit)

        self.vid_options_combo = QComboBox(Form)
        self.vid_options_combo.setObjectName(u"vid_options_combo")

        self.verticalLayout.addWidget(self.vid_options_combo)

        self.download_button = QPushButton(Form)
        self.download_button.setObjectName(u"download_button")
        self.download_button.clicked.connect(lambda: self.downloadVideo(Form))

        self.verticalLayout.addWidget(self.download_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Youtube video downloader", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Enter video URL:</span></p></body></html>", None))
        self.search_button.setText(QCoreApplication.translate("Form", u"Search", None))
        self.vid_info_text.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Plesae enter video URL in the box above.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Options:</span></p></body></html>", None))
        self.vid_path_edit.setText(QCoreApplication.translate("Form", u"Path (optional)", None))
        self.download_button.setText(QCoreApplication.translate("Form", u"Download", None))


    def searchVideo(self, form):
        if not self.vid_url_edit.text():
            QMessageBox.about(form, "Error", "Error: Video URL not specified.")
            return
        self.yt = YouTube(self.vid_url_edit.text())
        self.yt.register_on_complete_callback(self.onComplete)
        self.vid_info_text.setHtml("<p>Video title: {}</p>".format(self.yt.title))
        self.vid_info_text.append("<p>Video author: {}</p>".format(self.yt.author))
        self.vid_info_text.append("<p>Video description: {}</p>".format(self.yt.description))
        self.vid_info_text.append("<p>Duration: {} seconds".format(self.yt.length))
        self.vid_info_text.append("<p>Views: {}".format(self.yt.views))
        self.data = self.yt.streams
        for i in range(len(self.data)):
        #don't toucha this. Seriously, don't.
            self.vid_options_combo.addItem(str(self.data[i])[31:52].replace('" res="', " resolution: ").replace('" abr="', " abr: ").strip('"'))
    
    def downloadVideo(self, form):
        if not self.vid_url_edit.text():
            QMessageBox.about(form, "Error", "Error: Video URL not specified.")
            return
        current_stream_id = self.vid_options_combo.currentIndex()
        itag = self.data[current_stream_id].itag
        stream = self.yt.streams.get_by_itag(itag)
        path = ''
        if not self.vid_path_edit.text() or not self.vid_path_edit.text() == "Path (optional)":
            path = self.vid_path_edit.text()
        stream.download(output_path = path)
        
    def onComplete(self, stream, file_path):
        QMessageBox.about(self._form, "Downloader", "Download complete.")
        
    
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()

    ui = Ui_Form()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())