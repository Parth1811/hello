import numpy as np

def readfile(filepath):
    file = open(filepath,'r')
    data = []
    for line in file:
        content = line.split('\r\n')[0].split(',')
        list = (content[0], content[1])
        data.append(list)
    file.close()
    return data

def run(data , ranklist, marklist):
    flag = True
    print ('===========================================')
    print ("Type 'stop' with quotes to stop the program")
    print ('===========================================')
    while flag:
        print('Enter Roll Number: ')
        try:
            user_input = input()
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if user_input != 'stop':
            try:
                index = ranklist.index(user_input)
            except:
                print ('Invalid Roll no Try again')
                print('')
                continue
            rank = 1000 - index
            marks = data[user_input-1][1]
            tied = marklist.count(float(marks))
            print ('Marks: %s, Rank: %s, Tied Between: %s'%(marks,rank,tied))
            print('')
        else:
            flag = False


if __name__ == '__main__':
    filepath = 'Marksheet.csv'
    data = readfile(filepath)
    dtype = [('roll no', int),('marks',float)]
    num_data = np.array(data , dtype = dtype)
    sort_data = np.sort(num_data , order = 'marks')
    ranklist = sort_data['roll no'].tolist()
    marklist = sort_data['marks'].tolist()
    run(data, ranklist, marklist)

