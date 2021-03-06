# -*- coding: utf-8 -*-
"""
brickv (Brick Viewer)
Copyright (C) 2009-2012 Olaf Lüke <olaf@tinkerforge.com>
Copyright (C) 2012-2014 Matthias Bolte <matthias@tinkerforge.com>
Copyright (C) 2014 Philipp Kroos <philipp.kroos@fh-bielefeld.de>

tab_window.py: Detachable container to be used in a TabBar (e.g. TabWidget)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QDialog, QAbstractButton, QTabBar, QPainter, \
                        QSizePolicy, QIcon

from brickv import config
from brickv.load_pixmap import load_pixmap
from brickv.utils import get_modeless_dialog_flags

class IconButton(QAbstractButton):
    clicked = pyqtSignal()

    def __init__(self, tab, default_icon, mouse_over_icon, parent=None):
        super(IconButton, self).__init__(parent)
        self.default_icon = default_icon
        self.mouse_over_icon = mouse_over_icon
        self.setIcon(default_icon)
        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        self.icon().paint(QPainter(self), event.rect())

    def sizeHint(self):
        return self.iconSize()

    def enterEvent(self, event):
        self.set_mouse_over_icon()

    def leaveEvent(self, event):
        self.set_default_icon()

    def mousePressEvent(self, event):
        self.clicked.emit()

    def set_mouse_over_icon(self):
        self.setIcon(self.mouse_over_icon)

    def set_default_icon(self):
        self.setIcon(self.default_icon)

class TabWindow(QDialog):
    """Detachable widget usable in a TabWidget. The widget can be detached
    from the TabWidget by calling untab(), added to it by calling tab(). If tabbed,
    it has a clickable icon visualizing mouseOver events; on click the button_handler
    of this class is called with the current index in the TabWidget.
    Callbacks called after the tabbing and before the  untabbing events
    can be registered."""

    def __init__(self, tab_widget, name, button_handler, parent=None):
        super(TabWindow, self).__init__(parent)

        self.tab_widget = tab_widget
        self.name = name
        self.button = None # see tab()
        self.button_handler = button_handler
        self.button_icon_default = QIcon(load_pixmap('tab-default-icon.png'))
        self.button_icon_mouse_over = QIcon(load_pixmap('tab-mouse-over-icon.png'))
        self.cb_on_tab = None
        self.cb_on_untab = None

    # overrides QDialog.closeEvent
    def closeEvent(self, event):
        self.tab()
        event.accept()

    # overrides QDialog.reject
    def reject(self):
        pass # ignore escape key, because QDialog.reject would hide the widget

    def untab(self):
        index = self.tab_widget.indexOf(self)
        if index > -1:
            if self.cb_on_untab != None:
                self.cb_on_untab(index)

            self.tab_widget.removeTab(index)
            self.setWindowFlags(get_modeless_dialog_flags(Qt.Window))
            self.setWindowTitle('Brick Viewer ' + config.BRICKV_VERSION + ' - ' + self.name)
            self.adjustSize()
            self.show()

    def tab(self):
        if self.windowFlags() & get_modeless_dialog_flags(Qt.Window):
            self.setWindowFlags(Qt.Widget)
            index = self.tab_widget.addTab(self, self.name)

            # (re-)instantiating button here because the TabBar takes ownership and
            # destroys it when this TabWindow is untabbed
            self.button = IconButton(self, self.button_icon_default,
                                     self.button_icon_mouse_over)
            self.tab_widget.tabBar().setTabButton(index, QTabBar.LeftSide, self.button)
            self.button.clicked.connect(lambda:
                                        self.button_handler(self.tab_widget.indexOf(self)))

            if self.cb_on_tab != None:
                self.cb_on_tab(index)

    def set_callback_on_tab(self, callback):
        self.cb_on_tab = callback

    def set_callback_on_untab(self, callback):
        self.cb_on_untab = callback
