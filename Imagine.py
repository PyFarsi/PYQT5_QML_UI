import os
import sys

from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from UI import classres  



os.environ['QT_QUICK_CONTROLS_STYLE'] = "Imagine"
app = QApplication(sys.argv)

# Create QML engine
engine = QQmlApplicationEngine()

# Load the qml file into the engine
engine.load(QUrl('qrc:/UI/qml/main.qml'))

# Qml file error handling
if not engine.rootObjects():
    sys.exit(-1)

# Send QT_QUICK_CONTROLS_STYLE to main qml (only for demonstration)
qtquick2Themes = engine.rootObjects()[0].findChild(
    QObject,
    'qtquick2Themes'
)
qtquick2Themes.setProperty('text', os.environ['QT_QUICK_CONTROLS_STYLE'])
sys.exit(app.exec_())
