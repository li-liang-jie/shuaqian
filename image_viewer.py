import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                           QVBoxLayout, QHBoxLayout, QWidget, QFileDialog)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image
import os

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片查看器")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # 创建布局
        layout = QVBoxLayout()
        
        # 创建图片显示标签
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumSize(400, 400)
        layout.addWidget(self.image_label)
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        
        # 创建打开图片按钮
        self.open_button = QPushButton("打开图片")
        self.open_button.clicked.connect(self.open_image)
        button_layout.addWidget(self.open_button)
        
        # 创建缩放按钮
        self.zoom_in_button = QPushButton("放大")
        self.zoom_in_button.clicked.connect(self.zoom_in)
        button_layout.addWidget(self.zoom_in_button)
        
        self.zoom_out_button = QPushButton("缩小")
        self.zoom_out_button.clicked.connect(self.zoom_out)
        button_layout.addWidget(self.zoom_out_button)
        
        layout.addLayout(button_layout)
        main_widget.setLayout(layout)
        
        # 初始化变量
        self.current_image = None
        self.scale_factor = 1.0
        
    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "选择图片",
            "",
            "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_name:
            self.load_image(file_name)
    
    def load_image(self, file_name):
        self.current_image = QPixmap(file_name)
        self.update_image()
    
    def update_image(self):
        if self.current_image:
            scaled_pixmap = self.current_image.scaled(
                self.current_image.width() * self.scale_factor,
                self.current_image.height() * self.scale_factor,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
    
    def zoom_in(self):
        self.scale_factor *= 1.25
        self.update_image()
    
    def zoom_out(self):
        self.scale_factor *= 0.8
        self.update_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec()) 