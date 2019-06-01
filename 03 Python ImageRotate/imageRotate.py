import os
from PIL import Image

path = 'c://image/'
pathOutput = 'c://imageOutput/'

##-----------------------------------------------
def readFileListInFolder():
    fList =  os.listdir(path)
    fList.sort()
    return fList

##-----------------------------------------------
cnt = 0
file_list = readFileListInFolder()
#print(file_list)

def imageRotate(index):
    readPathFileName = path + file_list[index]
    print(readPathFileName)
    im = Image.open(readPathFileName)

    if (cnt%2 == 0) :
        im1 = im.transpose(Image.ROTATE_90) #시계방향
    else :
        im1 =im.transpose(Image.ROTATE_270) # 반시계 방향

    savePathFileName = pathOutput + file_list[index]
    im1.save(savePathFileName)
    return

##-----------------------------------------------


for i in range(len(file_list)):
    imageRotate(i)
    cnt = cnt + 1

print("***** Convert DONE *****")
