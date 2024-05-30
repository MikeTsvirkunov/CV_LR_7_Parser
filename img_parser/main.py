import logging
import sys
sys.path.append("./")
sys.path.append("../")
from img_parser.constants import FilePathes, SearchParams
from img_parser.actors import ImagesToTensorFileLoader, ImgsLinkSearcher, search_links_pipline
from img_parser.initiators import driver_initiation
from threading import Thread

logging.basicConfig(level=logging.INFO, filename=FilePathes.logs_path,filemode="w")
driver_initiation()

def full_search_pipline(searching_param):
    data = search_links_pipline(searching_param)
    logging.info(f'Get {len(data)} hrefs for images')
    ImagesToTensorFileLoader(data).load()


if __name__ == '__main__':
    for param in SearchParams.search_params:
        full_search_pipline(param)
    # threads = list(map(
    #     lambda a: Thread(target=lambda: full_search_pipline(a)), 
    #     SearchParams.search_params
    # ))
    # for thread in threads:
        # thread.start()

