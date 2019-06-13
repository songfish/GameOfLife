import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入my_win.py中内容
from my_win import *
from gameoflife import *

# 创建mainWin类并传入Ui_MainWindow
class mainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMessage())

    def showMessage(self):
        s = GameofLife()
        matrix = np.zeros([20, 20], dtype=int)
        matrix[0, 1] = 1
        matrix[1, 0] = 1
        matrix[1, 2] = 1
        matrix[2, 0] = 1
        matrix[2, 2] = 1
        matrix[3, 1] = 1
        matrix[3, 2] = 1
        T = 50
        self.label.setText(s.game(matrix, T))

if __name__ == '__main__':
    # 下面是使用PyQt5的固定用法
    app = QApplication(sys.argv)
    main_win = mainWin()
    main_win.show()
    sys.exit(app.exec_())