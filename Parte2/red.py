import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(1000, 400, 1000, 1000)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.l1 = QLabel()
        self.l1.setText('tired')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1000, 1000)
    w.move(1000, 400)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
   '''