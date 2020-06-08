#根据得到的UCF-101-FINAL  triplets文件夹，根据训练集和测试集的划分，生成新的txt文件

import os
import shutil
import fileinput


#待写入的txt文件，frame1,frame2,frame3

test_frame1  = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_test_files_frame1.txt','w')
test_frame2  = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_test_files_frame2.txt','w')
test_frame3  = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_test_files_frame3.txt','w')
train_frame1 = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_train_files_frame1.txt','w')
train_frame2 = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_train_files_frame2.txt','w')
train_frame3 = open('/share1/home/fenglei/data/UCF-101-avi-to-png/train_test_split_txt/ucf101_train_files_frame3.txt','w')





path = '/share1/home/fenglei/data/UCF-101-avi-to-png/UCF-101-FINAL'
dirs = os.listdir(path)
#print(dirs)
dirs.sort()
#print(dirs)
parent_dirs = []
for dir in dirs:
    parent_dirs.append(dir)
    #print(dir)

L1 = len(parent_dirs)
#print(parent_dirs)


for i in range(L1):
    new_path = path + '/' + parent_dirs[i]
    print(parent_dirs[i])
    items = os.listdir(new_path)
    #print(items)
    items.sort()
    #print(items)
    for index, item in enumerate(items):
        list = item.split('_')
        #print(index)

        if list[2] in ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07' ]:
            if index == 0:
                test_frame1.write( parent_dirs[i] + '/' + item + '\n' )
            elif index == 1:
                test_frame2.write( parent_dirs[i] + '/' + item + '\n' )
            elif index == 2:
                test_frame3.write( parent_dirs[i] + '/' + item + '\n' )

        if list[2] in ['g08', 'g09', 'g10', 'g11', 'g12', 'g13', 'g14' ,'g15', 'g16', 'g17', 'g18', 'g19', 'g20', 'g21', 'g22', 'g23', 'g24', 'g25' ]:
            if index == 0:
                train_frame1.write( parent_dirs[i] + '/' + item + '\n')
            elif index == 1:
                train_frame2.write( parent_dirs[i] + '/' + item + '\n')
            elif index == 2:
                train_frame3.write( parent_dirs[i] + '/' + item + '\n')

test_frame1.close()
test_frame2.close()
test_frame3.close()
train_frame1.close()
train_frame2.close()
train_frame3.close()
