"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from d_from_ui import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(['dec', 'bin', 'hex', 'oct'])

        self.init_signals()

    def init_signals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.dial.valueChanged.connect(lambda: self.ui.lcdNumber.display(self.ui.dial.value()))
        self.ui.dial.valueChanged.connect(lambda: self.ui.horizontalSlider.setValue(self.ui.dial.value()))
        self.ui.horizontalSlider.valueChanged.connect(
            lambda: self.ui.lcdNumber.display(self.ui.horizontalSlider.value()))
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.ui.dial.setValue(self.ui.horizontalSlider.value()))
        self.ui.comboBox.currentTextChanged.connect(self.set_lcd_mode)

        ...

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Вращение диала клавишами "+" и "-"
        """

        if event.key() == 43:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
            print(self.ui.dial.value())
        if event.key() == 45:
            self.ui.dial.setValue(self.ui.dial.value() - 1)
            print(self.ui.dial.value())

    def set_lcd_mode(self) -> None:
        """
        Изменение системы счисления для QLCDNumber
        """
        text = self.ui.comboBox.currentText()
        if text == 'dec':
            self.ui.lcdNumber.setDecMode()
        elif text == 'bin':
            self.ui.lcdNumber.setBinMode()
        elif text == 'hex':
            self.ui.lcdNumber.setHexMode()
        elif text == 'oct':
            self.ui.lcdNumber.setOctMode()
        # print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
