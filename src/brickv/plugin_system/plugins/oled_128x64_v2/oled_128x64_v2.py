# -*- coding: utf-8 -*-
"""
OLED128x64 Plugin
Copyright (C) 2018 Olaf Lüke <olaf@tinkerforge.com>

oled_128x64.py: OLED 128x64 Plugin Implementation

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

from PyQt4.QtCore import Qt, QSize, QPoint
from PyQt4.QtGui import QWidget, QImage, QPainter, QPen, QColor

from brickv.plugin_system.comcu_plugin_base import COMCUPluginBase
from brickv.async_call import async_call
from brickv.slider_spin_syncer import SliderSpinSyncer
from brickv.plugin_system.plugins.oled_128x64_v2.ui_oled_128x64_v2 import Ui_OLED128x64V2
from brickv.bindings.bricklet_oled_128x64_v2 import BrickletOLED128x64V2
from brickv.callback_emulator import CallbackEmulator

class ScribbleArea(QWidget):
    """
      this scales the image but it's not good, too many refreshes really mess it up!!!
    """
    def __init__(self, w, h, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.scribbling = 0

        self.width = w
        self.height = h
        self.image_pen_width = 5
        self.pen_width = 1
        self.circle_width = 30
        self.image = QImage(QSize(w, h), QImage.Format_RGB32)

        self.setMaximumSize(w*self.image_pen_width, w*self.image_pen_width)
        self.setMinimumSize(w*self.image_pen_width, h*self.image_pen_width)

        self.last_point = QPoint()
        self.clear_image()
        
    def clear_image(self):
        self.image.fill(Qt.black)
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.scribbling = 1
        elif event.button() == Qt.RightButton:
            self.last_point = event.pos()
            self.scribbling = 2

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.scribbling == 1:
            self.draw_line_to(event.pos())
        elif (event.buttons() & Qt.RightButton) and self.scribbling == 2:
            self.draw_line_to(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling == 1:
            self.draw_line_to(event.pos())
            self.scribbling = 0
        elif event.button() == Qt.RightButton and self.scribbling == 2:
            self.draw_line_to(event.pos())
            self.scribbling = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image.scaledToWidth(self.width*self.image_pen_width))

    def draw_line_to(self, end_point):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.white if self.scribbling == 1 else Qt.black,
                            self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.last_point/5, end_point/5)

        self.update()
        self.last_point = QPoint(end_point)

class OLED128x64V2(COMCUPluginBase, Ui_OLED128x64V2):
    def __init__(self, *args):
        COMCUPluginBase.__init__(self, BrickletOLED128x64V2, *args)

        self.setupUi(self)

        self.oled = self.device

        self.scribble_area = ScribbleArea(128, 64)
        self.image_button_layout.insertWidget(0, self.scribble_area)

        self.contrast_syncer = SliderSpinSyncer(self.contrast_slider, self.contrast_spin, lambda value: self.new_configuration())
        self.char_syncer = SliderSpinSyncer(self.char_slider, self.char_spin, self.char_slider_changed)

        self.draw_button.clicked.connect(self.draw_clicked)
        self.clear_button.clicked.connect(self.clear_clicked)
        self.send_button.clicked.connect(self.send_clicked)
        self.clear_display_button.clicked.connect(self.clear_display_clicked)
        self.invert_checkbox.stateChanged.connect(self.new_configuration)

        self.current_char_value = -1

        self.write_line_response_expected = False

    def char_slider_changed(self, value):
        if value != self.current_char_value:
            self.current_char_value = value
            self.write_chars(value)
            self.char_slider.setValue(value)

    def new_configuration(self):
        contrast = self.contrast_slider.value()
        invert = self.invert_checkbox.isChecked()
        self.oled.set_display_configuration(contrast, invert, True)

    def write_chars(self, value):
        if value > 248:
            value = 248
        for j in range(8):
            start = ""
            if value + j < 10:
                start = "  "
            elif value + j < 100:
                start = " "
            self.oled.write_line(j, 8, start + str(value+j) + ": " + chr(value+j) + '\0')

    def clear_display_clicked(self):
        self.oled.clear_display()

    def clear_clicked(self):
        self.scribble_area.clear_image()

    def send_clicked(self):
        line = int(self.line_combobox.currentText())
        pos = int(self.pos_combobox.currentText())
        text = self.text_edit.text()
        self.oled.write_line(line, pos, text)

    def draw_clicked(self):
        data = []
        for i in range(64):
            for j in range(128):
                if QColor(self.scribble_area.image.pixel(j, i)) == Qt.white:
                    data.append(True)
                else:
                    data.append(False)

        self.oled.write_pixels(0, 0, 127, 63, data)

    def cb_display_configuration(self, conf):
        self.contrast_slider.setValue(conf.contrast)
        self.invert_checkbox.setChecked(conf.invert)

    def cb_read_pixels(self, pixels):
        for i in range(64):
            for j in range(128):
                if pixels[i*128 + j]:
                    self.scribble_area.image.setPixel(j, i, 0xFFFFFF)
                else:
                    self.scribble_area.image.setPixel(j, i, 0)

        self.scribble_area.update()

    def start(self):
        # Use response expected for write_line function, to make sure that the
        # data queue can't fill up while you move the slider around.
        self.write_line_response_expected = self.oled.get_response_expected(self.oled.FUNCTION_WRITE_LINE)
        self.oled.set_response_expected(self.oled.FUNCTION_WRITE_LINE, True)

        async_call(self.oled.get_display_configuration, None, self.cb_display_configuration, self.increase_error_count)
        async_call(self.oled.read_pixels, (0, 0, 127, 63), self.cb_read_pixels, self.increase_error_count)

    def stop(self):
        self.oled.set_response_expected(self.oled.FUNCTION_WRITE_LINE, self.write_line_response_expected)

    def destroy(self):
        pass

    @staticmethod
    def has_device_identifier(device_identifier):
        return device_identifier == BrickletOLED128x64V2.DEVICE_IDENTIFIER
