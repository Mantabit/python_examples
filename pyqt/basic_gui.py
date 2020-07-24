# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:21:39 2020

@author: dvarx
"""

from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QPushButton,QHBoxLayout,QSlider
from PyQt5.QtCore import Qt

app=QApplication([])

def top_btn_cb():
    global topbutton
    topbutton.setText("Clicked Top")
def slider_val_chgd(val):
    global sliderlabel
    sliderlabel.setText("Value changed:%-3d"%(val))

mainwindow=QWidget()

layout=QVBoxLayout()

toplayout=QHBoxLayout()
bottomlayout=QHBoxLayout()

topbutton=QPushButton("Top")
toplabel=QLabel("Top-Button: ")
toplayout.addWidget(toplabel)
toplayout.addWidget(topbutton)

bottombutton=QPushButton("Bottom")
bottomlabel=QLabel("Bottom-Button: ")
bottomlayout.addWidget(bottomlabel)
bottomlayout.addWidget(bottombutton)

sliderlabel=QLabel("Current Value:%-3d"%(0))
slider=QSlider(Qt.Horizontal)
slider.setTickPosition(QSlider.TicksBelow)
slider.setTickInterval(10)
slider.setMinimum(0)
slider.setMaximum(255)
slider.setValue(0)
slider.valueChanged.connect(slider_val_chgd)
sliderlayout=QVBoxLayout()
sliderlayout.addWidget(slider)
sliderlayout.addWidget(sliderlabel)

topbutton.clicked.connect(top_btn_cb)

layout.addLayout(toplayout)
layout.addLayout(bottomlayout)
layout.addLayout(sliderlayout)

mainwindow.setLayout(layout)

mainwindow.show()

app.exec_()