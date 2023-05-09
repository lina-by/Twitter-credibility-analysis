import threading
import time


result = [0]


def run2(lettre, result):
    for i in range(10):
        #print("thread ", lettre, " : ", i)
        time.sleep(0.09)
    result[0] = 3


m2 = threading.Thread(target=run2, args=('b', result))  # crée un second thread
m2.start()                 # démarre le thread,

enchainement = ['\\', '/', '-']
for i in range(0, 5):
    print("processing ", enchainement[i % 3], i)
    time.sleep(0.1)

m2.join()
print('result ', str(result[0]))
