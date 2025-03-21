from loguru import logger
import subprocess
import sys
import os
import ctypes

def run_as_admin(batch_file_path):
    # 使用 ctypes 启动一个新的进程，以管理员权限运行指定的批处理文件
    try:
        logger.info("Running build.bat with admin privileges...")
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error occurred while running build.bat: {e}")
        sys.exit(1)

def main():
    # 配置日志
    logger.add("build.log", rotation="1 MB", level="DEBUG", backtrace=True, diagnose=True)

    # 批处理文件路径
    batch_file_path = r"D:\MIY\PycharmProjects\MUtil\build.bat"

    # 检查批处理文件是否存在
    if not os.path.exists(batch_file_path):
        logger.error("批处理文件未找到，请检查路径。")
        sys.exit(1)

    # 检查是否以管理员权限运行
    if ctypes.windll.shell32.IsUserAnAdmin():
        run_as_admin(batch_file_path)
    else:
        logger.info("Requesting admin privileges...")
        # 重新启动脚本以管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"{__file__}", None, 1)

if __name__ == "__main__":
    main()