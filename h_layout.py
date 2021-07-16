# this is an example of Horizontal layout - from left to right

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')

#1. creates layout object to control

layout = QHBoxLayout()

#2. Create 3 buttons in the layout - this way they are fixed to be visible

layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))

#3. Set Layout to the app

window.setLayout(layout)

window.show()

sys.exit(app.exec_())