import os
import fileinput
import shutil


file_frame1 = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame1.txt','r')
lines_frame1 = file_frame1.readlines()


file_frame2 = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame2.txt','r')
lines_frame2 = file_frame2.readlines()


file_frame3 = open('C:/Users/smile/Desktop/ffmpeg test/ucf101_files_frame3.txt','r')
lines_frame3 = file_frame3.readlines()


file_frame1.close()
file_frame2.close()
file_frame3.close()

#UCF-101数据集路径，在完成avi_to_png的转换之后
themes_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101'


themes = []
for dir in os.listdir(themes_path):
    themes.append(dir)

L1 = len(themes)


for i in range(L1):
    dir = themes[i]
    j = 1
    for line in lines_frame1:
        if line.startswith(dir):
            #print(dir)

            new_path = dir + '_' + str( '%05d' % j )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            os.makedirs('C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path)
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            j = j + 1

    j = 1
    for line in lines_frame2:
        if line.startswith(dir):
            #print(dir)

            new_path = dir +  '_' + str( '%05d' % j )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            j = j + 1

    j = 1
    for line in lines_frame3:
        if line.startswith(dir):
            #print(dir)

            new_path = dir + '_' + str( '%05d' % j )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            j = j + 1










'''

for dir in os.listdir(themes_path):
    i = 1
    for line in lines_frame1:
        if line.startswith(dir):
            #print(dir)

            new_path = dir + '_' + str( '%05d' % i )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            os.makedirs('C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path)
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            i = i + 1

    i = 1
    for line in lines_frame2:
        if line.startswith(dir):
            #print(dir)

            new_path = dir +  '_' + str( '%05d' % i )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            i = i + 1

    i = 1
    for line in lines_frame3:
        if line.startswith(dir):
            #print(dir)

            new_path = dir + '_' + str( '%05d' % i )
            #print(new_path)

            new_absolute_path = 'C:/Users/smile/Desktop/ffmpeg test/UCF-101-FINAL/' + new_path
            #print(new_absolute_path)

            img = themes_path + '/' + line
            #print(img)
            img = img.rstrip('\n')
            #print(img)
            shutil.copy2(img, new_absolute_path)
            i = i + 1
'''
