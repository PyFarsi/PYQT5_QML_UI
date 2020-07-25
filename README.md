# PYQT5 QML UI
Framework Modern UI PYQT5 QML Sample Modules By Javad

## Screenshot

**Material Design**

![Material](https://raw.githubusercontent.com/PyFarsi/PYQT5_QML_UI/master/ScreenShot/Material.jpg)

**Modern Design**

![Modern](https://raw.githubusercontent.com/PyFarsi/PYQT5_QML_UI/master/ScreenShot/Modern.jpg)

**Fusion Design**

![Fusion](https://raw.githubusercontent.com/PyFarsi/PYQT5_QML_UI/master/ScreenShot/Fusion.jpg)

**Imagine Design**

![Imagine](https://raw.githubusercontent.com/PyFarsi/PYQT5_QML_UI/master/ScreenShot/Imagine.jpg)

**Universal Design**

![Universal](https://raw.githubusercontent.com/PyFarsi/PYQT5_QML_UI/master/ScreenShot/Universal.jpg)

## How to update QML Resources

1. change QML files.
2. update **resources.qrc** file
3. ``pyrcc5 resources.qrc -o resfile.py``
4. import **resfile.py** into your main.py files

## Comilation Via Nuitka Command

``
nuitka Material.py --show-progress --recurse-all --standalone --plugin-enable=qt-plugins --include-qt-plugins=all --windows-disable-console
``

### PyFarsi Group 

Group in Telegram: [PyFarsi](https://t.me/PyFarsi)
