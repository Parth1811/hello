import sys
import os
import time
from os.path import expanduser, join

file_name = ''

def lazy_name(task, variables, folder_path):
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
        ('e' , 'empty_'),
        ('g' , 'gate_'),
        ('m' , 'multi_'),
        ('p' , 'parking_'),
        ('mr' , 'maker_'),
        ('t' , 'torpedo'),
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

    if 'P' in variables:
        P_or_T = 'pool'
    elif 'T' in variables:
        P_or_T = 'transdeck'
    else:
        P_or_T = ''

    if 'L' in variables:
        L_or_D = 'light_'
    elif 'D' in variables:
        L_or_D = 'dark_'
    else:
        L_or_D = ''

    if 'F' in variables:
        F_or_N = 'far_'
    elif 'N' in variables:
        F_or_N = 'near_'
    else:
        F_or_N = ''

    task_name = task + L_or_D + F_or_N + P_or_T

    return task_name, short_folder_path

def trim_in_folder(folder_path):
    global file_name
    with open(join(folder_path, 'trim.txt'), 'r') as rf:
        ls = rf.readlines()
        home = expanduser("~")
        print(ls)
        for wrds in ls:
            try:
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
            except Exception as e:
                print (e)

def trim_recursive_folder(folder_path):
    for root, subdirs, files in os.walk(folder_path):
        for file in files:
            if file == 'trim.txt':
                print("------------------------------------------------------")
                print('Starting trim in folder ' + root)
                trim_in_folder(root)

if __name__ == '__main__':
    try:
        root_folder_path = sys.argv[1]
    except IndexError:
        root_folder_path = '.'
    trim_recursive_folder(expanduser(root_folder_path))
