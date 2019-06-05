import os
from PIL import Image, ImageEnhance


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


#https://kite.com/python/examples/3186/pil-increase-the-brightness-of-an-image
#https://kite.com/python/examples/3183/pil-increase-the-sharpness-of-an-image
def ImageEnhanceModule(index):
    readPathFileName = path + file_list[index]
    print(readPathFileName)
    im = Image.open(readPathFileName)

    # brightness
    BR_enhancer = ImageEnhance.Brightness(im)
    BR_enhanced_im = BR_enhancer.enhance(1.8)

    #sharpness
    SH_enhancer = ImageEnhance.Sharpness(BR_enhanced_im)
    SH_enhanced_im = SH_enhancer.enhance(20.0)

    savePathFileName = pathOutput + file_list[index]
    SH_enhanced_im.save(savePathFileName)
    return

##-----------------------------------------------


for i in range(len(file_list)):
    ImageEnhanceModule(i)
    cnt = cnt + 1

print("***** Image Enance DONE *****")
