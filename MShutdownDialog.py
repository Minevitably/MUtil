import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PySide6.QtCore import QTimer

from Form import Ui_Form
from loguru import logger


class MShutdownDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shutdown Confirmation")
        self.setGeometry(100, 100, 300, 100)

        self.layout = QVBoxLayout()
        self.label = QLabel("系统将在 <span id='countdown'>60</span> 秒后关机。")
        self.layout.addWidget(self.label)

        self.confirm_button = QPushButton("确认关机")
        self.cancel_button = QPushButton("取消")
        self.layout.addWidget(self.confirm_button)
        self.layout.addWidget(self.cancel_button)

        self.setLayout(self.layout)

        self.confirm_button.clicked.connect(self.shutdown_system)
        self.cancel_button.clicked.connect(self.cancel_shutdown)

        self.countdown_time = 60  # 倒计时60秒
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)

        self.show()
        self.start_countdown()

    def start_countdown(self):
        self.timer.start(1000)  # 每秒触发一次

    def update_countdown(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.label.setText(f"系统将在 <span id='countdown'>{self.countdown_time}</span> 秒后关机。")
        else:
            self.shutdown_system()

    def shutdown_system(self):
        logger.info("Shutting down the system...")
        # 这里可以替换为实际的关机命令
        subprocess.Popen(["shutdown", "/s", "/t", "0"])
        self.timer.stop()
        self.close()

    def cancel_shutdown(self):
        logger.info("Shutdown canceled.")
        self.timer.stop()
        self.close()
