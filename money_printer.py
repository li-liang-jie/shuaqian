import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QGroupBox, QRadioButton, QComboBox, QLineEdit, QGridLayout
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class MoneyPrinter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("刷钱机")
        self.setGeometry(200, 100, 600, 700)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 1. 纸币图片
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        try:
            self.image_label.setPixmap(QPixmap("rmb100.jpg").scaled(500, 220, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        except Exception:
            self.image_label.setText("[人民币图片]")
        main_layout.addWidget(self.image_label)

        # 2. 面额选择
        amount_group = QGroupBox("选择面额：")
        amount_layout = QGridLayout()
        self.amount_buttons = []
        amounts = [
            "10元", "20元", "30元", "40元", "50元", "100元", "500元",
            "1000元", "5000元", "10000元", "50000元", "100000元", "1000000元", "10000000元"
        ]
        for i, text in enumerate(amounts):
            btn = QRadioButton(f"刷{text}的")
            if i == 0:
                btn.setChecked(True)
            self.amount_buttons.append(btn)
            amount_layout.addWidget(btn, i // 4, i % 4)
        amount_group.setLayout(amount_layout)
        main_layout.addWidget(amount_group)

        # 3. 下部区域
        bottom_layout = QHBoxLayout()

        # 左侧：银行、速度、卡号
        left_layout = QVBoxLayout()
        # 银行选择
        bank_layout = QHBoxLayout()
        bank_label = QLabel("请选择银行：")
        bank_label.setStyleSheet("color: blue;")
        self.bank_combo = QComboBox()
        self.bank_combo.addItems([
            "工商银行", "农业银行", "建设银行", "交通银行", "农业信用社"
        ])
        bank_layout.addWidget(bank_label)
        bank_layout.addWidget(self.bank_combo)
        left_layout.addLayout(bank_layout)
        # 速度设置
        speed_layout = QHBoxLayout()
        speed_label1 = QLabel("一秒")
        self.speed_edit = QLineEdit("100")
        self.speed_edit.setFixedWidth(60)
        speed_label2 = QLabel("张")
        speed_label1.setStyleSheet("color: blue;")
        self.speed_edit.setStyleSheet("color: blue;")
        speed_label2.setStyleSheet("color: blue;")
        speed_layout.addWidget(speed_label1)
        speed_layout.addWidget(self.speed_edit)
        speed_layout.addWidget(speed_label2)
        left_layout.addLayout(speed_layout)
        # 银行卡号输入
        self.card_edit = QLineEdit()
        self.card_edit.setPlaceholderText("请输入银行卡号！")
        left_layout.addWidget(self.card_edit)
        bottom_layout.addLayout(left_layout)

        # 右侧：操作按钮
        right_layout = QVBoxLayout()
        self.set_btn = QPushButton("确认设置")
        self.start_btn = QPushButton("开始刷钱")
        self.stop_btn = QPushButton("停止刷钱")
        right_layout.addWidget(self.set_btn)
        right_layout.addWidget(self.start_btn)
        right_layout.addWidget(self.stop_btn)
        bottom_layout.addLayout(right_layout)

        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyPrinter()
    window.show()
    sys.exit(app.exec()) 