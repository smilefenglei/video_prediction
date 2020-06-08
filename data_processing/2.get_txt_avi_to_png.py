
import os
import shutil
#UCF-101原始数据集路径
path_1 = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101'

sh_file = open('C:/Users/smile/Desktop/ffmpeg test/avi_to_png.txt','w')

####读取每个主题的文件夹名
####读取每个主题文件夹下的子视频名
####生成将每个主题的子视频转换成图片帧的单行指令，并且写入avi_to_png.txt文件中
####将最终得到的avi_to_png.txt文件中的内容复制粘贴，然后保存为以.sh结尾的脚本文件avi_to_png.sh
####打开git bash，运行avi_to_png.sh
####------注意：在得到avi_to_png.txt文件的过程中，UCF-101文件夹下只能包含主题视频
####-----------在运行avi_to_png.sh时，要将avi_to_png.sh和extract-ucf101.sh放到UCF-101中

for dir in os.listdir(path_1):
    path_2 = path_1 + '/' + dir
    for item in os.listdir(path_2):
        sh_file.write('/bin/sh extract-ucf101.sh ' + dir + '/' + item + '\n')


sh_file.close()
