from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QSizePolicy, QPushButton, QStyleOptionButton, QStyle


# https://stackoverflow.com/questions/31742194/dynamically-resize-qicon-without-calling-setsizeicon
class QIconButton(QPushButton):
    def __init__(self, label=None, parent=None):
        super(QIconButton, self).__init__(label, parent)

        self.pad = 4  # padding between the icon and the button frame
        self.minSize = 8  # minimum size of the icon

        size_policy = QSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        self.setSizePolicy(size_policy)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        # ---- get default style ----

        opt = QStyleOptionButton()
        self.initStyleOption(opt)

        # ---- scale icon to button size ----

        rect = opt.rect

        h = rect.height()
        w = rect.width()
        icon_size = max(min(h, w) - 2 * self.pad, self.minSize)

        opt.iconSize = QSize(icon_size, icon_size)

        # ---- draw button ----

        self.style().drawControl(QStyle.CE_PushButton, opt, qp, self)

        qp.end()
