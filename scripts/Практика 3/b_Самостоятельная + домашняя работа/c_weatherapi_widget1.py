"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаем элементы управления
        self.lat_label = QtWidgets.QLabel("Широта:")
        self.lat_input = QtWidgets.QLineEdit(self)
        self.lon_label = QtWidgets.QLabel("Долгота:")
        self.lon_input = QtWidgets.QLineEdit(self)
        self.delay_label = QtWidgets.QLabel("Задержка (сек):")
        self.delay_input = QtWidgets.QLineEdit(self)
        self.weather_output = QtWidgets.QTextEdit(self)
        self.start_stop_button = QtWidgets.QPushButton("Start", self)

        # Создаем поток WeatherHandler
        self.weather_handler_thread = None

        # Подключаем сигналы к слотам
        self.start_stop_button.clicked.connect(self.toggle_weather_thread)

        # Размещаем элементы управления на форме
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.lat_label)
        layout.addWidget(self.lat_input)
        layout.addWidget(self.lon_label)
        layout.addWidget(self.lon_input)
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.start_stop_button)
        layout.addWidget(self.weather_output)

    def toggle_weather_thread(self):
        if not self.weather_handler_thread or not self.weather_handler_thread.isRunning():
            # Если поток не существует или не запущен, создаем и запускаем его
            lat = float(self.lat_input.text())
            lon = float(self.lon_input.text())
            delay = float(self.delay_input.text())
            self.weather_handler_thread = WeatherHandler(lat, lon)
            self.weather_handler_thread.setDelay(delay)
            self.weather_handler_thread.weatherDataReceived.connect(self.update_weather)
            self.weather_handler_thread.start()
            self.lat_input.setDisabled(True)
            self.lon_input.setDisabled(True)
            self.delay_input.setDisabled(True)
            self.start_stop_button.setText('Stop')
        else:
            # Если поток запущен, останавливаем его
            self.weather_handler_thread.terminate()  # останавливает поток не разрушая его
            self.lat_input.setDisabled(False)
            self.lon_input.setDisabled(False)
            self.delay_input.setDisabled(False)
            self.start_stop_button.setText('Start')

    def update_weather(self, weather_data):
        # Обновляем поле вывода информации о погоде
        self.weather_output.clear()
        self.weather_output.insertPlainText(str(weather_data))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = WeatherWidget()
    widget.show()
    app.exec()
