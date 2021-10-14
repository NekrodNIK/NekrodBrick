import sys

from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsScene, QMainWindow, QApplication
from interface.window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        img = Image.open("./example_image/cat.jpg")

        img = img.convert("P", palette=Image.ADAPTIVE,
                          colors=5).convert('RGBA')

        img = ImageEnhance.Contrast(img).enhance(3)

        img = (img.resize([64, 64], resample=Image.ADAPTIVE)).resize(
                img.size,
                Image.NEAREST
            )

        self.set_image(
            img
        )

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
