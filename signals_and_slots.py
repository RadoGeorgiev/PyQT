# this file demonstrate signal and slot mechanism

import sys

import functools

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting(who):
    """Slot function"""

    if msg.text():
        msg.setText("")
    else:
        msg.setText(f'Hello {who}')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals&Slots")
layout = QVBoxLayout()

btn = QPushButton('Greet')
#btn.clicked.connect(functools.partial(greeting,'World!'))       # Connect clicked signal to slot function greeting ()
btn.clicked.connect(lambda x: greeting('World!'))                # using lambda instead calling function tools

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
