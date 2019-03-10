import sys
import os
import time
from os.path import expanduser, join

file_name = ''

def lazy_name(task, P_or_T, folder_path):
    '''
    task is the acronym for task should be less than 3 letters
        ## DONT FORGET TO ADD UNDERSORCE AT THE END OF TASK NAME ##

    P_or_T is pool or transdeck should be strictly 'P' or 'T'
    F_or_B is front or bottom camera should be strictly 'F' or 'B'
    '''
    TASKNAME_LIST = [
        ('br' , 'buoy_red_'),
        ('bg' , 'buoy_green_'),
        ('by' , 'buoy_yellow_'),
        ('bir' , 'bin_red_'),
        ('big' , 'bin_green_'),
    ]

    task_found = False
    for task_map in TASKNAME_LIST:
        if task == task_map[0]:
            task = task_map[1]
            task_found = True
            break

    folder_list = folder_path.split('/')
    if folder_list[-1] == '':
        folder_list.pop(-1)
    short_folder_path = folder_list[-2]

    if P_or_T == 'P':
        P_or_T = 'pool'
    elif P_or_T == 'T':
        P_or_T = 'transdeck'
    else:
        short_folder_path = P_or_T

    if task_found:
        task_name = task + P_or_T
    else:
        task_name = task

    return task_name, short_folder_path

def trim_in_folder(folder_path):
    global file_name
    with open(join(folder_path, 'trim.txt'), 'r') as rf:
        ls = rf.readlines()
        home = expanduser("~")
        print(ls)
        for wrds in ls:
            l = wrds.strip('\n').split(" ")
            if l[0].find('.avi') == -1:
                if file_name.find('.avi') == -1:
                    raise AttributeError
                l = [file_name] + l
            file_name = join(folder_path, l[0])
            task_name, short_folder_path = lazy_name(l[3], l[4], folder_path)
            try:
                txtF = os.listdir(home + '/AUV_DataBase/' + task_name)
            except OSError:
                os.system('mkdir -p ' + home + '/AUV_DataBase/' + task_name)
                txtF = os.listdir(home + '/AUV_DataBase/' + task_name)
            num = txtF
            t1 = l[1].split(':')
            t2 = l[2].split(':')
            try:
                int(t1[2])
            except IndexError:
                t1 = [0] + t1
                t2 = [0] + t2
            tdf = (int(t2[0]) - int(t1[0])) * 3600 + (int(t2[1]) - int(t1[1])) *60 + (int(t2[2]) - int(t1[2]))
            t3 = time.strftime('%H:%M:%S', time.gmtime(tdf))
            os.system("ffmpeg -ss "+l[1]+" -i "+ file_name +" -t "+t3+" -c copy " + home+'/AUV_DataBase/'+task_name+"/"+str(len(num))+'_'+short_folder_path+'.avi')

if __name__ == '__main__':
    print ('starting......')
    trim_in_folder(expanduser('~/Videos2/front_camera_store_20170722_000002/0'))
