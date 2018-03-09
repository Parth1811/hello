import threading
import time

dam = True

def loop1_10():
    time.sleep(6)
    dam = False


threading.Thread(target=loop1_10).start()

while dam:
    print "yoyo"
