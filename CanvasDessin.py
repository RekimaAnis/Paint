from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath
from PyQt5.QtCore import Qt
from Trace import Trace


class CanvasDessin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.traces = []
        self.current_trace = None
        self.pen_color = Qt.black  
        self.pen_width = 3       

    def setPenColor(self, color):
        self.pen_color = color

    def setPenWidth(self, width):
        self.pen_width = width

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.current_trace = Trace(width=self.pen_width, color=self.pen_color)
            self.current_trace.points.append(event.pos())

    def mouseMoveEvent(self, event):
        if self.current_trace and event.buttons() & Qt.LeftButton:
            self.current_trace.points.append(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.current_trace:
            self.traces.append(self.current_trace)
            self.current_trace = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for trace in self.traces:
            pen = QPen(trace.color, trace.width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)

            path = QPainterPath()
            if trace.points:
                path.moveTo(trace.points[0])
                for point in trace.points[1:]:
                    path.lineTo(point)
                painter.drawPath(path)

        if self.current_trace:
            pen = QPen(self.current_trace.color, self.current_trace.width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)

            path = QPainterPath()
            if self.current_trace.points:
                path.moveTo(self.current_trace.points[0])
                for point in self.current_trace.points[1:]:
                    path.lineTo(point)
                painter.drawPath(path)
