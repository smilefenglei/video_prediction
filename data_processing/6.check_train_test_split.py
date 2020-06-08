import os
import shutil
#import fileinput



#####检查作者的划分，是否是将每个主题视频的g01-g07用作测试集，g08-g25用作训练集，并且同时检查每个主题视频是否最多有g25

#首先检查trainlist
test_dirs_1 = []
train_dirs_1 = []
extra_dirs_1 = []
trainlist = open( "C:/Users/smile/Desktop/ffmpeg test/ucf101_train_test_split/trainlist01.txt",'r')
lines = trainlist.readlines()
for line in lines:
    list = line.split('_')
    if list[2] in ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07' ]:
        test_dirs_1.append(line)
        print('trainlist is wrong')
    elif list[2] in ['g08', 'g09', 'g10', 'g11', 'g12', 'g13', 'g14' ,'g15', 'g16', 'g17', 'g18', 'g19', 'g20', 'g21', 'g22', 'g23', 'g24', 'g25' ]:
        train_dirs_1.append(line)
    else:
        extra_dirs_1.append(line)

trainlist.close()

#再检查testlist
test_dirs_2 = []
train_dirs_2 = []
extra_dirs_2 = []
testlist = open( "C:/Users/smile/Desktop/ffmpeg test/ucf101_train_test_split/testlist01.txt",'r')
lines = testlist.readlines()
for line in lines:
    list = line.split('_')
    if list[2] in ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07' ]:
        test_dirs_2.append(line)
    elif list[2] in ['g08', 'g09', 'g10', 'g11', 'g12', 'g13', 'g14' ,'g15', 'g16', 'g17', 'g18', 'g19', 'g20', 'g21', 'g22', 'g23', 'g24', 'g25' ]:
        train_dirs_2.append(line)
        print('testlist is wrong')
    else:
        extra_dirs_2.append(line)

testlist.close()



#####检查UCF-101中的所有数据是否都被作者用来训练和测试，通过分别检查UCF-101-original中g01-g07和g08-g25的视频个数是否等于trainlist01和testlist01的行数
path = 'D:/UCF-101-original/UCF-101-original'
dirs = os.listdir(path)
parent_dirs = []
for dir in dirs:
    parent_dirs.append(dir)

L1 = len(parent_dirs)

sub_train_dirs = []
sub_test_dirs  = []

for i in range(L1):
    path = 'D:/UCF-101-original/UCF-101-original/' + parent_dirs[i]
    dirs = os.listdir(path)
    for dir in dirs:
        '''
        print('------------------')
        print(parent_dirs[i])
        print(dir)
        '''
        list = dir.split('_')
        '''print(list)'''

        if list[2] in ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07' ]:
            sub_test_dirs.append(dir)
        if list[2] in ['g08', 'g09', 'g10', 'g11', 'g12', 'g13', 'g14' ,'g15', 'g16', 'g17', 'g18', 'g19', 'g20', 'g21', 'g22', 'g23', 'g24', 'g25' ]:
            sub_train_dirs.append(dir)

test_L2 = len(sub_test_dirs)
train_L2 = len(sub_train_dirs)

print(test_L2)
print(train_L2)
