import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from CanvasDessin import CanvasDessin

from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QColorDialog, QSlider, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap


class Dessin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zone de Dessin")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = CanvasDessin(self)
        self.setCentralWidget(self.canvas)

        self.initToolbar()

    def initToolbar(self):
        toolbar = QToolBar("Outils de Dessin")
        self.addToolBar(toolbar)

        self.color_action = QAction("Couleur", self)
        self.updateColorIcon()  
        self.color_action.triggered.connect(self.changeColor)
        toolbar.addAction(self.color_action)

        self.width_slider = QSlider(Qt.Horizontal, self)
        self.width_slider.setMinimum(1)
        self.width_slider.setMaximum(20)
        self.width_slider.setValue(3)  
        self.width_slider.valueChanged.connect(self.changeWidth)
        toolbar.addWidget(self.width_slider)

        clear_button = QPushButton("Effacer", self)
        clear_button.clicked.connect(self.clearCanvas)
        toolbar.addWidget(clear_button)

    def updateColorIcon(self):
        pixmap = QPixmap(16, 16)  
        pixmap.fill(self.canvas.pen_color)  
        icon = QIcon(pixmap)  
        self.color_action.setIcon(icon)  

    def changeColor(self):
        color = QColorDialog.getColor(self.canvas.pen_color, self, "Choisir une couleur")
        if color.isValid():
            self.canvas.setPenColor(color)
            self.updateColorIcon() 

    def changeWidth(self):
        self.canvas.setPenWidth(self.width_slider.value())

    def clearCanvas(self):
        self.canvas.traces = []
        self.canvas.current_trace = None
        self.canvas.update()

def main(args):
    app = QApplication(args)
    window = Dessin()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)