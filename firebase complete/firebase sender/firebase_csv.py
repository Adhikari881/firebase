import random
from datetime import datetime
import threading
import time
import csv
import pyrebase
print('Press Ctrl-C to quit..')



#fake data
def fun():
    value = random.randint(1,10)
    voltage = value
    outputValue= (1613.3202 * voltage) - 806.6601
    datapacket=[value,voltage,outputValue]
    timestamp=datetime.now().strftime('%H/%M/%S/%f')
    datapacket.insert(0, timestamp)
    #print(datapacket)
    return datapacket

#pushing data in file
def funtu():
    path = '.csv'
    new_path = '%s%s' % (datetime.now().strftime('%H%M%S%f'),path)

    with open('/Users/pc2/Desktop/rough work/good work/folder/'+new_path, 'w') as f:
        fieldnames = ['timestamp','value','outputvalue','voltage']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames)
        
        thewriter.writeheader()
        start_time = time.time()
        duration = 60
        
        while time.time() - start_time < duration:
            start_total = time.time()
            start_time_1 = time.time()
            duration_1 = 1
            arr=[]
            while time.time() - start_time_1 < duration_1:
                data = fun()
                packet = {'timestamp':data[0],
                        'value':data[1],
                        'voltage':data[2],
                        'outputvalue':data[3]}
                
                if len(arr)<10:
                    thewriter.writerow(packet)
                    arr.append(packet)
            start_firebase = time.time()   
            t1 = threading.Thread(target=upload_to_firebase, args=(arr,))
            t1.start()
            print(len(arr),arr[0])
            print(time.time()-start_firebase,"firebase upload time")
            
            print(time.time() - start_total,"total time per second")

            
            #time.sleep(1)
def upload_to_firebase(arr):
    db.child("lolo").push(arr)


config = {
    
   'apiKey': "AIzaSyDsgxpOrGxEPnShj4Mi-PRXu0_lLmJT96k",
  'authDomain': "pressure-sensor-38714.firebaseapp.com",
  'databaseURL': "https://pressure-sensor-38714-default-rtdb.firebaseio.com",
  'projectId': "pressure-sensor-38714",
  'storageBucket': "pressure-sensor-38714.appspot.com",
  'messagingSenderId': "928002848156",
  'appId': "1:928002848156:web:69748cb2db8d3c89bc4459",
  'measurementId': "G-X4T3LW5Q4W"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    funtu()
    





















