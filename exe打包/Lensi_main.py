'''
Author: your name
Date: 2022-03-21 13:57:01
LastEditTime: 2022-03-22 11:37:26
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Lensi\Lensi_main.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import qtmodern.styles
import qtmodern.windows
import Lensi_GUL,Lensi_all
from functools import partial
from PyQt5.QtCore import QObject, pyqtSignal,QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication

class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)
    def write(self, text):
        self.newText.emit(str(text))

# def GUL_install_1(app,source):
#     print(result)
#     Lensi_all.Lensi_install(result[0][4],result[0][7])
#     print("Installing")
# def GUL_install_2():
#     Lensi_all.Lensi_install(result[1][4],result[1][7])
#     print("Installing")
# def GUL_install_3():
#     Lensi_all.Lensi_install(result[2][4],result[2][7])
#     print("Installing")
# def GUL_install_4():
#     Lensi_all.Lensi_install(result[3][4],result[3][7])
#     print("Installing")
# def GUL_install_5():
#     Lensi_all.Lensi_install(result[4][4],result[4][7])
#     print("Installing")

def GUL_search(ui):
    app_name = ui.textEdit.toPlainText()
    app_num = [1,1,1,1,1]
    result = Lensi_all.Lensi_search(app_name,app_num)
    # print(result)
    #摆烂做法 ！！ 开摆了 (╯▔皿▔)╯
    try:
        ui.textBrowser.setText(result[0][0])
    except:
        pass
    try:
        ui.textBrowser_6.setText(result[1][0])
    except:
        pass
    try:
        ui.textBrowser_7.setText(result[2][0])
    except:
        pass
    try:
        ui.textBrowser_8.setText(result[3][0])
    except:
        pass
    try:
        ui.textBrowser_9.setText(result[4][0])
    except:
        pass

    try:
        ui.textBrowser_1.setText(result[0][2])
    except:
        pass
    try:
        ui.textBrowser_2.setText(result[1][2])
    except:
        pass
    try:
        ui.textBrowser_3.setText(result[2][2])
    except:
        pass
    try:
        ui.textBrowser_4.setText(result[3][2])
    except:
        pass
    try:
        ui.textBrowser_5.setText(result[4][2])
    except:
        pass

    try:
        ui.textBrowser_15.setText(result[0][7])
    except:
        pass
    try:
        ui.textBrowser_16.setText(result[1][7])
    except:
        pass
    try:
        ui.textBrowser_17.setText(result[2][7])
    except:
        pass
    try:
        ui.textBrowser_18.setText(result[3][7])
    except:
        pass
    try:
        ui.textBrowser_19.setText(result[4][7])
    except:
        pass

    try:
        ui.textBrowser_10.setText(result[0][1])
    except:
        pass
    try:
        ui.textBrowser_11.setText(result[1][1])
    except:
        pass
    try:
        ui.textBrowser_12.setText(result[2][1])
    except:
        pass
    try:
        ui.textBrowser_13.setText(result[3][1])
    except:
        pass
    try:
        ui.textBrowser_14.setText(result[4][1])
    except:
        pass

    try:
        ui.textBrowser_20.setText(result[0][3])
    except:
        pass
    try:
        ui.textBrowser_21.setText(result[1][3])
    except:
        pass
    try:
        ui.textBrowser_22.setText(result[2][3])
    except:
        pass
    try:
        ui.textBrowser_23.setText(result[3][3])
    except:
        pass
    try:
        ui.textBrowser_24.setText(result[4][3])
    except:
        pass

    try:
        ui.textBrowser_25.setText(result[0][4])
    except:
        pass
    try:
        ui.textBrowser_26.setText(result[1][4])
    except:
        pass
    try:
        ui.textBrowser_27.setText(result[2][4])
    except:
        pass
    try:
        ui.textBrowser_28.setText(result[3][4])
    except:
        pass
    try:
        ui.textBrowser_29.setText(result[4][4])
    except:
        pass
    # print(str(result[0][5]))
    # print(str(result[1][5]))
    # print(str(result[2][5]))
    # print(str(result[3][5]))
    # print(str(result[4][5]))
    try:
        if str(result[4][5]) != None:
            ui.webEngineView_5.load(QUrl(str(result[4][5])))
    except:
        pass
    try:
        if str(result[0][5]) != None:
            ui.webEngineView_1.load(QUrl(str(result[0][5])))
    except:
        pass
    try:
        if str(result[1][5]) != None:
            ui.webEngineView_2.load(QUrl(str(result[1][5])))
    except:
        pass
    try:
        if str(result[2][5]) != None:
            ui.webEngineView_3.load(QUrl(str(result[2][5])))
    except:
        pass
    try:
        if str(result[3][5]) != None:
            ui.webEngineView_4.load(QUrl(str(result[3][5])))
    except:
        pass
    # ui.pushButton_4.clicked.connect(partial(GUL_install_1(result[0][4],result[0][7])))
    # ui.pushButton_5.clicked.connect(partial(GUL_install_2(result[1][4],result[1][7])))
    # ui.pushButton_6.clicked.connect(partial(GUL_install_3(result[2][4],result[2][7])))
    # ui.pushButton_7.clicked.connect(partial(GUL_install_4(result[3][4],result[3][7])))
    # ui.pushButton_8.clicked.connect(partial(GUL_install_5(result[4][4],result[4][7])))
    return result
    # ui.webEngineView_1.load(str(result[0][5]))
    # ui.webEngineView_2.load(str(result[1][5]))
    # ui.webEngineView_3.load(str(result[2][5]))
    # ui.webEngineView_4.load(str(result[3][5]))
    # ui.webEngineView_5.load(str(result[4][5]))

def GUL_install_1(ui):
    app_name = ui.textBrowser_25.toPlainText()
    app_source= ui.textBrowser_15.toPlainText()
    Lensi_all.Lensi_install(app_name,app_source)
def GUL_install_2(ui):
    app_name = ui.textBrowser_26.toPlainText()
    app_source= ui.textBrowser_16.toPlainText()
    Lensi_all.Lensi_install(app_name,app_source)
def GUL_install_3(ui):
    app_name = ui.textBrowser_27.toPlainText()
    app_source= ui.textBrowser_17.toPlainText()
    Lensi_all.Lensi_install(app_name,app_source)
def GUL_install_4(ui):
    app_name = ui.textBrowser_28.toPlainText()
    app_source= ui.textBrowser_18.toPlainText()
    Lensi_all.Lensi_install(app_name,app_source)
def GUL_install_5(ui):
    app_name = ui.textBrowser_29.toPlainText()
    app_source= ui.textBrowser_19.toPlainText()
    Lensi_all.Lensi_install(app_name,app_source)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    MainWindow = QMainWindow()
    MainWindow.setWindowTitle("Lensi")
    ui = Lensi_GUL.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton_2.clicked.connect(Lensi_all.Lensi_init)
    ui.pushButton_3.clicked.connect(Lensi_all.Lensi_update_all)
    ui.pushButton.clicked.connect(partial(GUL_search, ui))
    ui.pushButton_4.clicked.connect(partial(GUL_install_1,ui))
    ui.pushButton_9.clicked.connect(partial(GUL_install_2,ui))
    ui.pushButton_6.clicked.connect(partial(GUL_install_3,ui))
    ui.pushButton_7.clicked.connect(partial(GUL_install_4,ui))
    ui.pushButton_8.clicked.connect(partial(GUL_install_5,ui))
    sys.exit(app.exec_())