import sys

from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QFileDialog, QGraphicsScene,
                             QMainWindow, QApplication)

from interface.window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    class IMAGE_SETTINGS:
        isChangedSettings: bool

        size: tuple[int, int]
        filterBlackWhite: bool
        invertColor: bool
        contrastValue: float
        colorCount: int

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        update_timer = QtCore.QTimer(self)
        update_timer.setInterval(100)
        update_timer.timeout.connect(self.update_image)
        update_timer.start()

        self.IMAGE_SETTINGS.isChangedSettings = False
        self.IMAGE_SETTINGS.size = [self.WidthAndHeightSpinBox.value(),
                                    self.WidthAndHeightSpinBox.value()]
        self.IMAGE_SETTINGS.filterBlackWhite = (
                self.BlackWhiteModeButton.isChecked()
            )
        self.IMAGE_SETTINGS.invertColor = (
            self.InvertedColorButton.isCheckable()
        )
        self.IMAGE_SETTINGS.contrastValue = self.ContrastValueSpinBox.value()
        self.IMAGE_SETTINGS.colorCount = self.ColorCountSpinBox.value()

        self.OpenFileButton.clicked.connect(self.open_file)
        self.WidthAndHeightSpinBox.valueChanged.connect(
            self.change_width_and_height_value
        )
        self.BlackWhiteModeButton.stateChanged.connect(
            self.change_mode_filter_black_white
        )
        self.InvertedColorButton.stateChanged.connect(
            self.change_mode_inverted_color
        )
        self.ContrastValueSpinBox.valueChanged.connect(
            self.change_contrast_value
        )
        self.ColorCountSpinBox.valueChanged.connect(
            self.change_contrast_value
        )

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Открыть файл", "./")[0]
        self.image_raw = Image.open(file_path)
        self.IMAGE_SETTINGS.isChangedSettings = True

    def change_width_and_height_value(self):
        self.IMAGE_SETTINGS.size = [
                self.WidthAndHeightSpinBox.value(),
                self.WidthAndHeightSpinBox.value()
            ]
        self.IMAGE_SETTINGS.isChangedSettings = True

    def change_mode_filter_black_white(self):
        self.IMAGE_SETTINGS.filterBlackWhite = (
                self.BlackWhiteModeButton.isChecked()
            )
        self.IMAGE_SETTINGS.isChangedSettings = True

    def change_mode_inverted_color(self):
        self.IMAGE_SETTINGS.invertColor = self.InvertedColorButton.isChecked()
        self.IMAGE_SETTINGS.isChangedSettings = True

    def change_contrast_value(self):
        self.IMAGE_SETTINGS.contrastValue = self.ContrastValueSpinBox.value()
        self.IMAGE_SETTINGS.isChangedSettings = True

    def change_color_count(self):
        self.IMAGE_SETTINGS.colorCount = self.ColorCountSpinBox.value()
        self.IMAGE_SETTINGS.isChangedSettings = True

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
        if self.IMAGE_SETTINGS.isChangedSettings:
            print(1)

            self.IMAGE_SETTINGS.isChangedSettings = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
