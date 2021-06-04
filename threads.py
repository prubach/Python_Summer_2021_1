import threading
import time

class MyThread(threading.Thread):
    def __init__(self, id, name, delay, counter):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print('starting thread: ' + self.name)
        while self.counter > 0:
            time.sleep(self.delay)
            print('{}: {} at {}'.format(self.name, time.ctime(time.time()), self.counter))
            self.counter -= 1
        print('finished thread: ' + self.name)


th1 = MyThread(1, 'th1', 1, 5)
th2 = MyThread(2, 'th2', 1, 5)
th3 = MyThread(3, 'th3', 1, 5)

th_list = [th1, th2, th3]
# Sequentially
#th1.run()
#th2.run()
#th3.run()

for th in th_list:
    th.start()
    #th.run()

print('All threads started')

for th in th_list:
    th.join()

print('Finished the program')