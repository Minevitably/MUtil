@echo off
call conda activate PySideInsight
cd /d D:\MIY\PycharmProjects\MUtil
nuitka main.py --standalone --disable-console --enable-plugin=pyside6
pause