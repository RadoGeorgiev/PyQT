import sys

### simple hello world with PyQt5

# 1. add lib

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create app

app = QApplication(sys.argv)    ### when using command line arg /// alternative is empty list - app = QApplication([])

# 3. Create GUI

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# 4. Show app

window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())

