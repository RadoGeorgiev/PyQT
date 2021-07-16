# this is an example of Vertical layout - from top to bottom

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QVBoxLayout')

#1. creates layout object to control

layout = QVBoxLayout()

#2. Create 3 buttons in the layout - this way they are fixed to be visible

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))

#3. Set Layout to the app

window.setLayout(layout)

window.show()

sys.exit(app.exec_())