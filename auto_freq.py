import numpy as np
import progressbar as pg
from math import sqrt
from datetime import datetime
import rospy


from auv_msgs.srv import auto_freq
from auv_msgs.srv import auto_freqResponse



NO_of_DATA = 500000
NO_OF_HYDROPHONE = 4

def data_read(filename):
    try:
        csv_file = open(filename,'r+')
       
    except IOError:
        print ("ERROR:       Invalid text_file path")
        return

    data = []
    for i in range(NO_OF_HYDROPHONE):
        data.append(np.zeros(NO_of_DATA))
    
    #bar = pg.ProgressBar(maxval = NO_of_DATA)
    #bar.start()
    
    for j in range(NO_of_DATA): 
        line = csv_file.readline()
        words = line.split(',')
        for i in range(NO_OF_HYDROPHONE):
            data[i][j] = float(words[i])
        #bar.update(j+1)

    #bar.finish()
    return data

def apply_fft(data):
    fft_data = []
    
    for i in range(NO_OF_HYDROPHONE):
        fft = np.fft.fft(data[i])
        fft_data.append(fft)
    return fft_data

def power_spec(fft_data):
    powr_spec = []
    for i in range(NO_OF_HYDROPHONE):
        powr_spec.append(np.zeros(NO_of_DATA/2))
    
    
    #bar = pg.ProgressBar(maxval = NO_of_DATA/2)
    #bar.start()
    for j in range(NO_of_DATA/2):
        for i in range(NO_OF_HYDROPHONE):
            abos = fft_data[i].real[j]**2 + fft_data[i].imag[j]**2
            powr_spec[i][j] = sqrt(sqrt(abos))
        #bar.update(j+1)
    #bar.finish()
    return powr_spec


def filter_intial(powr_spec):
    for i in range(NO_OF_HYDROPHONE):
        powr_spec[i][0:50000] = 0
        powr_spec[i][-80000:-1] = 0
        powr_spec[i][-1] = 0
        
        
def auto_freq_detect(fft_data):
    index = []
    for i in range(NO_OF_HYDROPHONE):
        index.append(fft_data[i].argmax())
        
    
    avg = 0
    for i in range(NO_OF_HYDROPHONE):
        avg = avg + index[i]/2
    
    avg = str(avg/NO_OF_HYDROPHONE)
    print ("========================================================")
    print ("========AUTO FREQUENCY DETECTED :"+avg+"================")
    print ("========================================================")
    return avg


def save_data(powr_spec):
    text_file = open ("PowerSpectrum" + datetime.now().strftime("%H:%M")\
                         + ".txt",'w')
    for i in range(NO_of_DATA/2):
        string = ''
        for j in range(NO_OF_HYDROPHONE):
            string += str(powr_spec[j][i]) + ','
        string += '\n'
        text_file.write(string)

def call_back(file_path):
#    file_path = req.filepath
    data  = data_read(file_path)
    fft_data = apply_fft(data)
    powr_spec = power_spec(fft_data)
    save_data(powr_spec)
    filter_intial(data)
    detected_freq = int(auto_freq_detect(data))

    print ("done")
#    return auto_freqResponse(detected_freq)


def auto_freq_server():
    rospy.init_node('auto_freq_server')
    s = rospy.Service('auto_freq_srv' , auto_freq, call_back)
    print ("Server ready to take request.......")
    rospy.spin()
  



if __name__ == '__main__' :
    filename = "/home/parth/hello/pinger/data7.txt"
    call_back(filename)




