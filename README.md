## 下载Python

``
https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe
``

## 一路next安装

安装之后 在cmd打开目录

## 安装必要的库

``
pip install numpy opencv_contrib_python PyAutoGUI
``

## 然后运行

``
python fallen_doll.py
``

## 注意
要满敏感度，速度3，动作要失神也能用的，我用的是No.123
分辨率默认为1920x1080，如果想要更改，去`fallen_doll.py` line12: `resRate`改为1080p的n倍，2160p为2 (2160/1080=2)
如果遇到了在较新版本的python中的PyAutoGUI中的依赖问题，请 pip install Pillow
