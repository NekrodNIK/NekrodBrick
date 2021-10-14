import sys

from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QFileDialog, QGraphicsScene,
                             QMainWindow, QApplication)

from interface.window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        update_timer = QtCore.QTimer(self)
        update_timer.setInterval(100)
        update_timer.timeout.connect(self.update_image)
        update_timer.start()

        self.OpenFileButton.clicked.connect(self.open_file)

        self.isChangedSettings = False

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Открыть файл", "./")[0]
        self.image_raw = Image.open(file_path)
        self.isChangedSettings = True

    def set_image(self, image: Image.Image):
        height = self.ImageView.height()-10
        image = image.resize(
            [height, height], Image.ADAPTIVE
        )

        imgQt = ImageQt(image.convert("RGBA"))
        pixmap = QtGui.QPixmap(QtGui.QImage(imgQt))

        scene = QGraphicsScene(self)
        scene.addPixmap(pixmap)
        self.ImageView.setScene(scene)

    def update_image(self):
        if self.isChangedSettings:
            print(1)

            self.isChangedSettings = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
