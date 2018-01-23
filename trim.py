import os
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    num = 0
    file_name = ''
    os.system('mkdir ' + path + '/new')
    with open(path + 'time.txt', 'r') as fp:
        for line in fp:
            t_arr = line.split(',')
            if '.avi' in t_arr[0]:
                file_name = t_arr[0].split('\n')[0]
            else:
                num += 1
                start = t_arr[0]
                end = t_arr[1].split('\n')[0]
                #print start,end,file_name
                string = 'ffmpeg -y -i ' + path + file_name + ' -vcodec copy -ss ' + start + ' -to ' + end + ' ' + path + 'new/' + str(num) + '.avi;'
                #print string
                os.system(string)
