import datetime
import sys
import os

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QFileDialog, QMessageBox, \
    QTextEdit
from shutil import copy

from libs.all_data_object import PathToFile
from libs.main_change import main_change


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass  # Необходимо для совместимости с sys.stdout


class FileUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.target_folder = output_folder

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Кнопки
        self.addButton = QPushButton('Добавить файлы', self)
        self.addButton.clicked.connect(self.addFiles)

        self.start_checking = QPushButton('Начать проверку', self)
        self.start_checking.clicked.connect(self.start)

        # Список файлов
        self.fileListWidget = QListWidget(self)
        self.fileListWidget.setFixedSize(900, 100)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # Запрещаем редактирование
        self.text_edit.setFixedSize(900, 400)
        self.redirect_stdout()
        self.stream.textWritten.connect(self.on_text_written)

        self.open_folder = None

        # Добавляем виджеты в макет
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.fileListWidget)
        self.layout.addWidget(self.start_checking)
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)
        self.setWindowTitle('Проверка файлов')
        self.resize(900, 500)

    def redirect_stdout(self):
        self.stream = EmittingStream()
        sys.stdout = self.stream
        sys.stderr = self.stream

    def on_text_written(self, text):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()
        QApplication.processEvents()

    def start(self):
        output_folder = "Результаты" + "_" + str(datetime.datetime.now().strftime("(%d.%m.%y)_%H-%M-%S"))
        PathToFile.output_folder = output_folder
        os.makedirs(output_folder)
        for i in range(self.fileListWidget.count()):
            source_file = self.fileListWidget.item(i).text()
            print(source_file)
            try:
                copy(source_file, os.path.join(output_folder, os.path.basename(source_file).replace(".xls", "")
                                               + "_" + str(datetime.datetime.now().strftime("(%d.%m.%y)_%H-%M-%S"))
                                               + ".xls"))
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось переместить файл: {str(e)}")
        main_change()
        if self.open_folder is None:
            self.open_folder = QPushButton('Открыть папку с проверенными файлами', self)
            self.open_folder.clicked.connect(self.open_result_folder)
            self.layout.addWidget(self.open_folder)

    def addFiles(self):
        self.fileListWidget.clear()
        files, _ = QFileDialog.getOpenFileNames(self, "Выберите файлы", "", "Все файлы (*)")
        if files:
            for file in files:
                self.fileListWidget.addItem(file)

    def open_result_folder(self):
        os.startfile(PathToFile.output_folder)


def www():
    app = QApplication(sys.argv)
    uploader = FileUploader()
    output_folder = "Проверенные файлы" + "_" + str(datetime.datetime.now().strftime("%d.%m.%y_%H.%M"))
    PathToFile.output_folder = output_folder
    uploader.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    www()
