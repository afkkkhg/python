# class Calculator()
#   self.QGridLayout

#class ClassBtn(self):
#   def __init__(self):
#       super(self).__init__()

#       self.btn1 = 1
#       self.btn2 = 2
#       self.btn3 = 3
#       self.btn4 = 4
#       self.btn.clicked.connect(self.run)

#        widget = QWidget()
#        widget.setLayout(layout)
#        self.setCentralWidget(widget)


from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton

class Calculator(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.display = QLineEdit(self)
        self.grid = QGridLayout()

        buttons = ["7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   "0", ".", "=", "/"]

        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            self.grid.addWidget(QPushButton(button), row, col)
            col += 1

        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Calculator")
        self.show()

if name == "main":
    app = QApplication([])
    calculator = Calculator()
    app.exec()