import numpy as np

#This is full path of csv file , can edit accordingly
filepath = '/home/parth/hello/Marksheet.csv'

def readfile(filepath):
    '''
    This function reads the data from the csv file
    stores it in a array of lists and return the array
    '''
    file = open(filepath,'r')
    data = []
    for line in file:
        content = line.split('\r\n')[0].split(',')
        list = (content[0], content[1])
        data.append(list)
    file.close()
    return data

def run(data , ranklist, marklist):
    '''
    This function takes the data array , sorted ranklist,and
    marklist as input, and responds to every user input by searching
    roll no in ranklist thus finding the rank extracting marks from data
    array and counting ties from the list of all marks
    '''
    flag = True
    print ('===========================================')
    print ("Type 'stop'with quotes to stop the program")
    print ('===========================================')
    while flag:
        print('Enter Roll Number: ')
        try:
            user_input = input()
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if str(user_input) != 'stop':
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
    data = readfile(filepath)
    #creating a numpy array
    dtype = [('roll no', int),('marks',float)]
    num_data = np.array(data , dtype = dtype)

    #storing the sorted array in increasing order of marks in sort_data
    sort_data = np.sort(num_data , order = 'marks')

    #slicing the sort_data array into marklist and ranklist
    ranklist = sort_data['roll no'].tolist()
    marklist = sort_data['marks'].tolist()

    #running the while  loop for user inputs
    run(data, ranklist, marklist)

