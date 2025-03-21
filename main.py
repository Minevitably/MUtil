# This is a sample Python script.
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PySide6.QtCore import QTimer

from Form import Ui_Form
from loguru import logger

from MShutdownDialog import MShutdownDialog


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class MUtil(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        logger.info("btnClicked")

        # 执行批处理命令
        self.execute_commands()

        # 等待 1 分钟（60 秒）
        logger.info("Waiting for 1 minute before shutting down...")
        # 关机
        self.shutdown_dialog = MShutdownDialog()

    def execute_commands(self):
        commands = [
            "D:",
            "cd D:\\MIY\\vagrant\\dev",
            "start vagrant halt",
            "cd D:\\MIY\\vagrant\\omnibus",
            "start vagrant halt"
        ]

        for command in commands:
            try:
                # 使用 subprocess.run 执行命令
                subprocess.run(command, shell=True, check=True)
                logger.info(f"Executed: {command}")
            except subprocess.CalledProcessError as e:
                logger.error(f"Error executing command: {command} - {e}")

    def shutdown_system(self):
        try:
            logger.info("Shutting down the system...")
            subprocess.run("shutdown /s /t 0", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error shutting down the system: {e}")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    w = MUtil()
    w.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
