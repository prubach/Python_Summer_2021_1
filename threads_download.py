import multiprocessing
from pathlib import Path
from queue import Queue
from threading import Thread
from multiprocessing.pool import Pool
from concurrent.futures.process import ProcessPoolExecutor

from functools import partial

from knotprot_download import time_it, download_link, setup_download_dir, get_proteins, create_thumbnail

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
    for n in range(8):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((mydir, p))
    queue.join()

### Multiprocessing
def run_multiprocessing(mydir):
    proteins = get_proteins()
    download = partial(download_link, mydir)
#    for p in proteins:
#        download(p)
    with Pool(16) as pool:
        pool.map(download, proteins)

### Thumbnails
def thumbnails_sequential():
    for image_path in Path('images').iterdir():
        print(image_path)
        create_thumbnail((192, 192), image_path)

def thumbnails_parallel():
    cr_thumb = partial(create_thumbnail, (192, 192))
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(cr_thumb, Path('images').iterdir())


mydir = setup_download_dir()
# Sequential
#time_it(run_sequentially, mydir)
# Workers
#time_it(run_workers, mydir)
# Multiprocessing
time_it(run_multiprocessing, mydir)
# Thumbnails
#time_it(thumbnails_sequential)
time_it(thumbnails_parallel)
