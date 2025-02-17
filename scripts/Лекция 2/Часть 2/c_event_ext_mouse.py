"""
Перехват и расширенная обработка событий мыши
"""

from time import ctime

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QHBoxLayout()
        self.pp = QtWidgets.QPushButton('button')
        self.pb = QtWidgets.QPushButton('next')
        self.setMouseTracking(True)
        layout.addWidget(self.pp)
        layout.addWidget(self.pb)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        #self.initUi()

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.pp:
            print(event.type())
            if event.type() == QtCore.QEvent.Type.Leave:
                print('Leave')
            if event.type() == QtCore.QEvent.Type.Enter:
                print('Enter')
                
        return super().eventFilter(watched, event)

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(300, 100)
        # self.setMouseTracking(True)

        self.label = QtWidgets.QLabel("Нажми на меня")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий нажатия мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        if event.button() == QtCore.Qt.LeftButton:
            print(ctime(), "mousePressEvent LEFT")
            self.label.setText("mousePressEvent LEFT")

        elif event.button() == QtCore.Qt.MiddleButton:
            print(ctime(), "mousePressEvent MIDDLE")
            self.label.setText("mousePressEvent MIDDLE")

        elif event.button() == QtCore.Qt.RightButton:
            print(ctime(), "mousePressEvent RIGHT")
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий отпускания мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        if event.button() == QtCore.Qt.LeftButton:
            print(ctime(), "mouseReleaseEvent LEFT")
            self.label.setText("mouseReleaseEvent LEFT")

        elif event.button() == QtCore.Qt.MiddleButton:
            print(ctime(), "mouseReleaseEvent MIDDLE")
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif event.button() == QtCore.Qt.RightButton:
            print(ctime(), "mouseReleaseEvent RIGHT")
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий двойного нажатия мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        if event.button() == QtCore.Qt.LeftButton:
            print(ctime(), "mouseDoubleClickEvent LEFT")
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif event.button() == QtCore.Qt.MiddleButton:
            print(ctime(), "mouseDoubleClickEvent MIDDLE")
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif event.button() == QtCore.Qt.RightButton:
            print(ctime(), "mouseDoubleClickEvent RIGHT")
            self.label.setText("mouseDoubleClickEvent RIGHT")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
