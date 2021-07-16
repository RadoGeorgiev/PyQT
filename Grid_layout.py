import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()

# first row
layout.addWidget(QPushButton('Button(0,0)'),0,0)        ##### int coordinates - (row, column)
layout.addWidget(QPushButton('Button(0,1)'),0,1)
layout.addWidget(QPushButton('Button(0,2)'),0,2)

# second row

layout.addWidget(QPushButton('Button(1,0)'),1,0)
layout.addWidget(QPushButton('Button(1,1)'),1,1)
layout.addWidget(QPushButton('Button(1,2)'),1,2)

# third row

layout.addWidget(QPushButton('Button(2,0)'),2,0)
layout.addWidget(QPushButton('Button(2,1) + 2 Columns Span'), 2, 1, 1, 2)  # demonstrates row / column span

window.setLayout(layout)

window.show()

sys.exit(app.exec_())