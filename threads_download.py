from queue import Queue
from threading import Thread

from knotprot_download import time_it, download_link, setup_download_dir, get_proteins

def run_sequentially(dir):
    for p in get_proteins():
        download_link(dir, p)

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) -> None:
        while True:
            mydir, prot = self.queue.get()
            try:
                download_link(mydir, prot)
            finally:
                self.queue.task_done()

def run_workers(mydir):
    proteins = get_proteins()
    queue = Queue()
    for n in range(4):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((mydir, p))
    queue.join()


mydir = setup_download_dir()
# Sequential
#time_it(run_sequentially, mydir)
# Workers
time_it(run_workers, mydir)
