# Binder
python捆绑工具，exe+任意文件  

使用教程：  

1、安装python打包程序pyinstaller  

pip3 install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple  

需要将include下的pyinstaller.exe替换为你刚下载的pyinstaller，否则会报错  

你自己的pyinstaller.exe默认下载路径为  

C:\Users\用户名\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts  

2、运行Binder.py进行捆绑  

python Binder.py calc.exe 1.txt  

calc.exe：你要捆绑的exe文件  

1.txt：你的正常文件  

3、最后生成的exe文件在dist目录下  

dist\pyinstall.exe  
