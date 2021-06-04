from knotprot_download import time_it, download_link, setup_download_dir, get_proteins

def run_sequentially(dir):
    for p in get_proteins():
        download_link(dir, p)



mydir = setup_download_dir()
time_it(run_sequentially, mydir)