#将所有的txt文件按照frame1,frame2,frame3融合在一起，不分训练集和测试集

import os
import shutil
import fileinput

#UCF-101数据集路径，在完成avi_to_png的转换之后
path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101'



#待写入的txt文件，frame1,frame2,frame3

ucf101_files_frame1  = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame1.txt','w')
ucf101_files_frame2  = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame2.txt','w')
ucf101_files_frame3  = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame3.txt','w')


dirs = os.listdir(path)
parent_dirs = []
for dir in dirs:
    parent_dirs.append(dir)

L1 = len(parent_dirs)


for i in range(L1):
    path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101/' + parent_dirs[i]
    new_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-txt-set/' + parent_dirs[i] + '/'
    os.makedirs(new_path)
    files = os.listdir(path)
    for file in files:

        #将生成的txt文件copy一份出来，放在新的目录下
        #方便查看和验证是否每个主题的视频都有得到txt文件
        #可以和avi_to_png_test(一些无法生成txt的视频)中的记录作一个比对

        if file.endswith('.txt'):
            absolute_file = path + '/' + file
            shutil.copy2(absolute_file, new_path)


        list = file.split('_')

        #读取文件，先判断是第几帧，将原txt文件按行写入相应的txt文件

        if file.endswith('frame1.txt'):
            frame1 = open( path + '/' + file,'r')
            lines = frame1.readlines()
            for line in lines:
                ucf101_files_frame1.write(line)
            frame1.close()

        elif file.endswith('frame2.txt'):
            frame2 = open( path + '/' + file,'r')
            lines = frame2.readlines()
            for line in lines:
                ucf101_files_frame2.write(line)
            frame2.close()

        elif file.endswith('frame3.txt'):
            frame3 = open( path + '/' + file,'r')
            lines = frame3.readlines()
            for line in lines:
                ucf101_files_frame3.write(line)
            frame3.close()


ucf101_files_frame1.close()
ucf101_files_frame2.close()
ucf101_files_frame3.close()
