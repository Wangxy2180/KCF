import os

current_path = os.path.dirname(os.path.abspath(__file__))
img_path='/Biker/img'   
path = current_path + img_path + ''

dirs=os.listdir(path)
dirs.sort()
f=open('images.txt','w')
for dir in dirs:
	img=path+'/'+dir
	f.write(img+'\n')

f.close()

